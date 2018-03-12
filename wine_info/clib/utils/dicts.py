def merge(*args):
    """Merge a bunch of dictionaries into one and return the result. Note
    that in cases of key collisions, the value for that key will be whatever
    it was set to last in order of the argument list."""
    output = {}
    for d in args:
        output.update(d)
    return output


def add_prefix(d, prefix, keys=None):
    """
    Returns a dictionary with keys prepended with the given prefix

    :param d: dictionary to search
    :param prefix: prefix to add to keys
    :param keys: keys on which to add the prefix. If omitted, prefix all
        of the keys.
    """
    if not keys:
        keys = set(d.keys())
    else:
        keys = set(keys)

    def add_prefix_if(k):
        return '{0}{1}'.format(prefix, k) if k in keys else k

    return dict((add_prefix_if(k), v)
                for k, v in d.iteritems())


def add_suffix(d, suffix, keys=None):
    """
    Returns a dictionary with keys appended with the given suffix

    :param d: dictionary to search
    :param suffix: suffix to add to keys
    :param keys: keys on which to add the suffix. If omitted, suffix all
        of the keys.
    """
    if not keys:
        keys = set(d.keys())
    else:
        keys = set(keys)

    def add_suffix_if(k):
        return '{0}{1}'.format(k, suffix) if k in keys else k

    return dict((add_suffix_if(k), v)
                for k, v in d.iteritems())


def remove_prefix(d, prefix):
    """
    Returns dictionary with keys matching the given prefix and the prefix
    removed from those keys

    :param d: dictionary to search
    :param prefix: keys in result must have this prefix and will have this
        removed
    """
    return dict((k.replace(prefix, ''), v)
                for k, v in d.iteritems()
                if k.startswith(prefix))


def prefix_values(d, keys, prefix):
    """
    Prefix values in d if the key is in keys.
    If the prefix is falsy, do nothing.
    """
    d = d.copy()
    if prefix:
        for key in keys:
            if key in d:
                d[key] = '{0}{1}'.format(prefix, d[key])
    return d


def invert(d):
    """
    Remaps dictionary from (key, value) to (value, key).

    Note that if the same value exists for multiple keys, it will only appear
    once in the result.
    """
    return dict((v, k) for k, v in d.iteritems())


def remap(d, mapping):
    """
    Remaps a dictionary / pair iterable according to mapping.

    :param d: dictionary or iterable of pairs (e.g. a list of 2-tuples)
    :param mapping: dictionary of keys in d to the new keys in the
        remapped dictionary
    """
    items = d.iteritems() if hasattr(d, 'iteritems') else d
    return {mapping[k]: v for k, v in items if k in mapping}


class MappedDictionary(dict):
    """
    Dictionary-like object that maps the incoming arguments according
    to the static method remap which must be implemented.
    """
    @classmethod
    def remap(cls, original):
        """Return remapped version of request"""
        raise NotImplementedError

    def __init__(self, original):
        remapped = self.remap(original)
        dict.__init__(self, remapped)
        self.original = (original)


def filter_keys(d, keys):
    """
    Filter a dictionary so that it only includes the given keys
    """
    keys = set(keys)
    return {k: v for k, v in d.iteritems() if k in keys}


def redact_keys(d, keys):
    """
    Returns a new dictionary with the given keys removed

    Note that the new dictionary is a shallow copy of the original
    """
    keys = set(keys)
    return dict([(k, v) for k, v in d.iteritems() if k not in keys])


def unpack_values(d, keys):
    """
    Unpack a dictionary-like object using the following rules:

    It is useful for unpacking dictionaries as so
    d = {'foo': 'bar', 'spam': 'eggs'}
    foo, spam = unpack_values(d, ('foo', 'spam'))
    """
    return tuple(d.get(key) for key in keys)


def overlay(*args):
    """
    Similar to ```merge()``` except that keys that have a dict values are merged
    rather than replaced.
    """
    def _overlay(a, b):
        c = {k: _overlay(v, b[k]) for k, v in a.iteritems()
             if k in b and isinstance(v, dict) and isinstance(b[k], dict)}
        return merge(a, b, c)

    return reduce(_overlay, args)
