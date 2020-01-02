class PathFilter(object):

    def __init__(self, app, conf):
        self.app = app

    def __call__(self, environ, start_response):

        if str(environ['PATH_INFO']).startswith('/path'):
            start_response(
                '200 OK',
                [
                    ('content-type', 'text/plain')
                ]
            )

            return "hello world"
        else:
            return self.app(environ, start_response)


def filter_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)

    def auth_filter(app):
        return PathFilter(app, conf)

    return auth_filter
