#!/usr/bin/env python

from cinder import objects, context
from oslo_log import log
from oslo_config import cfg

from dev_demo.openstack.cinder.driver \
    import init_driver
from dev_demo.openstack.cinder \
    import init_app

LOG = log.getLogger(__name__)


def register_opts():
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            "volume_id",
            required=True
        )
    )

    cfg.CONF.register_cli_opt(
        cfg.BoolOpt(
            "create",
            default=False
        )
    )


def get_volume_by_id(volid):
    ctx = context.get_admin_context()
    volume = objects.Volume.get_by_id(ctx, volid)
    return volume


def delete_volume(vol_driver, volid):
    try:
        volume = get_volume_by_id(volid)
        vol_driver.delete_volume(volume)
    except Exception:
        LOG.exception("delete volume failed")


def create_volume(vol_driver, volid):
    try:
        volume = get_volume_by_id(volid)
        vol_driver.create_volume(volume)
    except Exception:
        LOG.exception('create volume failed')


if __name__ == '__main__':
    """start executing"""

    register_opts()
    backend, host, db_driver = init_app()
    vol_driver = init_driver(backend, host, db_driver)
    if not cfg.CONF.create:
        delete_volume(vol_driver, cfg.CONF.volume_id)
    else:
        create_volume(vol_driver, cfg.CONF.volume_id)
