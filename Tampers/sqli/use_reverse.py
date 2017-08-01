import re
from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.BackEND_SPECIFIED
__priority__ = PRIORITY.HIGH

def tamper(payload, **kwargs):
    """
    REVERSE(noinu)+REVERSE(tceles)

    >>> tamper("selet")
    'REVERSE(tceles)'
    """
    string=''
    for word in payload.split(' '):
        if re.search(r'^\w+',word) and len(word)>2 and re.search(r'\d',word) is None:
            word=list(word)
            word.reverse()
            word=''.join(word)
            new_word='REVERSE('+word+')'
            string=string+' '+new_word
        else:
            string=string+' '+word
            


    return (string) if payload else payload

if __name__ == "__main__":      
    print tamper('select 1,2,3 from base_name')
