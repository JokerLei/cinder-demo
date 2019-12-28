import sys

from cinder import objects
from cinder import version
from cinder.db import base
from cinder.cmd.volume import host_opt
from oslo_config import cfg
from oslo_utils import importutils


def init_app():
    """initialize application"""

    objects.register_all()
    cfg.CONF(
        sys.argv[1:],
        project='cinder',
        version=version.version_string()
    )

    # choose the first in backend list
    backend = cfg.CONF.enabled_backends[0]
    cfg.CONF.register_opt(
        host_opt,
        backend
    )

    # get backend host
    backend_host = getattr(
        cfg.CONF,
        backend
    ).backend_host

    if not backend_host:
        print("please add a backend host")
        sys.exit(1)

    # form a host
    host = "%s@%s" % (
        backend_host,
        backend
    )

    # import and initialize db driver module
    db_driver = importutils.import_module(cfg.CONF.db_driver)
    db_driver.dispose_engine()

    return (
        backend, host, db_driver
    )
