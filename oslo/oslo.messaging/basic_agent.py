#!/usr/bin/env python

# coding: utf-8
import socket

import logging as symlog
from oslo_log import log as logging
from oslo_log import helpers as log_helpers
from oslo_config import cfg
import oslo_messaging

import eventlet

eventlet.monkey_patch()

LOG = logging.getLogger(__name__)
symlog.basicConfig(level=symlog.INFO)

class RpcCallHandler(object):
    def func1(self, ctxt, **kwargs):
        LOG.info("called RpcCallHandler.func1 - %s", kwargs)
        return True

transport_url = 'rabbit://gjxdknsw:6Eiq5MPMvrfhbJVvZCrktF4N5NdE7xHg@sidewinder.rmq.cloudamqp.com:5672/gjxdknsw'
transport = oslo_messaging.get_transport(cfg.CONF, transport_url)

target = oslo_messaging.Target(exchange="basic", topic='basic_agent',
                               server=socket.gethostname())
endpoints = [RpcCallHandler()]
server = oslo_messaging.get_rpc_server(
    transport, target, endpoints, executor='eventlet')

LOG.info('server starts')
server.start()

LOG.info('server consuming...')
server.wait()
