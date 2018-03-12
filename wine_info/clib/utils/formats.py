import re
import string
from datetime import time, datetime
from decimal import Decimal, ROUND_HALF_DOWN, ROUND_DOWN

import arrow
from unidecode import unidecode


WORD_CHARS = string.letters + string.digits


def format_decimal(value, places=0):
    """Formats a decimal to a given number of places
    Args:
        value - original decimal value to format
    Keyword Args:
        places - number of places to display. Defaults to 0

    Returns:
        decimal quantized to ```places``` places.
    """
    return Decimal(value).quantize(Decimal(10) ** -places)


def money(v):
    return format_decimal(v, 2)


def as_string(i, chars=WORD_CHARS):
    """
    Converts an integer to a string representation
    :param i: integer to convert
    :param chars: characters to choose from
    """
    char_len = len(chars)
    if i == 0:
        return ''
    else:
        return chars[i % char_len] + as_string(i / char_len, chars)


def slugify(s):
    """Converts the given string into a suitable slug"""
    s = unidecode(unicode(s)).lower()
    return re.sub("[^\w\-\_]", "", re.sub("\s+?", "-", s.lower()))


def format_phone(s):
    """
    Formats a string containing digits as a U.S. phone number. Any numbers
    after the first 10 (11 if there is a leading 1) are considered extension
    numbers. If the number is shorter than 10 (11 with leading 1) digits,
    return the original string.
    """
    if not s:
        return s
    s = re.sub('[^0-9]', '', s)
    if not s or (len(s) < 10) or (s[0] == '1' and len(s) < 11):
        return s
    if s[0] == u'1':
        result = u'1 '
        s = s[1:]
    else:
        result = ''

    result += u'({0}) {1}-{2}'.format(s[0:3], s[3:6], s[6:10])

    if len(s) > 10:
        result += u' x{0}'.format(s[10:])

    return result


def to_datetime(dt):
    """Convert a date to a datetime"""
    return datetime.combine(dt, time())


def to_date(dt):
    """Converts a datetime to a date (or returns itself if already a date"""
    if hasattr(dt, 'date'):
        return dt.date()
    return dt


def to_closest(v, closest=Decimal("1"), precision=Decimal("1"),
               rounding=ROUND_HALF_DOWN):
    """Rounds number to the closest value with a given precision on
    step closest"""
    val = Decimal(v).quantize(precision)
    return (val / closest).quantize(precision, rounding) * closest


def format_percent(percent, closest=Decimal('5'), precision=Decimal('1')):
    return to_closest(percent, closest=closest, precision=precision,
                      rounding=ROUND_DOWN)


# http://dzone.com/snippets/convert-integer-english
def english_number(val):
    """Return an english representation of a number"""
    to_19 = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
             'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
    tens = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
            'eighty', 'ninety')
    denom = ('', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
             'quintillion', 'sextillion', 'septillion', 'octillion',
             'nonillion', 'decillion', 'undecillion', 'duodecillion',
             'tredecillion', 'quattuordecillion', 'sexdecillion',
             'septendecillion', 'octodecillion', 'novemdecillion',
             'vigintillion')

    def _convert_nn(val):
        """convert a value < 100 to English."""
        if val < 20:
            return to_19[val]
        for (dcap, dval) in ((k, 20 + (10 * v)) for (v, k) in enumerate(tens)):
            if dval + 10 > val:
                if val % 10:
                    return dcap + '-' + to_19[val % 10]
                return dcap

    def _convert_nnn(val):
        """convert a value < 1000 to english, special cased because it is the
        level that kicks off the < 100 special case.  The rest are more general.
        This also allows you to get strings in the form of 'forty-five hundred'
        if called directly."""
        word = ''
        (mod, rem) = (val % 100, val // 100)
        if rem > 0:
            word = to_19[rem] + ' hundred'
            if mod > 0:
                word += ' '
        if mod > 0:
            word += _convert_nn(mod)
        return word

    if val < 100:
        return _convert_nn(val)
    if val < 1000:
        return _convert_nnn(val)
    for (didx, dval) in ((v - 1, 1000 ** v) for v in range(len(denom))):
        if dval > val:
            mod = 1000 ** didx
            l = val // mod
            r = val - (l * mod)
            ret = _convert_nnn(l) + ' ' + denom[didx]
            if r > 0:
                ret = ret + ', ' + english_number(r)
            return ret


def format_date_range(start, end):
    start_ = arrow.get(start)
    end_ = arrow.get(end)

    if start_ == end_:
        return start_.format("MMMM Do")
    elif start_.month == end_.month:
        return "{} - {}".format(start_.format("MMMM Do"), end_.format("Do"))
    else:
        return "{} - {}".format(start_.format("MMMM Do"),
                                end_.format("MMMM Do"))
