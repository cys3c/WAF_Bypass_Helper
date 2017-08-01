from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.UNIVERSAL
__priority__ = PRIORITY.LOWEST

def tamper(payload, **kwargs):
    """
    insert null byte before string

    >>> tamper("1 AND '1'='1")
    '%001 AND '1'='1'
    """
    return ('%00 '+payload) if payload else payload
