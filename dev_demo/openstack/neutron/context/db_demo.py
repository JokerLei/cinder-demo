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

    # try an update commadn
    with db_api.context_manager.writer.using(admin_ctx):
        admin_ctx.session \
            .query(models_v2.Port) \
            .filter(models_v2.Port.id == port_id) \
            .update({"status": port_status})

        # will print port_status in the same transaction
        print admin_ctx.session \
            .query(models_v2.Port) \
            .filter(models_v2.Port.id == port_id) \
            .all()

        # this will always using subtransactions
        with db_api.context_manager.reader.using(admin_ctx):
            print admin_ctx.session \
                .query(models_v2.Port) \
                .filter(models_v2.Port.id == port_id) \
                .all()

        # to work around substransactions
        ctx_enginefacade = getattr(admin_ctx, '_enginefacade_context', None)
        old_ctx_enginefacde = None

        if ctx_enginefacade is not None:
            old_ctx_enginefacde = ctx_enginefacade
            admin_ctx._enginefacade_context = None

        with admin_ctx.session.begine(subtransaction=False):
            print admin_ctx.session \
                .query(models_v2.Port) \
                .filter(models_v2.Port.id == port_id) \
                .all()
        if old_ctx_enginefacde:
            admin_ctx._enginefacade_context = old_ctx_enginefacde

    # try a select command
    with db_api.context_manager.reader.using(admin_ctx):
        print admin_ctx.session \
            .query(models_v2.Port) \
            .filter(models_v2.Port.id == port_id) \
            .all()
