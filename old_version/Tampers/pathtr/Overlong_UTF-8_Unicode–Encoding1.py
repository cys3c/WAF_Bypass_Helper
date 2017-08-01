#!/usr/bin/env python
from main_modules.settings import PRIORITY, TYPE
__priority__ = PRIORITY.LOWEST
__classificationtype__ = TYPE.BackEND_SPECIFIED


from main_modules.settings import PRIORITY
__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    

    >>> 
    dot                           %u002e

    forward slash          %u2215

    backslash                %u2216
    """

    return payload.replace(".", "%c0%2e").replace('\\', '%c0%5c').replace('/', '%c0%af')
