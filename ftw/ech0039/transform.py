from DateTime.interfaces import IDateTime
from Products.CMFPlone.utils import safe_unicode
from pyxb.binding import datatypes as xs
import re
from ftw.ech0039.bind import BIND


def as_normalized_string(text):
    """Convert text to a normalized string as defined in:
    http://www.w3.org/TR/xmlschema-2/#normalizedString

    Normalized strings can't contain carriage returns, linefeeds, or tabs.

    """
    text = safe_unicode(text)
    return re.sub(ur"[\r\n\t]", u' ', text, flags=re.UNICODE)


def as_token(text):
    """Convert text to a token as defined in:
    http://www.w3.org/TR/xmlschema-2/#token

    Tokens can't contain leading or trailing whitespace characters nor any
    occurrence of two or more consecutive space characters nor carriage
    returns, linefeeds, or tabs.

    """
    normalized_string = as_normalized_string(text)
    return normalized_string.strip().replace(u'  ', u' ')


def as_tokens(iterable):
    """Convert an iterable to bound ech0039 tokens.

    """
    return BIND(*[as_token(each) for each in iterable])


def as_date(date):
    """Convert a either date (or datetime) or a DateTime object to an
    xs.date object.

    """

    if IDateTime.providedBy(date):
        return xs.date(date.year(), date.month(), date.day())
    return xs.date(date.year, date.month, date.day)
