import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.LOW

def tamper(payload, **kwargs):
    """
    onvert to char()

    =char(100,118,119,97)
char(0x##)+char(0x##)+... if we can use only one character

    >>> tamper("selet")
    'SeLeT'

    CHAR(83, 101, 76, 101, 84) mysql 
 CHAR(83) + CHAR(101) + CHAR(76) + CHAR(101) + CHAR(84) mssql
  CHR(115) || CHR(101) || CHR(108) || CHR(101) || CHR(99) || CHR(116) oracle
    """
            
    string=re.sub(r"\w*",convert_this,str(payload))

    return (string) if payload else payload

def convert_this(string):
    new_word=[]
    string=string.group()
    new_word=" || ".join("Char("+str("{:07x}".format(ord(c))+')') for c in string)
    return new_word