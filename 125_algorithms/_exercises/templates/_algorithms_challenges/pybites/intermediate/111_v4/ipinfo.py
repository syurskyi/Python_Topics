import requests


IPINFO_URL = 'http://ipinfo.io/{ip}/json'


___ get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    resp = requests.get(url=IPINFO_URL.format(ip=ip_address))
    return resp.json()['country']
