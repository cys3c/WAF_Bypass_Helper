from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.UNIVERSAL
__priority__ = PRIORITY.LOW


def tamper(payload, **kwargs):
    """
    Replaces apostrophe character with its illegal double unicode counterpart

    >>> tamper("1 AND '1'='1")
    '1 AND %00%271%00%27=%00%271'
    """

    return payload.replace('\'', "%00%27") if payload else payload
