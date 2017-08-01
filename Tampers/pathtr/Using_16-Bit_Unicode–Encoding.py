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

    return payload.replace(".", "%u002e").replace('\\', '%u2216').replace('/', '%u2215')
