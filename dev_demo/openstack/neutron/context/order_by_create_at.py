#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from oslo_config import cfg
from neutron_lib import context
from neutron.common import rpc as n_rpc
from neutron import objects
import logging
from neutron.common.config import setup_logging
from neutron.server import _init_configuration
from neutron.db import api as db_api
from neutron.db import models_v2

LOG = logging.getLogger(__name__)


def register_extra_opts(conf):
    conf.register_cli_opt(
        cfg.StrOpt(
            "port_id"
        )
    )

    conf.register_cli_opt(
        cfg.StrOpt(
            "port_status",
            default="unknown"
        )
    )


def init():
    register_extra_opts(cfg.CONF)
    _init_configuration()
    n_rpc.init(cfg.CONF)
    setup_logging()
    objects.register_objects()


if __name__ == "__main__":
    init()
    admin_ctx = context.get_admin_context()
    port_id = cfg.CONF.port_id
    port_status = cfg.CONF.port_status

    with db_api.context_manager.reader.using(admin_ctx):
        res = admin_ctx.session.query(models_v2.Port).join(
            models_v2.standard_attr.StandardAttribute
        ).filter(id=port_id).all()
        print res
