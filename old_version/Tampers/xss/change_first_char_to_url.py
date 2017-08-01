# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.NORMAL


def tamper(payload, **kwargs):
    """
    >>> 
    %55nion(%53elect) <- U=%55 S=%53
%55nion %53eLEct
    """
    
    string=re.sub(r"\w*",convert_this,payload)

    return (string) if payload else payload

def convert_this(string):
    
    string=string.group()
    if len(string)>0:
        string='%'+str(ord(string[0:1]))+string[1:]
    return string
