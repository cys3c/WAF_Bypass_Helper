from main_modules.settings import PRIORITY
__priority__ = PRIORITY.LOWEST

def tamper(payload, **kwargs):
    """
    insert null byte before string

    >>> tamper("1 AND '1'='1")
    '%001 AND '1'='1'
    """
    return (payload+'%00') if payload else payload
