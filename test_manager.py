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
            required=True
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
            required=True
        )
    )


if __name__ == '__main__':
    register_opts()
    backend, host, db_driver = init_app()
    if not rpc.initialized():
        rpc.init(cfg.CONF)
    coordination.COORDINATOR.start()

    from cinder.volume.manager import VolumeManager

    manager = VolumeManager(
        host=host,
        cluster=None,
        service_name=backend
    )
    ctx = context.get_admin_context()
    ctx.auth_token = cfg.CONF.auth_token
    manager.init_host(
        added_to_cluster=False,
        service_id=objects.Service.get_by_args(
            ctx, host, vol_constants.VOLUME_BINARY
        ).id
    )
    volume_obj = objects.Volume.get_by_id(
        ctx, cfg.CONF.volume_id
    )
    specs = {
        "image_id": cfg.CONF.image_id
    }
    request_spec = objects.RequestSpec(
        **specs
    )
    manager.create_volume(
        ctx,
        volume_obj,
        request_spec
    )
