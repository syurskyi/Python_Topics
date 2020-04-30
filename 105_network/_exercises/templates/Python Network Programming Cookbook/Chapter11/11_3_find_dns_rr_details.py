# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 11
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ a_p..
# ______ d__.z..
# ______ d__.r..
# ______ ?
#
# ___ main address
#     # IPv4 DNS Records
#     answer _ ?.r__.q.. ? 'A'
#     ___ i __ xr.. 0 le. ?
#         print("Default: ", a.. ?
#
#     # IPv6 DNS Records
#     ___
#         answer6 _ ?.r__.q.. ? 'AAAA'
#         ___ i __ xr.. 0 le. a_6
#             print("Default: ", a_6 ?
#     ______ ?.r__.NA.. __ e
#         print("Exception in resolving the IPv6 Resource Record:", e)
#
#     # MX (Mail Exchanger) Records
#     ___
#         mx _ ?.r__.q.. ? 'MX'
#         ___ i __ xr.. 0 le. ?
#             print("Default: " ? ?
#     ______ ?.r__.NA.. __ e
#         print("Exception in resolving the MX Resource Record:" ?
#
#     ___
#         cname_answer _ ?.r__.q.. ? 'CNAME'
#         print("CNAME: " ?
#     ______ ?.r__.NA.. __ e
#         print('Exception retrieving CNAME' ?
#
#     ___
#         ns_answer _ ?.r__.q.. ? 'NS'
#         print ?
#     ______ ?.r__.NA.. __ e
#         print("Exception in resolving the NS Resource Record:" ?
#
#     ___
#         sig_answer _ ?.r__.q..(?, 'SIG')
#         print("SIG: " ?
#     ______ ?.r__.NA.. __ e
#         print('Exception retrieving SIG' ?
#
#     ___
#         key_answer _ ?.r__.q.. ? 'KEY')
#         print("KEY: " ?
#     ______ ?.r__.NA.. __ e
#         print('Exception retrieving KEY' ?
#
#     soa_answer _ ?.r__.q.. ? 'SOA'
#     print("SOA Answer: ", ? 0 .mn..
#     master_answer _ ?.r__.q.. ? 0 .mn.. 'A'
#     print("Master Answer: " ? 0 .?
#
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'DNS Python'
#     ?.a_a.. '--address' a.._"store" d.._"address"  d.._'dnspython.org'
#     given_args _ ?.p_a..
#     address _ ?.a..
#     ? ?
#
