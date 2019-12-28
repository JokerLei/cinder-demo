from cinder.common import constants as vol_constants
from cinder import context
from cinder import objects, rpc, coordination
from oslo_config import cfg
from oslo_log import log

from dev_demo.openstack.cinder import init_app

from cinder.api import extensions
import routes
import webob
import webob.dec
import webob.request

from cinder.api.openstack import api_version_request as api_version
from cinder.api.openstack import wsgi as os_wsgi
from cinder.api.v2 import limits
from cinder.api.v3 import limits
from cinder.api import versions

import fakes

LOG = log.getLogger(__name__)


def register_opts():
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'volume_id',
            required=False
        )
    )
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'image_id',
            required=False,
            default=None
        )
    )
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'auth_token',
            required=False
        )
    )


if __name__ == '__main__':
    register_opts()
    backend, host, db_driver = init_app()
    if not rpc.initialized():
        rpc.init(cfg.CONF)
    #coordination.COORDINATOR.start()

    from cinder.volume.api import API
    from cinder.api.v3.volumes import VolumeController

    req = fakes.HTTPRequest.blank('/v2/volumes/detail?all_tenants=True', use_admin_context=True)
    #req = fakes.HTTPRequest.blank('/v2/volumes/detail')
    ext_mgr = extensions.ExtensionManager()
#    ext_mgr.extensions = {}
    volume_control = VolumeController(ext_mgr)
    vols = volume_control.detail(req)
#    ctx = context.get_admin_context()
#
#    volume_api = API()
#    vols = volume_api.get_all(
#        ctx, filters={"all_tenants": True}
#    )
    print(vols)
    print(len(vols['volumes']))
