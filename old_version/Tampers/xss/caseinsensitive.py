import re
from main_modules.settings import PRIORITY
__priority__ = PRIORITY.LOW

def tamper(payload, **kwargs):
    """
    change case

    >>> tamper("")
    '<IMG SRC=JaVaScRiPt:alert('XSS')>'
    """
    string=''
    for word in payload.split(' '):
        if re.search('\w',word):
            new_word=''
            #for letter in word:
            i=0
            while i<len(word):
                if i%2==0:
                    new_word=new_word+word[i].upper()
                else:
                    new_word=new_word+word[i].lower()
                i+=1
            string=string+' '+new_word
        else:
            string=string+' '+word
            


    return (string) if payload else payload
