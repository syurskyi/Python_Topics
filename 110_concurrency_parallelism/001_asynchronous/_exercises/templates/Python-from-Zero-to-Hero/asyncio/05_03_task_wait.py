# ____ ____
# _____ ____ ____ F..
# _____ c.. ____ n..
#
# ____ ai..
#
# Service = n.. 'Service', ('name', 'url', 'ip_attr'
#
# services = (
#     ?('ipify', 'https://api.ipify.org?format=json', 'ip'),
#     ?('ip-api', 'http://ip-api.com/json', 'query')
# )
#
#
# _____ ___ get_json url
#     _____ w___ a__.C.. __ session
#         _____ w___ ?.g.. ? __ response
#             r_ _____ ?.j___
#
#
# _____ ___ fetch_ip service
#     print _* Fetching IP from |?.n..|
#
#     json_response = _____ g.. ?.u..
#     ip = ? ?.i..
#     r_ _*|?.n..| finished with result: |?|
#
#
# _____ ___ main
#     coros = ? service ___ ? __ services
#
#     done, pending = _____ ____.w.. ? return_when=F..
#
#     ___ x __ d..
#         print ?.r..
#
#
# __ _______ __ _______
#     ____.r.. m..
