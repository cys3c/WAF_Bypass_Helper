import re
import sys
from main_modules.settings import PRIORITY, TYPE
__priority__ = PRIORITY.LOWEST
__classificationtype__ = TYPE.BackEND_SPECIFIED

def tamper(payload, **kwargs):
    """
    

    >>> /etc/passwd 
    /./etc/./passwd 
    
    """
    repeat_el='./'
    re.sub(r'/{1}(?!\\)','/./',payload)
    #re.sub(r'\\{1}(?!/)','\\.\\',payload)




    return (payload) if payload else payload
