from main_modules.settings import PRIORITY, TYPE
__priority__ = PRIORITY.LOWEST
__classificationtype__ = TYPE.BackEND_SPECIFIED

def tamper(payload, **kwargs):
    """
    

    >>> ../../../../../etc/passwd%0a.jpg 
    """
    return (payload+'%0a') if payload else payload
