#!/user/bin/env python

from oslo_config import cfg
from keystone.server import common
import sys


def register_opts(conf):
    conf.register_cli_opt(
        cfg.StrOpt(
            "project_id"
        )
    )
    conf.register_cli_opt(
        cfg.StrOpt(
            "project_name"
        )
    )


if __name__ == '__main__':
    common.configure(config_files=[])
