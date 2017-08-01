import re

from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.UNIVERSAL
__priority__ = PRIORITY.NORMAL

def tamper(payload, **kwargs):
    """

    change all spaces to tabs
    """
    result=[]
    result.append(re.sub(r"[\s+]",'&#x09;',payload))
    result.append(re.sub(r"[\s+]",'\t',payload))
    result.append(re.sub(r"[\s+]",'\v',payload))

# all string to comments(this out first brackets)
    if re.search('^\w',payload):
        result.append('/*!'+payload+'*/')
    elif re.search('\W',payload):
        i=0
        string=''
        while re.search('\W',payload[i]):
            string=string+payload[i]
            i+=1
        string=string+'/*!'+payload[i:]+'*/'
        result.append(string)
        

# all words to comments
    string=re.sub(r"\w*",convert_this,str(payload))
    result.append(string)


    return result if payload else payload

def convert_this(string):
    string=string.group()
    string='/*!'+string+'*/'
    return string
