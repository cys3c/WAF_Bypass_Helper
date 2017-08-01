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

    return result if payload else payload

