#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import collections
from time import time
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
from neutron.objects import ports as port_obj
from neutron_lib.api.definitions import portbindings
from neutron_lib.plugins import constants as plugin_constants

LOG = logging.getLogger(__name__)


def my_dvr_handle_new_service_port(
        l3_plugin,
        context,
        port,
        dest_host,
        unbound_migrate=False
):
    port_host = dest_host or port[portbindings.HOST_ID]
    l3_agent_on_host = (l3_plugin.get_l3_agents(
        context, filters={'host': [port_host]}) or [None])[0]
    if not l3_agent_on_host:
        return

    if dest_host:
        # Make sure we create the floatingip agent gateway port
        # for the destination node if fip is associated with this
        # fixed port
        l3plugin = directory.get_plugin(plugin_constants.L3)
        (
            l3plugin.
                check_for_fip_and_create_agent_gw_port_on_host_if_not_exists(
                context, port, dest_host))

    subnet_ids = [ip['subnet_id'] for ip in port['fixed_ips']]
    router_ids = l3_plugin.get_dvr_routers_by_subnet_ids(context, subnet_ids)
    if not router_ids:
        return
    agent_port_host_match = False
    if unbound_migrate:
        # This might be a case were it is migrating from unbound
        # to a bound port.
        # In that case please forward the notification to the
        # snat_nodes hosting the routers.
        # Make a call here to notify the snat nodes.
        snat_agent_list = l3_plugin.get_dvr_snat_agent_list(context)
        for agent in snat_agent_list:
            LOG.debug('DVR: Handle new unbound migration port, '
                      'host %(host)s, router_ids %(router_ids)s',
                      {'host': agent.host, 'router_ids': router_ids})
            l3_plugin.l3_rpc_notifier.routers_updated_on_host(
                context, router_ids, agent.host)
            if agent.host == port_host:
                agent_port_host_match = True
    if not agent_port_host_match:
        hosts = set([port_host])
        for router_id in router_ids:
            hosts |= set(l3_plugin.get_hosts_to_notify(context, router_id))

        host_routers = collections.defaultdict(set)
        for router_id in router_ids:
            # avoid calling get_ports in host loop
            subnet_ids = l3_plugin.get_subnet_ids_on_router(
                context.elevated(),
                router_id
            )
            for host in hosts:
                LOG.debug('DVR: Handle new service port, host %(host)s, '
                          'router ids %(router_id)s',
                          {'host': host, 'router_id': router_id})
                if l3_plugin._check_dvr_serviceable_ports_on_host(
                        context.elevated(),
                        host,
                        subnet_ids
                ):
                    host_routers[host].add(router_id)

        for host, router_ids in host_routers.items():
            l3_plugin.l3_rpc_notifier.routers_updated_on_host(
                context,
                router_ids,
                host
            )


_init_configuration()
n_rpc.init(cfg.CONF)

objects.register_objects()
admin_ctx = context.get_admin_context()

logging.basicConfig(level=logging.DEBUG)
setup_logging()
port_id = 'b434cfd4-16a3-41b4-92bf-68d6c090f4ef'

initialize_all()
l3_plugin = directory.get_plugin(lib_const.L3)
port = port_obj.Port.get_objects(
    admin_ctx,
    id=port_id
)

l3_plugin.dvr_handle_new_service_port(
    admin_ctx,
    port[0],
    dest_host='cmp003'
)

my_dvr_handle_new_service_port(
    l3_plugin,
    admin_ctx,
    port[0],
    dest_host='cmp089'
)

print port
