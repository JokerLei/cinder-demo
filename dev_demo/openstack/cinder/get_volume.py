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
    register_opts()
    init_app()

    volid = cfg.CONF.volume_id
    filters = {
        "id": volid
    }

    # demo usage of VolumeList
    ctx = context.get_admin_context()
    volume_list = objects.VolumeList.get_all(ctx, filters=filters)

    for v in volume_list:
        print(v.name)

    # demo Volume
    print objects.Volume.get_by_id(
        ctx, volid
    )
