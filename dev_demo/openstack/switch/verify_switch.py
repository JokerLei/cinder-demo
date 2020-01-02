#!/usr/bin/env python

import argparse
import sys
import netmiko
import contextlib
import logging

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)


@contextlib.contextmanager
def time_counter():
    import time
    now = time.time()
    try:
        yield
    except Exception:
        LOG.exception("execution failed")
    else:
        LOG.info(time.time() - now)


def init_parser(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--ip',
        help='ip address'
    )
    parser.add_argument(
        '--username',
        help='username'
    )
    parser.add_argument(
        '--password',
        help='password'
    )
    parser.add_argument(
        '--port',
        help='ethernet port'
    )
    parser.add_argument(
        '--device_type',
        default='cisco_nxos'
    )
    return parser.parse_args(args)


if __name__ == '__main__':

    args = init_parser(sys.argv[1:])
    ip = args.ip
    username = args.username
    password = args.password

    with time_counter():

        # ccreate connection
        # netmiko generalize functions
        # and provides a universal interface
        conn = netmiko.ConnectHandler(
            ip=ip,
            username=username,
            password=password,
            device_type=args.device_type
        )

        # use with clause to close connection
        # automatically
        with conn:
            conn.send_command('show vxlan')
            conn.send_command('show interface status | json')
