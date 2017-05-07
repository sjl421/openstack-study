#!/usr/bin/env python

# coding: utf-8
import socket
import logging as symlog
from oslo_log import log as logging
from oslo_log import helpers as log_helpers
from oslo_config import cfg
import oslo_messaging

LOG = logging.getLogger(__name__)
symlog.basicConfig(level=symlog.INFO)

transport_url = 'rabbit://gjxdknsw:6Eiq5MPMvrfhbJVvZCrktF4N5NdE7xHg@sidewinder.rmq.cloudamqp.com:5672/gjxdknsw'
transport = oslo_messaging.get_transport(cfg.CONF, transport_url)

target = oslo_messaging.Target(
    exchange="basic", topic="basic_agent",
    server=socket.gethostname())
client = oslo_messaging.RPCClient(transport, target)

LOG.info(client.prepare(fanout=False).call({}, "func1", mtype="call"))
LOG.info(client.prepare(fanout=False).cast({}, "func1", mtype="cast"))
