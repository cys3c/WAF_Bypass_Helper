# Encoding used for Unicode data
class STDPARAMS:
    UNICODE_ENCODING = "utf8"
    TAMPER = 'TAMPERS'
    SPEC = 'specified'

class BNSpecifiedTechink:
    url = 'urlencode'
    durl = 'double url encode'
    base64 = 'base64 encode'



class PRIORITY:
    LOWEST = -100
    LOWER = -50
    LOW = -10
    NORMAL = 0
    HIGH = 10
    HIGHER = 50
    HIGHEST = 100

class TYPE:
    SPECIFIED = -100
    UNIVERSAL = 100
    UNIVERSAL_NETWORK = 101
    BackEND_SPECIFIED = 0

class NETWORK:
    http_proxy  = "http://@127.0.0.1:8080"
    https_proxy = "https://@127.0.0.1:8080"
    user_agent="\'User-Agent\':\'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0\'"
    accept_language='\'Accept-Language\':\'en-US,en;q=0.5\''
    accept_encoding='\'Accept-Encoding\':\'gzip, deflate\''