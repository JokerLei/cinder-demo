#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import sys
import webob
import six

from oslo_config import cfg
from oslo_log import log as logging

from neutron.agent.linux import utils as agent_utils
from neutron.agent.metadata import agent
from neutron.common import cache_utils as cache
from neutron.common import config
from neutron.common import utils
from neutron.conf.agent import common as agent_conf
from neutron.conf.agent.metadata import config as meta

LOG = logging.getLogger(__name__)


def main():
    meta.register_meta_conf_opts(meta.SHARED_OPTS)
    meta.register_meta_conf_opts(meta.UNIX_DOMAIN_METADATA_PROXY_OPTS)
    meta.register_meta_conf_opts(meta.METADATA_PROXY_HANDLER_OPTS)
    cache.register_oslo_configs(cfg.CONF)
    agent_conf.register_agent_state_opts_helper(cfg.CONF)
    config.init(sys.argv[1:])
    config.setup_logging()
    utils.log_opt_values(LOG)
    proxy = SjtUnixDomainMetadataProxyDemo(cfg.CONF)
    proxy.run()


class SjtUnixDomainMetadataProxyDemo(agent.UnixDomainMetadataProxy):

    def run(self):
        server = agent_utils.UnixDomainWSGIServer('neutron-metadata-agent')
        server.start(SjtMetadataPorxyHandlerDemo(self.conf),
                     self.conf.metadata_proxy_socket,
                     workers=self.conf.metadata_workers,
                     backlog=self.conf.metadata_backlog,
                     mode=self._get_socket_mode())
        self._init_state_reporting()
        server.wait()


class SjtMetadataPorxyHandlerDemo(agent.MetadataProxyHandler):

    @webob.dec.wsgify(RequestClass=webob.Request)
    def __call__(self, req):
        try:
            LOG.debug("Request: %s", req)

            path_info = req.path_info

            if str(path_info).startswith('/custom'):
                req.response.body = "Hello world"
                req.response.content_type = "text/plain"
                return

            instance_id, tenant_id = self._get_instance_and_tenant_id(req)
            if instance_id:
                return self._proxy_request(instance_id, tenant_id, req)
            else:
                return webob.exc.HTTPNotFound()

        except Exception:
            LOG.exception("Unexpected error.")
            msg = _('An unknown error has occurred. '
                    'Please try your request again.')
            explanation = six.text_type(msg)
            return webob.exc.HTTPInternalServerError(explanation=explanation)
