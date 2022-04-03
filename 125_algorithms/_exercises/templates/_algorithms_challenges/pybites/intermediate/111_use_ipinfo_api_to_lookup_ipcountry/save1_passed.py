_______ r__

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


___ get_ip_country(ip_address
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    response = r__.g.. IPINFO_URL, ip_address)
    r.. response.j...g.. 'country')