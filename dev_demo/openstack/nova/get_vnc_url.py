#!/usr/bin/env python

from nova import context
from nova.objects import register_all
from nova.scheduler.host_manager import HostManager
from oslo_config import cfg
from nova.db.sqlalchemy import api
from nova.api.openstack import common
from nova import compute
from nova import rpc
import nova.conf
from nova import config
import sys

import logging

logging.basicConfig(level=logging.INFO)


def register_opts(conf):
    conf.register_cli_opt(
        cfg.StrOpt(
            "instance_id"
        )
    )


if __name__ == '__main__':
    # register objects
    register_all()

    register_opts(cfg.CONF)
    config.parse_args(sys.argv)

    compute_api = compute.API()

    # host manager should use [api_database] connection
    api.configure(cfg.CONF)

    # print all host states
    hm = HostManager()
    ctx = context.get_admin_context()
    instance = common.get_instance(
        compute_api,
        ctx,
        cfg.CONF.instance_id
    )

    # print compute_api.get_vnc_console(
    #     ctx,
    #     instance,
    #     "novnc"
    # )

    print compute_api.compute_rpcapi.get_vnc_console(
        ctx,
        instance=instance,
        console_type='novnc'
    )
