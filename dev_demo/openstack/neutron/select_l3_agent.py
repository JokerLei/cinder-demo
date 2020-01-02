#!/usr/bin/env python

from oslo_config import cfg
from neutron_lib import context
from neutron.plugins.ml2.plugin import Ml2Plugin
from neutron.common import rpc as n_rpc
from neutron import objects
import logging
from neutron_lib.plugins import directory
from neutron_lib.plugins import constants as lib_const
from neutron.common.config import setup_logging
from neutron.server import _init_configuration
from neutron.pecan_wsgi.startup import initialize_all


_init_configuration()
n_rpc.init(cfg.CONF)

objects.register_objects()
admin_ctx = context.get_admin_context()

logging.basicConfig(level=logging.DEBUG)
setup_logging()
#port_id = 'b434cfd4-16a3-41b4-92bf-68d6c090f4ef'
#port_obj = {
#    "port": {
#        "binding:host_id": "cmp003",
#        "device_id": "123123123",
#        "device_owner": "compute:cn-north-3",
#        "mac_address": " ac:de:48:76:06:5f"
#    }
#}

initialize_all()
plugin = directory.get_plugin('L3_ROUTER_NAT')
print plugin.list_router_ids_on_host(admin_ctx, 'cmp001')
#plugin.update_port(admin_ctx, port_id, port_obj)
#print plugin.get_l3_agents(admin_ctx, filters={'host': [None]})
#print plugin.get_hosts_to_notify(admin_ctx, 'f70929ae-67b5-4d70-b889-04732bfeb252')
#print plugin._get_other_dvr_router_ids_connected_router(admin_ctx, 'a0a391ea-0ae1-4ebf-b37c-b597b9e3fdb2')
#print plugin.get_dvr_routers_by_subnet_ids(admin_ctx, ['31a5fc6a-8bdf-4e8c-a2e8-e457254dd765'])
#print plugin._check_for_rtr_serviceable_ports(
#    admin_ctx,
#    'f70929ae-67b5-4d70-b889-04732bfeb252',
#    'cmp001'
#)
#
#agent = plugin._get_agent_by_type_and_host(
#    admin_ctx,
#    'L3 agent',
#    'cmp001'
#)
#print plugin._get_router_ids_for_agent(
#    admin_ctx,
#    agent,
#    ['d342bc23-4c9d-411f-9ad5-84591413fc9f']
#)
#
#print plugin._get_dvr_router_ids_for_host(
#    admin_ctx,
#    agent['host']
#)
