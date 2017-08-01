
from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.UNIVERSAL
__priority__ = PRIORITY.LOW

def tamper(payload, **kwargs):
    """
    Appends encoded NULL byte character at the end of payload

    Requirement:
        * Microsoft Access

    Notes:
        * Useful to bypass weak web application firewalls when the back-end
          database management system is Microsoft Access - further uses are
          also possible

    Reference: http://projects.webappsec.org/w/page/13246949/Null-Byte-Injection

    >>> tamper('1 AND 1=1')
    '1 AND 1=1%00'
    """

    return "%s%%00" % payload if payload else payload
