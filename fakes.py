import uuid

from oslo_service import wsgi
from oslo_utils import timeutils
import routes
import webob
import webob.dec
import webob.request

from cinder.api.middleware import auth
from cinder.api.middleware import fault
from cinder.api.openstack import api_version_request as api_version
from cinder.api.openstack import wsgi as os_wsgi
from cinder.api import urlmap
from cinder.api.v2 import limits
from cinder.api.v3 import limits
from cinder.api import versions
from cinder import context
from cinder.tests.unit import fake_constants as fake


class FakeRequestContext(context.RequestContext):
    def __init__(self, *args, **kwargs):
        user_id = '4740f066d77b4bcab8f7b4fe5a1c61d1'
        project_id = '1fc145617d5e4e97bad32c98b5d9b7c0'
        kwargs['auth_token'] = kwargs.get(user_id, project_id)
        super(FakeRequestContext, self).__init__(*args, **kwargs)


class HTTPRequest(webob.Request):

    @classmethod
    def blank(cls, *args, **kwargs):
        if args is not None:
            if 'v1' in args[0]:
                kwargs['base_url'] = 'http://localhost/v1'
            if 'v2' in args[0]:
                kwargs['base_url'] = 'http://localhost/v2'
            if 'v3' in args[0]:
                kwargs['base_url'] = 'http://localhost/v3'
        use_admin_context = kwargs.pop('use_admin_context', False)
        version = kwargs.pop('version', api_version._MIN_API_VERSION)
        out = os_wsgi.Request.blank(*args, **kwargs)
        user_id = '4740f066d77b4bcab8f7b4fe5a1c61d1'
        project_id = '1fc145617d5e4e97bad32c98b5d9b7c0'
        out.environ['cinder.context'] = FakeRequestContext(
            user_id,
            project_id,
            is_admin=use_admin_context)
        out.api_version_request = api_version.APIVersionRequest(version)
        return out
