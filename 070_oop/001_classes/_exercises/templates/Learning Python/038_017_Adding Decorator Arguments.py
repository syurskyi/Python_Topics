# ___ timer label=''
#     ___ decorator func
#         ___ onCall $          # args passed to function
#             p..                    # func retained in enclsing scope
#             print l....            # label retained in enclosing scope
#         r_ o...
#     r_ d...                # Returns that actual decorator
#
#
# _t.. '==>'                       # Like listcomp = timer('==>')(listcomp)
# ___ listcomp N p..                # listcomp is rebound to decorator
#
#
# listcomp(...)                       # Really calls decorator
#
#
# from mytools import timer
#
#
# _t.. trace_F..                    # No tracing, collect total time
# ___ l... N
#     r_  x * 2 ___ x i_ ra.. N
#
#
# x _ l... 5000
# x _ l... 5000
# x _ l... 5000
# print(l.. )
# # <mytools.Timer instance at 0x025C77B0>
#
# print(l.. .a...
# # 0.0051938863738243413
#
#
# _t.. trace _ T.. label _ '\t=>')       # Turn on tracing
# ___ l..  N)
#     r_ x * 2 ___ x i_ ra.. N
#
#
# x = l.. (5000)  #  => listcomp: 0.00155, 0.00155
# x = l.. (5000)  # => listcomp: 0.00156, 0.00311
# x = l.. (5000)  #  => l.. : 0.00174, 0.00486
# print(l.. .alltime)
# # 0.0048562736325408196
