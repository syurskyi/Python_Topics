_______ r__

#IPINFO_URL = 'http://ipinfo.io/{ip_address}/json'


___ get_ip_country(ip_address
   """Receives ip address string, use IPINFO_URL to get geo data,
      parse the json response returning the country code of the IP"""
   url = f"http://ipinfo.io/{ip_address}/json"
   ip_request = r__.g.. url)
   r.. ip_request.j..["country"]

__ _______ __ _______
   print(get_ip_country('187.190.38.36'