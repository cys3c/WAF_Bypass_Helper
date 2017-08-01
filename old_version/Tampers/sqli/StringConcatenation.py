import re,random

from main_modules.settings import PRIORITY
__priority__ = PRIORITY.HIGHEST

def tamper(payload, **kwargs):
    """
    EXEC('SEL' + 'ECT 1')

    >>> tamper("selet 1")
    'EXEC('SEL' + 'ECT 1')'
    """
    string=''
    string=re.sub(r'[a-z]*',convert_this,str(payload),flags=re.IGNORECASE)
         


    return (string) if payload else payload

def convert_this(string):
    string=string.group()
    length=len(string)
    if length>1:
        string='EXEC('+string[:length/2]+'\' + \''+string[length/2:]+')'
    return string