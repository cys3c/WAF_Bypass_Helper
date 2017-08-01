import urllib

from main_modules.settings import PRIORITY, TYPE
__priority__ = PRIORITY.LOWEST
__classificationtype__ = TYPE.BackEND_SPECIFIED



def tamper(payload, **kwargs):
    """
    

    >>> ....//

    ....\/

    ..../\

    ....\\
    """
    return payload.replace("\\", "\\/") if payload else payload