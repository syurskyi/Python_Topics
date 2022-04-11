_______ r__
_______ j__

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


___ get_ip_country(ip_address
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    w__ r__.S.. __ session:
        url_format = IPINFO_URL.f..(ip=ip_address)
        decode = session.g.. url_format).content.d.. 'utf-8')
        data = j__.l.. (decode)
    r.. data 'country'
