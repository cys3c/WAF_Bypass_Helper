#!/usr/bin/env python

from main_modules.settings import PRIORITY, TYPE
__priority__ = PRIORITY.LOWEST
__classificationtype__ = TYPE.BackEND_SPECIFIED

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    

    >>> 
    dot                           %u002e

    forward slash          %u2215

    backslash                %u2216
    """

    return payload.replace(".", "%e0%40%ae").replace('\\', '%c0%80%5c').replace('/', '%e0%80%af')
