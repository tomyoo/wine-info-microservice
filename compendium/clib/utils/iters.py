from itertools import groupby
from itertools import izip_longest, cycle, islice


def first(iterable):
    """Returns the first element of an iterable or None if it is empty"""
    try:
        return next(iter(iterable))
    except StopIteration:
        return None


def last(iterable):
    """Returns the first element of an iterable or None if it is empty"""
    l = list(iterable)
    if l:
        return l[-1]
    return None


def prefix_els(iterable, prefix):
    """
    Return a generator that add a prefix to elements returned by
    the given iterable.
    """
    return ('{0}{1}'.format(prefix, e) for e in iterable)

 
def flatten(iterable):
    """
    Return a generator that pulls out the first value of 1 elemement sequences
        from an iterable
    :param iterable: Iterable of 1 element sequences
    :return: Generator of the elements
    """
    return (el for (el,) in iterable)


class EmptyIterable(Exception):
    """A given iterable returns no results"""


def not_empty(iterable):
    """
    Returns a generator that raises an EmptyIterable exception if the iterable
    does not return any results.
    """
    empty = True
    for v in iterable:
        empty = False
        yield v
    if empty:
        raise EmptyIterable


def max_or_none(iterable, key=None):
    """
    Returns the max value in the iterable if it has any values that are
    not None else return None.
    """
    try:
        g = not_empty(v for v in iterable if v is not None)
        if key:
            return max(g, key=key)
        return max(g)
    except EmptyIterable:
        return None


def min_or_none(iterable, key=None):
    """
    Returns the min value in the iterable if it has any values that are
    not None else return None.
    """
    try:
        g = not_empty(v for v in iterable if v is not None)
        if key:
            return min(g, key=key)
        return min(g)
    except EmptyIterable:
        return None


# https://docs.python.org/2/library/itertools.html#recipes
def unique_justseen(iterable, key=None):
    """
    List unique elements, preserving order. Remember only the element just seen.

    :param iterable: source iterable
    :param key: key function to match elements by

    :returns: generator of unique elements

    >>> list(unique_justseen('AAAABBBCCDAABBB'))
    ['A', 'B', 'C', 'D', 'A', 'B']
    >>> list(unique_justseen('ABBCcAD', str.lower))
    ['A', 'B', 'C', 'A', 'D']
    """
    return (next(group) for _, group in groupby(iterable, key))


# https://docs.python.org/2/library/itertools.html
def grouper(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks or blocks

    :param iterable: Iterable to extract chunks for
    :param n: Size of the chunks
    :param fillvalue: Value to fill out slots in a chunk

    :returns: Iterable that returns tuples of n-size from the original iterable

    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    """
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


def parallel_batches(iterable, n, fillvalue=None):
    """
    Collect data into a given number of batches. This orders it so that the
        results of the iterable are distributed. Note that this is not lazy and
        could consume significant memory and will not work with infinite
        generators.

    :param iterable: Iterable to extract batches for
    :param n: Number of batches
    :param fillvalue: Value to fill out slots in a chunk

    :returns: Iterable that returns tuples of n-size from the original iterable

    parallel_batches('ABCDEFG', 3, 'x') --> ADG BEx CFx
    """
    groups = list(grouper(iterable, n))
    return grouper(roundrobin(*groups), len(groups), fillvalue=fillvalue)


# https://stackoverflow.com/a/8991553
def grouper_it(iterable, n):
    """
    Return generator of iterators of max size n from an initial iterable.

    :param iterable: iterable to break down
    :param n: max size
    :return: generator of iterators
    """
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, n))
        if not chunk:
            return
        yield chunk
