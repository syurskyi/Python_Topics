# # Registering decorated objects to an API
# 
# registry _      # dict
# ___ register obj                          # Both class and func decorator
#     registry o__. -n _ o..            # Add to registry
#     r_ o..                              # Return obj itself, not a wrapper
# 
# _r..
# ___ spam x
#     r_(x ** 2)                          # spam = register(spam)
# 
# _r..
# ___ ham x
#     r_(x ** 3)
# 
# _r..
# c_ Eggs                                 # Eggs = register(Eggs)
#     ___ - ___ x
#         ___.data _ x ** 4
#     ___ -s ___
#         r_ st. ___.d..
# 
# print('Registry:')
# ___ name i_ registry
#     print n.., '=>', ? |n.. ty.. r.. n..|
# 
# print('\nManual calls:')
# print(spam(2))                              # Invoke objects manually
# print(ham(2))                               # Later calls not intercepted
# X = Eggs(2)
# print(X)
# 
# print('\nRegistry calls:')
# ___ name i_ registry
#     print n.. '=>' r... n.. | 3    # Invoke from registry
# 
# 
# # Augmenting decorated objects directly
# 
# ___ decorate func
#     f__.marked _ T..          # Assign function attribute for later use
#     r_ f...
# 
# _d..
# ___ spam(a, b
#     r_ a + b
# 
# sp__.ma..
# # True
# 
# ___ annotate text             # Same, but value is decorator argument
#     ___ decorate func
#         f___.label _ t...
#         r_ f..
#     r_ d...
# 
# _a..  'spam data'
# ___ spam a b                 # spam = annotate(...)(spam)
#     r_ a + b
# 
# spam(1, 2), spam.label
# # (3, 'spam data')
