#!/usr/bin/env python

from oslo_config import cfg
from neutron_lib import context
from neutron.plugins.ml2.plugin import Ml2Plugin
from neutron.common import rpc as n_rpc
from neutron import manager
from neutron_lib.callbacks import registry
from neutron_lib.callbacks import resources
from neutron_lib.callbacks import events
import eventlet

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


def custom_callback(*args, **kwargs):
    print args, kwargs


registry.subscribe(custom_callback, resources.PORT, events.AFTER_UPDATE)

while True:
    eventlet.sleep()
