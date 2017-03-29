import time
import logging

from oslo_concurrency import watchdog

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def short_task():
    time.sleep(1)

def long_task():
    time.sleep(10)

if __name__ == '__main__':
    LOG.info("start")
    with watchdog.watch(LOG, "short task is over 5 sec",
                        level=logging.INFO,
                        after=5):
        short_task()

    with watchdog.watch(LOG, "long task is over 5 sec",
                        level=logging.INFO,
                        after=5):
        long_task()
    LOG.info("end")
