import webob


class PathFilter(object):

    def __init__(self, app, path):
        self.app = app
        self.path = path

    @webob.dec.wsgify(RequestClass=webob.Request)
    def __call__(self, req):

        path_info = req.path_info

        if str(path_info).startswith(self.path):
            req.response.content_type = 'text/plain'
            req.response.body = "hello world from path filter"
            return
        else:
            return self.app


def filter_factory(global_conf, path):
    if not str(path).startswith('/'):
        path = '/' + path

    def auth_filter(app):
        return PathFilter(app, path)

    return auth_filter
