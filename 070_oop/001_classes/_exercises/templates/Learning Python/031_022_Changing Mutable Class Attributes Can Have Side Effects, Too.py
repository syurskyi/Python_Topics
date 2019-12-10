# c_ C
#     shared =     # list                 # Class attribute
#     ___ -  _____
#         ____.perobj =     # list        # Instance attribute
#
# x = ?                         # Two instances
# y = ?                         # Implicitly share class attrs
# y.shared, y.perobj
#
# x.s__.ap_ spam         # Impacts y's view too!
# x.p_.ap.spam         # Impacts x's data only
# x.sh.. x.per..
#
# y.sh.. y.pe..              # y sees change made through x
# C.sh..                        # Stored on class and shared
#
# x.sh_.ap.. spam    # Changes shared object attached to class in-place
# x.sh_ = 'spam'          # Changed or creates instance attribute attached to x
