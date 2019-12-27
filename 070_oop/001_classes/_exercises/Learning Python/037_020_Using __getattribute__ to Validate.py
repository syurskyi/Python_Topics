# c_ CardHolder
#     acctlen _ 8                                  # Class data
#     retireage _ 59.5
#
#     ___ - ____, acct, name, age, addr
#         ____.a... _ a...                         # Instance data
#         ____.n... _ n...                         # These trigger __setattr__ too
#         ____.age  _ age                          # acct not mangled: name tested
#         ____.ad.. _ ad..                         # addr is not managed
#         # remain has no data
#     ___ -g ____ n...
#         superget _ obj___. -g             # Don't loop: one level up
#         i_ n... __ 'a...':                             # On all attr fetches
#             r_ ? ____ 'acct' ;-3 + '***'
#         e___ n... __ 'remain'
#             r_ ? ____ 'retireage') - ? ____ 'age'
#         e___
#             r_ ? ____ n...                # name, age, addr: stored
#
#     ___ -s ____ name value
#         i_ n... __ 'n...':                             # On all attr assignments
#             value _ v____.lo__ .re.. ' ', '_'    # addr stored directly
#         e___ n... __ 'age':
#             i_ v... < 0 o_ v... > 150:
#                 r____ V... invalid age
#         e___ n... __ 'acct'
#             value _ v___.re.. '-', ''
#             i_ le. v... !_ ____.ac...
#                 r___ T... invald acct number
#         e___ n... __ 'remain':
#             r____ T... cannot set remain
#         ____. -d n.. _ v..                    # Avoid loops, orig names
#
#
#
