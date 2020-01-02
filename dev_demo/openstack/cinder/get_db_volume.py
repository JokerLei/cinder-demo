from cinder import db
from cinder import objects
from cinder import context
from oslo_config import cfg

from dev_demo.openstack.cinder \
    import init_app


def register_opts():
    cfg.CONF.register_cli_opt(
        cfg.StrOpt(
            'volume_id',
            required=True
        )
    )


if __name__ == '__main__':
    # register a new cli opt
    init_app()

    # demo usage of VolumeList
    ctx = context.get_admin_context()
    volumes = db.volume_get_all(ctx, None, None,
                                sort_keys=None, sort_dirs=None,
                                filters=None, offset=None)

    for vol in volumes:
        print(vol.get('volume_attachment'))
