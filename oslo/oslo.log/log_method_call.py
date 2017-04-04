import logging as symlog
from oslo_log import log as logging
from oslo_log import helpers as log_helpers

LOG = logging.getLogger(__name__)
symlog.basicConfig(level=symlog.DEBUG)

class MyClass(object):
    
    def __init__(self):
        pass
    
    @log_helpers.log_method_call
    def creat_port(self, *args, **kwargs):
        LOG.debug(args)
        pass

if __name__ == '__main__':
    obj = MyClass()
    obj.myfunc1(1, 2, 3, name="Kim")

