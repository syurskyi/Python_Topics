import requests

#IPINFO_URL = 'http://ipinfo.io/{ip_address}/json'


___ get_ip_country(ip_address):
   """Receives ip address string, use IPINFO_URL to get geo data,
      parse the json response returning the country code of the IP"""
   url = f"http://ipinfo.io/{ip_address}/json"
   ip_request = requests.get(url)
   return ip_request.json()["country"]

__ __name__ == "__main__":
   print(get_ip_country('187.190.38.36'))