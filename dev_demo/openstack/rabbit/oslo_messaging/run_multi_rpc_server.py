import argparse
import eventlet
import logging
import socket
import time

from oslo_config import cfg
import oslo_messaging

logging.basicConfig(level=logging.DEBUG)

eventlet.monkey_patch()


def init_config():

    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'topic',
            default='test'
        )
    )
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'exchange',
            default='test'
        )
    )
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'server_name',
            default=socket.gethostname()
        )
    )
    cfg.CONF.register_cli_opt(
        cfg.IntOpt(
            'count',
            default=1000
        )
    )
    cfg.CONF(
        project='test',
    )

    oslo_messaging.set_transport_defaults(
        control_exchange=cfg.CONF.exchange
    )


# read oslo_messaging/rpc/server.py for more information
class ServerControlEndpoint(object):
    # despite claimed to be useful documented in from oslo_messaging/rpc/server.py,
    # it appears to me that this value here is ignored
    target = oslo_messaging.Target(topic='control', server='server1')

    def stop(self, ctx):
        print ctx
        return ctx


class TestEndpoint(object):

    def test(self, ctx, arg):
        print "received %s" % arg
        return time.time() - arg['time']

    def hello(self, ctx):
        return 'hello'


def run_server(transport, topic):

    target = oslo_messaging.Target(
        topic=topic,
        server=cfg.CONF.server_name
    )
    endpoints = [
        TestEndpoint(),
    ]
    server = oslo_messaging.get_rpc_server(
        transport, target, endpoints,
        executor='eventlet')
    try:
        print "starting"
        server.start()
    except KeyboardInterrupt:
        print("Stopping server")
    finally:
        server.stop()
        server.wait()

    return server



def main():

    init_config()
    count = cfg.CONF.count
    transport = oslo_messaging.get_rpc_transport(cfg.CONF)

    for i in range(0, count):
        import threading
        t = threading.Thread(target=run_server, args=(transport, "test_queue_%s" % i))
        t.daemon = True
        t.run()

    input('press any key to stop')







if __name__ == "__main__":
    main()
