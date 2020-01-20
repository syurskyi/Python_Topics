# c_ classic
#     ___ -g ____ name
#         __ name __ 'age':
#             r_ 40
#         ____
#             ra.. A..
#
# x = ?
# print('#' * 23 + ' Runs __getattr__')
# print ?.age                                 # Runs __getattr__
#
# # x.name                                # Runs __getattr__
# # AttributeError
#
#
# c_ newprops o..
#     ___ getage ____
#         r_ 40
#     age _ pr.. ? N.. N.. N..  # get, set, del, docs
#
# x = ?
# print('#' * 23 + ' Runs getage')
# print ?.a..                                         # Runs getage
#
# # x.name                                        # Normal fetch
# # AttributeError: newprops instance has no attribute 'name'
#
#
# c_ newprops o..
#     ___ getage ____
#         r_ 40
#
#     ___ setage ____ value
#         print('set age:' ?
#         ____._age _ ?
#     age = pr.. ? ? N.. N..
#
# x = ?
# print('#' * 23 + ' Runs getage')
# print(?.a..                                         # Runs getage
#
# ?.a.. _ 42                                    # Runs setage
#
# print('#' * 23 + ' Normal fetch; no getage call')
# print ?._a..                                        # Normal fetch; no getage call
#
# ?.job _ 'trainer'                             # Normal assign; no setage call
# print('#' * 23 + ' Normal fetch; no getage call')
# print ?.j..                                         # Normal fetch; no getage call
#
#
# c_ classic
#     ___ -g ____ name              # On undefined reference
#         __ name __ 'age'
#             r_ 40
#         ___
#             r____ A...
#
#     ___ -s ____ name value       # On all assignments
#         print('set:', ? ?
#         __ n.. __ 'age'
#             ____. -d  '_age' _ v...
#         ____
#             ____. -d name _ v...
#
# x _ cl...
# print('#' * 23 + ' Runs __getattr__')
# print ?.a..                                         # Runs __getattr__
#
# ?.a.. _ 41                                    # Runs __setattr__
# print('#' * 23 + ' Defined: no __getattr__ call')
# print ?._a..                                        # Defined: no __getattr__ call
#
# print('#' * 23 + ' Defined: no __getattr__ call')
# ?.j.. _ 'trainer'                             # Runs __setattr__ again
# print ?.j..                                         # Defined: no __getattr__ call
