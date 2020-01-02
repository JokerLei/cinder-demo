from cinder.common import constants as vol_constants
from cinder import objects
from cinder import context
from cinder.db.sqlalchemy import api, models
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


if __name__ == '__main__':
    register_opts()
    backend, host, db_driver = init_app()

    ctx = context.get_admin_context()
    volume_obj = objects.Volume.get_by_id(
        ctx, cfg.CONF.volume_id
    )
    session = api.get_session()
    with session.begin():
        rows = session.query(models.VolumeGlanceMetadata) \
            .filter_by(volume_id=volume_obj.id).delete()

