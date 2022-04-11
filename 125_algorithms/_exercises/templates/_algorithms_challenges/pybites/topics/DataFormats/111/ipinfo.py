_______ r__

#IPINFO_URL = 'http://ipinfo.io/{ip}/json'
IPINFO_URL 'http://ipinfo.io/210.195.171.202/json'


___ get_ip_country(ip_address
   new_url IPINFO_URL.r..('{ip}',ip_address)
   resp r__.g.. url=new_url)
   data resp.j..
   r.. data 'country' 


get_ip_country('210.195.171.202')