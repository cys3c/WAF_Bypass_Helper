import urlparse


from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.UNIVERSAL_NETWORK
__priority__ = PRIORITY.NORMAL

def tamper(payload,url_for_atack, **kwargs):
    """

    >>> tamper('	
toAccount=9876&amount=1000&fromAccount=12345')
    '	
toAccount=9876&amount=1000&fromAccount=12345&toAccount=99999'
    """
    #SplitResult=urlparse.urlsplit(url_for_atack)
    
    return "payload" if payload else payload
