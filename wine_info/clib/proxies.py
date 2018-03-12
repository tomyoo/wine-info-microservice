"""
Proxies to common Flask extensions
"""
from werkzeug.local import LocalProxy
from flask import current_app


current_logger = LocalProxy(lambda: current_app.logger)

statsd = LocalProxy(lambda: current_app.extensions['statsd'])

__all__ = ['statsd', 'current_logger']
