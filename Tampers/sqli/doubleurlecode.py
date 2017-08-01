import urllib

from main_modules.settings import PRIORITY
__priority__ = PRIORITY.LOW



def tamper(payload, **kwargs):
    """
    double url encode

    >>> tamper("1 AND '1'='1")
    %2527%2520union%2520select%2520password%2520from%2520mySQL.user%2520limit%25201%2520%252F*
    """
    return urllib.quote(urllib.quote(payload, safe=''), safe='') if payload else payload