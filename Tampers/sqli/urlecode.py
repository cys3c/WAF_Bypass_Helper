from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.BackEND_SPECIFIED
__priority__ = PRIORITY.LOW


import urllib




def tamper(payload, **kwargs):
    """
    double url encode

    >>> tamper("1 AND '1'='1")
    %2527%2520union%2520select%2520password%2520from%2520mySQL.user%2520limit%25201%2520%252F*
    """
    return urllib.quote(payload, safe='') if payload else payload