# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# http://code.activestate.com/recipes/413838-memento-closure/
#
# *TL;DR80
# Provides the ability to restore an object to its previous state.
# """
#
# ____ co.. ______ co..
# ____ co.. ______ d_c_
#
#
# ___ memento obj deep_F...
#     state _ d_c_ ?. -d) __ deep _____ co__ ?. -d
#
#     ___ restore
#         ?. -d .cl..
#         ?. -d .up.. s...
#
#     r_ ?
#
#
# c_ Transaction o..
#     """A transaction guard.
#
#     This is, in fact, just syntactic sugar around a memento closure.
#     """
#     deep _ F..
#     states _    # lsit
#
#     ___ - deep $targets
#         ?  ?
#         ?  ?
#         c..
#
#     ___ commit
#         states _ |m.. ta.. de..| ___ ta __ ta..s
#
#     ___ rollback
#         ___ a_state __ s...
#             ?
#
#
# c_ Transactional o..
#     """Adds transactional semantics to methods. Methods decorated  with
#
#     @Transactional will rollback to entry-state upon exceptions.
#     """
#
#     ___ - method
#         ?  ?
#
#     ___ -g obj T
#         ___ transaction $ $$
#             state _ m... o..
#             ___
#                 r_ me.. o.. $ $$
#             _____ E.. __ e
#                 s..
#                 r_ ?
#
#         r_ ?
#
#
# c_ NumObj o..
#
#     ___ - value
#         ?  ?
#
#     ___ -r
#         r_ '<%s: %r>'  -c  .-n  v..
#
#     ___ increment
#         v.. +_ 1
#
#     ?T..
#     ___ do_stuff
#         value _ '1111'  # <- invalid value
#         inc..  # <- will fail and rollback
#
#
# __ _______ __ ______
#     num_obj _ N.. -1
#     print ?
#
#     a_transaction _ T.. T.. ?
#     ___
#         ___ i __ ra.. 3
#             ?.inc..
#             print ?
#         a_t__.c..
#         print('-- committed')
#
#         ___ i __ ra .. 3
#             ?.inc..
#             print ?
#         ?.v.. +_ 'x'  # will fail
#         print ?
#     _____ E.. __ e
#         a_t__.r..
#         print('-- rolled back')
#     print ?
#
#     print('-- now doing stuff ...')
#     ___
#         ?.d_s..
#     _____ E... __ e
#         print('-> doing stuff failed!')
#         ______ ___
#         ______ t_b_
#
#         t_b_.p_e.. f_s__.s..o..
#     print ?
#
#
# ### OUTPUT ###
# # <NumObj: -1>
# # <NumObj: 0>
# # <NumObj: 1>
# # <NumObj: 2>
# # -- committed
# # <NumObj: 3>
# # <NumObj: 4>
# # <NumObj: 5>
# # -- rolled back
# # <NumObj: 2>
# # -- now doing stuff ...
# # -> doing stuff failed!
# # Traceback (most recent call last):
# # File "memento_001.py", line 97, in <module>
# #     num_obj.do_stuff()
# #   File "memento_001.py", line 52, in transaction
# #     raise e
# #   File "memento_001.py", line 49, in transaction
# #     r_ method(obj, *args, **kwargs)
# #   File "memento_001.py", line 70, in do_stuff
# #     increment()     # <- will fail and rollback
# #   File "memento_001.py", line 65, in increment
# #     value +_ 1
# # TypeError: Can't convert 'int' object to str implicitly
# # <NumObj: 2>
