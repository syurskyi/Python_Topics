______ requests
______ json

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


___ get_ip_country(ip_address
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    with requests.Session() as session:
        url_format = IPINFO_URL.format(ip=ip_address)
        decode = session.get(url_format).content.decode('utf-8')
        data = json.loads(decode)
    r_ data['country']
