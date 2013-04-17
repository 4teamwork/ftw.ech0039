import re


def as_normalized_string(text):
    """Convert text to a normalized string as defined in:
    http://www.w3.org/TR/xmlschema-2/#normalizedString

    Normalized strings can't contain carriage returns, linefeeds, or tabs.

    """
    return re.sub(ur"[\r\n\t]", u' ', text, flags=re.UNICODE)


def as_token(text):
    """Convert text to a token as defined in:
    http://www.w3.org/TR/xmlschema-2/#token

    Tokens can't contain leading or trailing whitespace characters nor any
    occurrence of two or more consecutive space characters nor carriage
    returns, linefeeds, or tabs.

    """
    return as_normalized_string(text.strip().replace(u'  ', u' '))
