from cinder import context
from cinder.volume import configuration
from oslo_utils import importutils


def init_driver(backend, host, db_driver):
    """inititialize a volume driver"""

    from cinder.volume.manager import volume_backend_opts

    config = configuration.Configuration(
        volume_backend_opts,
        config_group=backend
    )

    # import volume backend driver
    driver = importutils.import_object(
        config.volume_driver,
        configuration=config,
        db=db_driver,
        host=host,
        cluster_name=None,
        # assume db is not empty
        is_vol_db_empty=False,
        active_backend_id=None
    )

    # init backend driver
    ctx = context.get_admin_context()
    driver.do_setup(ctx)
    driver.check_for_setup_error()
    driver.init_capabilities()
    driver.set_initialized()

    return driver
