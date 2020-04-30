# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 11
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# ______ a_p..
# ______ re__
# ____ throttler.base_throttler ______ BaseThrottler
#
#
# ___ main(address):
#
#     # Throttle the requests with the BaseThrottler, delaying 1.5s.
#     bt _ BaseThrottler(name_'base-throttler', delay_1.5)
#
#     # Visit the address provided by the user. Complete URL only.
#     r _ ?.Request(method_'GET', url_address)
#
#     # 10 requests.
#     reqs _ [r ___ i __ ra..(0, 10)]
#
#     # Submit the requests with the required throttling.
#     w__ bt:
#         throttled_requests _ bt.submit(reqs)
#
#     # Print the response for each of the requests.
#     ___ r __ throttled_requests:
#         print (r.response)
#
#     # Final status of the requests.
#     print ("Success: {s}, Failures: {f}".f..(s_bt.successes, f_bt.failures))
#
#
# __ _______ __ ______
#     parser _ ?.AP..(d.._'Requests Throttling')
#     ?.a_a..('--address', a.._"store", d.._"address",  d.._'http://www.google.com')
#     given_args _ ?.p_a..
#     address _ ?.address
#     main (address)
#
