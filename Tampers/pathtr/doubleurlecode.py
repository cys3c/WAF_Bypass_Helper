import urllib

from main_modules.settings import PRIORITY, TYPE
__priority__ = PRIORITY.LOWEST
__classificationtype__ = TYPE.BackEND_SPECIFIED



def tamper(payload, **kwargs):
    """
    double url encode

    >>> tamper("1 AND '1'='1")
    %2527%2520union%2520select%2520password%2520from%2520mySQL.user%2520limit%25201%2520%252F*
    """
    payload=urllib.quote(urllib.quote(payload, safe=''), safe='')
    payload=payload.replace(".", "%252e").replace('\\', '%255c').replace('/', '%252f')
    return payload if payload else payload