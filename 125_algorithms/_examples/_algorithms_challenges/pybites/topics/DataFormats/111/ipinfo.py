import requests

#IPINFO_URL = 'http://ipinfo.io/{ip}/json'
IPINFO_URL = 'http://ipinfo.io/210.195.171.202/json'


def get_ip_country(ip_address):
   new_url = IPINFO_URL.replace('{ip}',ip_address)
   resp = requests.get(url=new_url)
   data = resp.json()
   return data['country']


get_ip_country('210.195.171.202')