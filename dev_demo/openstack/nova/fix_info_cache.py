#!/usr/bin/env python

from nova import context
from nova.objects import register_all
from nova.scheduler.host_manager import HostManager
from oslo_config import cfg
#from nova.db.sqlalchemy import api
from nova.api.openstack import common
from nova import compute
from nova import config
from nova import network
from nova.network.neutronv2 import api as neutron_client
from nova.network.base_api import update_instance_cache_with_nw_info
from nova.network import model as network_model
import sys

import logging

logging.basicConfig(level=logging.INFO)


def register_opts(conf):
    conf.register_cli_opt(
        cfg.StrOpt(
            "instance_id"
        )
    )
    conf.register_cli_opt(
        cfg.BoolOpt(
            'preserve',
            default=True
        )
    )


if __name__ == '__main__':
    # register objects
    register_all()

    register_opts(cfg.CONF)
    config.parse_args(sys.argv)

    compute_api = compute.API()

    # host manager should use [api_database] connection
    # api.configure(cfg.CONF)

    # print all host states
    hm = HostManager()
    ctx = context.get_admin_context()
    instance = common.get_instance(
        compute_api,
        ctx,
        cfg.CONF.instance_id,
        expected_attrs=[
            'info_cache'
        ]
    )

    network_api = network.API()
    n_client = neutron_client.get_client(ctx, admin=True)

    existing_ports = n_client.list_ports(
        tenant_id=instance.project_id,
        device_id=instance.uuid
    ).get('ports', [])

    refreshed_vifs = []
    for port in existing_ports:

        # get network by port ids
        networks = network_api._get_available_networks(
            ctx,
            instance.project_id,
            [port['network_id']],
            n_client
        )

        # construct vif from port objects
        refreshed_vif = network_api._build_vif_model(
            ctx,
            n_client,
            port,
            networks,
            [port['id']] if cfg.CONF.preserve else []
        )
        refreshed_vifs.append(refreshed_vif)

    # update & create new cache
    update_instance_cache_with_nw_info(
        network_api,
        ctx,
        instance,
        nw_info=network_model.NetworkInfo.hydrate(refreshed_vifs),
        update_cells=True
    )
