_______ requests
_______ json

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


___ get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    w__ requests.Session() __ session:
        url_format = IPINFO_URL.f..(ip=ip_address)
        decode = session.get(url_format).content.decode('utf-8')
        data = json.loads(decode)
    r.. data['country']
