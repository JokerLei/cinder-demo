from oslo_messaging.rpc.transport import get_rpc_transport
from oslo_config import cfg

CONF = cfg.CONF
CONF(project='sjt-test', default_config_files=[r'E:\Inspur\dev-demo\etc\test.conf'])
transport = get_rpc_transport(CONF)
