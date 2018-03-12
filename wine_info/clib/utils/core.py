from __future__ import print_function

import os
import re
import string
import sys
from datetime import datetime, date, timedelta
from decimal import Decimal
from functools import wraps
from random import choice
from urlparse import urlsplit
from uuid import getnode
from pytz import timezone, utc

import user_agents
from dateutil.relativedelta import relativedelta
from flask import current_app, request

from .dicts import remove_prefix
from .formats import as_string


FIRST_CAP_RE = re.compile('(.)([A-Z][a-z]+)')
ALL_CAP_RE = re.compile('([a-z0-9])([A-Z])')


REDACT_LIST = ['credit_card_number', 'credit_card_cvv', 'password',
               'new_password', 'password_confirm']


_invalid_default = object()


def get_by_obj_path(obj, path, default=_invalid_default):
    """
    Return the result of traversing down an object by a path using dot notation.
        This also works with dictionary keys.
    """
    uses_default = default is not _invalid_default

    def _get_indifferent(sobj, attr_name):
        try:
            if isinstance(sobj, dict):
                return sobj[attr_name]
            return getattr(sobj, attr_name)
        except (KeyError, AttributeError):
            if uses_default:
                return default
            raise
    if '.' not in path:
        return _get_indifferent(obj, path)
    idx = path.index('.')
    attr = _get_indifferent(obj, path[:idx])

    return get_by_obj_path(attr, path[idx + 1:], default=default)


def get_config(prefix='', app=None):
    """
    Get a dict of configuration variables from an app
    with the given prefix.

    :param prefix: prefix of keys to search for
    :param app: app instance to use config from. If omitted, use current app
    """
    app = app or current_app
    return remove_prefix(app.config, prefix)


def get_request_id():
    """Returns a unique identifier for the current request"""
    try:
        return id(request._get_current_object())
    except:
        return 0


def at_least_21(given_date):
    """Is the given date at least 21 years ago?"""
    today = date.today()
    return today - relativedelta(years=21) >= given_date


def get_subdomain(url, server_name):
    """
    Get the subdomain of the given url from the server name.
    If the there is no subdomain or the server name is not
    in the url, return None.
    """
    if server_name not in url:
        return None

    host = urlsplit(url).netloc

    if host == server_name:
        return None

    return host.replace('.%s' % server_name, '')


def within_req_context(*req_args, **req_kwargs):
    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with current_app.test_request_context(*req_args, **req_kwargs):
                return func(*args, **kwargs)
        return wrapper
    return _decorator


def get_machine_uuid():
    """Get a unique string for this machine"""
    return as_string(getnode())


def random_string(length):
    """
    :param length: number of characters in generated string
    :return: a string of the given length with random letters and numbers
    """
    return ''.join(choice(string.ascii_uppercase + string.digits)
                    for x in range(length))


def discount_percent(original, discounted):
    """
    :param original: the original price or amount
    :param discounted: a discounted price or amount, less than original
    :return: the percent by which original is reduced to arrive at discounted
    """
    original = Decimal(original)
    discounted = Decimal(discounted)
    return ((original - discounted) / original) * 100


def delegate_properties(cls, obj_func, attrs, prefix=''):
    """Create properties that are delegated to another object

    Args:
        cls - Class to add properties to
        obj_func - Callable that returns object to forward to
        attrs - List of attributes on obj to delegate to
        prefix - Prefix properties on cls with this
    """
    def f(attr):
        return lambda self: getattr(obj_func(self), attr)
    for attr in attrs:
        prefixed_attr = "{0}{1}".format(prefix, attr)
        setattr(cls, prefixed_attr, property(f(attr)))


def email_from_contact(entry):
    if "<" in entry and ">" in entry:
        return entry[entry.rfind("<") + 1:entry.rfind(">")]
    return entry


# http://stackoverflow.com/questions/3203286/how-to-create-a-read-only-class-property-in-python
class classproperty(object):
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


def send(signal, **kwargs):
    """Send a message to a signal with the current app as the first argument"""
    signal.send(current_app._get_current_object(), **kwargs)


def as_called(f, *args, **kwargs):
    """Return a string representation of a function as called"""
    return "{0}({1})".format(f.__name__, format_args(*args, **kwargs))


def format_args(*args, **kwargs):
    """Return a string representation of the given args and kwargs"""
    arg_parts = [repr(arg) for arg in args]
    kw_parts = ['{0}={1}'.format(k, repr(v)) for k, v in kwargs.iteritems()]
    return ', '.join(arg_parts + kw_parts)


# http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
def get_terminal_size():
    """
    Get the size of the current terminal window

    :returns: dictionary with keys 'columns' and 'rows'
    """
    rows, columns = os.popen('stty size', 'r').read().split()
    return {'rows': int(rows), 'columns': int(columns)}


# http://stackoverflow.com/questions/18766535/positive-integer-from-python-hash-function
def positive_hash(obj):
    return hash(obj) % ((sys.maxsize + 1) * 2)


def pisinstance(p_object, class_or_type_or_tuple):
    """
    Test to see if an object or the underlying object of a
        werkzeug.local.LocalProxy is an instance of something
    :param p_object: object to test
    :param class_or_type_or_tuple: Object to test against as defined
        by isinstance
    :returns: bool of whether it is or it isn't
    """
    if hasattr(p_object, '_get_current_object'):
        p_object = p_object._get_current_object()
    return isinstance(p_object, class_or_type_or_tuple)


class Stopwatch(object):
    """Chainable stopwatch object"""
    def __init__(self):
        self.start_time = None
        self.end_time = None

    @property
    def current(self):
        if self.start_time is None:
            return timedelta(0)
        if self.end_time is None:
            return datetime.now() - self.start_time
        return self.end_time - self.start_time

    def start(self):
        if self.start_time is None:
            self.start_time = datetime.now()
        self.end_time = None
        return self

    def stop(self):
        self.end_time = datetime.now()
        return self

    def reset(self):
        self.start_time = None
        self.end_time = None
        return self


def plog(level, msg, newline=True):
    """
    Print and log info at the same time.
    """
    end = '\n' if newline else ''
    print(msg, end=end)
    current_app.logger.log(level, msg)


def redact(data):
    redacted = {}
    for k, v in data.items():
        if hasattr(v, 'items'):
            redacted[k] = redact(v)
        elif k in REDACT_LIST:
            redacted[k] = '[redacted]'
        else:
            redacted[k] = v
    return redacted


def to_utc(dt, tz=None):
    """
    Convert a datetime to UTC.

    :param dt: datetime to convert
    :param tz: timezone string to convert from

    :returns: Non-offset datetime in UTC
    """
    if tz is None:
        tz = get_config()['TIMEZONE']

    tzinfo = timezone(tz)
    local_dt = tzinfo.localize(dt)

    return dt - local_dt.utcoffset()


def from_utc(dt, tz=None):
    """
    Convert a datetime from UTC.

    :param dt: datetime to convert
    :param tz: timezone string to convert from. Use config timezone if
        not specified

    :returns: Non-offset datetime in tz
    """
    if tz is None:
        tz = get_config()['TIMEZONE']

    tzinfo = timezone(tz)
    return dt.replace(tzinfo=utc).astimezone(tzinfo).replace(tzinfo=None)


def get_device_type(user_agent_string):
    """
    Get the device type from the user agent string
    """
    if user_agent_string:
        user_agent = user_agents.parse(user_agent_string)
        if user_agent.is_mobile:
            return 'mobile'
        elif user_agent.is_tablet:
            return 'tablet'
        elif user_agent.is_pc:
            return 'desktop'
    return None
