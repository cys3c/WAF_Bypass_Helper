# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.NORMAL




def tamper(payload, **kwargs):
    """
    >>> tamper("<IMG SRC="/x" onerror="javascript:alert('XSS');">")
<IMG SRC="/" onerror="jav&#x09;ascript:alert('XSS');">
    """
    result=[]
    string=re.sub(r"[\w]*",convert_this,str(payload))


    return (string) if payload else payload

def convert_this(string):
    new_word=[]
    string=string.group()
    length=len(string)
    if length>1:
        string=string[:length/2]+"&#x09;"+string[length/2:]
    return string
