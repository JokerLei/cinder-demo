from cinder.common import constants as vol_constants
from cinder import context
from cinder import objects, rpc, coordination
from oslo_config import cfg
from oslo_log import log

from dev_demo.openstack.cinder import init_app

LOG = log.getLogger(__name__)


def register_opts():
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'volume_id',
            required=False
        )
    )
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'image_id',
            required=False,
            default=None
        )
    )
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'auth_token',
            required=False
        )
    )


if __name__ == '__main__':
    register_opts()
    backend, host, db_driver = init_app()
    if not rpc.initialized():
        rpc.init(cfg.CONF)
    #coordination.COORDINATOR.start()

    from cinder.volume.api import API

    ctx = context.get_admin_context()
    volume_api = API()
    vols = volume_api.get_all(
        ctx, filters={"all_tenants": True}
    )
    print(vols)
