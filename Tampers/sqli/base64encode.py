import base64

from main_modules.settings import PRIORITY, TYPE, STDPARAMS
__classificationtype__=TYPE.BackEND_SPECIFIED
__priority__ = PRIORITY.NORMAL


def tamper(payload, **kwargs):
    """
    Base64 all characters in a given payload

    >>> tamper("1' AND SLEEP(5)#")
    'MScgQU5EIFNMRUVQKDUpIw=='
    """

    return base64.b64encode(payload.encode(STDPARAMS.UNICODE_ENCODING)) if payload else payload
