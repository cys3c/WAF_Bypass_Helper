import re,random

from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.BackEND_SPECIFIED
__priority__ = PRIORITY.LOWER

def tamper(payload, **kwargs):
    """
    ad keyword splitt

    >>> tamper("selet")
    'Se<LeT'
    """
    string=re.sub(r"\w*",convert_this,payload)
    
    return (string) if payload else payload

def convert_this(string):
    
    string=string.group()
    if len(string)>1:
        split_point=random.randint(1,len(string)-1)
        string=string[:split_point]+'<'+string[split_point:]
    return string
