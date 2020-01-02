#!/usr/bin/env python

from sys import argv
import nova.conf
from nova import config
from nova import context
from nova.objects import register_all
from nova.scheduler.host_manager import HostManager
from oslo_config import cfg
from nova.db.sqlalchemy import api
from nova import objects

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
    CONF = cfg.CONF

    register_opts(CONF)
    CONF(
        project='host-test',
    )

    # host manager should use [api_database] connection
    api.configure(CONF)

    # print all host states
    hm = HostManager()
    ctx = context.get_admin_context()

    request_spec = objects.RequestSpec.get_by_instance_uuid(
        ctx,
        CONF.instance_id
    )

    print list(hm.get_host_states_by_uuids(
        ctx,
        None,
        request_spec
    ))
