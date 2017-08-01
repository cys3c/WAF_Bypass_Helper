# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.HIGHEST



def tamper(payload, **kwargs):
    """
   

    >>> tamper("<IMG SRC="/" onerror=javascript:alert('XSS')>")
<IMG SRC="/" onerror=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>

    """
    string=re.sub(r"(?<=[=:])[\S]*(?=[;<>\s/\\])",convert_this,str(payload))

    return (string) if payload else payload

def convert_this(string):
    string=string.group()
    new_word="&#x"+"&#x".join("{:07x}".format(ord(c)) for c in string)
    return new_word

