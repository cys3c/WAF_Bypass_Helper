import re,random


from main_modules.settings import PRIORITY
__priority__ = PRIORITY.NORMAL


def tamper(payload, **kwargs):
    """
    substring() -> mid(), substr(), etc
    ascii() -> hex(), bin(), etc
    benchmark() -> sleep()
    """
    string=''
    array_sybstring=['substring','mid','substr']

    for word in payload.split(' '):
        if re.search(r'^\w+',word) and len(word)>2 and re.search(r'\d',word) is None:
            new_word=''

            string=string+' '+new_word
        else:
            string=string+' '+word
            

    string = ' no idea ((( need to do'
    return (string) if payload else payload