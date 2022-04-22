from collections import namedtuple

from prometheus_client import start_http_server, Gauge

import random
import time

from packages import checkupdates
from apscheduler.schedulers.blocking import BlockingScheduler

#print(packages.checkupdates())

Options = namedtuple('Options', ['security_updates_unattended', 'show_package_names', 'readable_output'])


scheduler = BlockingScheduler()

NUM_UPDATES = Gauge('prom_packages_updates', 'Number of available apt updates')
NUM_SECURITY_UPDATES = Gauge('prom_packages_security_updates', 'Number of available apt security updates')


def check_apt():
    (num_updates, num_security_updates) = checkupdates()
    NUM_UPDATES.set(num_updates)
    NUM_SECURITY_UPDATES.set(num_security_updates)


def run_app():
    check_apt()

    # Start up the server to expose the metrics.
    start_http_server(8000)

    scheduler.add_job(check_apt, 'interval', hours=1)
    scheduler.start()