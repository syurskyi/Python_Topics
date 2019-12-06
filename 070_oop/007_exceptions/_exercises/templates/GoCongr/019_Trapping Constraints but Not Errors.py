# # Trapping Constraints but Not Errors
# ___ f x
#     a.. x < 0, 'x must be negative'
#     r___ x ** 2
#
# f(1) # error
#
# ___ reciprocal x
#     a.. x != 0              # A useless assert!
#     r_ 1 / x               # Python checks for zero automatically