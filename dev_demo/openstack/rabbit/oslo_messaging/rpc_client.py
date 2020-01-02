import argparse
import socket
import time
import logging

import oslo_messaging as messaging
from oslo_config import cfg

logging.basicConfig(level=logging.DEBUG)


def init_config():
    """
    do not mix argparse with oslo_config
    :return:
    """

    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'topic',
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
        cfg.StrOpt(
            'exchange',
            default='test'
        )
    )
    cfg.CONF(
        project='test',
    )

    messaging.set_transport_defaults(
        control_exchange=cfg.CONF.exchange
    )


def main():
    init_config()
    transport = messaging.get_rpc_transport(cfg.CONF)
    target = messaging.Target(
        # queue name represents a topic
        topic=cfg.CONF.topic,
        # will send to a specific server
        server=cfg.CONF.server_name
    )
    client = messaging.RPCClient(
        transport,
        target,
        timeout=20
    )
    # print client.call(dict(), 'test', arg={'a': 'b', 'time': now})
    # print client.call(dict(), 'hello')

    # call: context, method, kwargs
    print client.call(dict(), 'stop')


if __name__ == "__main__":
    main()
