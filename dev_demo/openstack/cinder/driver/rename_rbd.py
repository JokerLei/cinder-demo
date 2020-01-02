from cinder import objects
from cinder import context
from cinder.volume.drivers.rbd import RADOSClient
from oslo_config import cfg
from oslo_log import log

from dev_demo.openstack.cinder \
    import init_app
from dev_demo.openstack.cinder.driver \
    import init_driver

LOG = log.getLogger(__name__)


def register_opts():
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'volume_id',
            required=True
        )
    )

    cfg.CONF.register_opt(
        cfg.StrOpt(
            'demo_name_template',
            default="%s-demo-volume"
        )
    )


def rename_backend_volume(vol_driver, volume):
    """demo how to rename backend volume"""

    try:
        src_name = volume.name
        with RADOSClient(vol_driver) as client:
            vol_driver.RBDProxy().rename(
                client.ioctx,
                src_name,
                cfg.CONF.demo_name_template % src_name
            )
    except Exception:
        LOG.exception("rename rbd failed")


if __name__ == '__main__':
    # register a new cli opt
    register_opts()
    init_params = init_app()

    volid = cfg.CONF.volume_id
    ctx = context.get_admin_context()
    volume = objects.Volume.get_by_id(
        ctx, cfg.CONF.volume_id
    )

    # rename a backend volume
    vol_driver = init_driver(*init_params)
    rename_backend_volume(
        vol_driver, volume
    )
