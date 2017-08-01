from main_modules.settings import PRIORITY, TYPE
__priority__ = PRIORITY.LOWEST
__classificationtype__ = TYPE.BackEND_SPECIFIED

def tamper(payload, **kwargs):
    """
    

    >>> ../../../../../etc/passwd/.
    """
    return (payload+'/.') if payload else payload
