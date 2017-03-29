import sys
from oslo_config import cfg
from oslo_log import log as logging

LOG = logging.getLogger(__name__)

group = cfg.OptGroup(name='simple',
                     title='A Simple Example')

opts = [
    cfg.StrOpt('enable', default="False",
               help=('True enables, False disables'))
]

CONF = cfg.CONF
CONF.register_group(group)
CONF.register_cli_opts(opts, group)

logging.register_options(CONF)
logging.setup(CONF, "simple")

if __name__ == "__main__":
    CONF(sys.argv[1:])
    print(CONF.simple.enable)
    LOG.info("hello")
