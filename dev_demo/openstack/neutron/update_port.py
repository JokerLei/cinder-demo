#!/usr/bin/env python

from oslo_config import cfg
from neutron_lib import context
from neutron.plugins.ml2.plugin import Ml2Plugin
from neutron.common import rpc as n_rpc
from neutron import manager


cfg.CONF(
    project='sjt-test-neutron',
    default_config_files=['neutron.conf']
)
n_rpc.init(cfg.CONF)
manager.init()

admin_ctx = context.get_admin_context()

port_id = ''
port_obj = {
    "port": {
        "device_id": "123123123",
        "device_owner": "compute:cn-north-3",
        "binding:host_id": "cmp088"
    }
}

ml2_instance = Ml2Plugin()
ml2_instance.update_port(admin_ctx, port_id, port_obj)
