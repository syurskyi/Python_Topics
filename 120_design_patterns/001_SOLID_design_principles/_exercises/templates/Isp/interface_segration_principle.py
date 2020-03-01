# """
# Interface segregation principle states that many specialized interfaces are better than one universal. In other words
# we can say this also that client must not be forced to implement an interface that it doesn’t use. So the main purpose
# is to divide the interfaces so that they are more specific.
# """
#
# # BAD PRACTICE
#
# ____ a.. ______ A.. a...
# ______ ti..
#
# print('>' * 10)
# print('BAD')
# print('>' * 10)
#
#
# c_ AbstractWorker o...
#     m...
#
#     ?a...
#     ___ work
#         p..
#
#     ?a...
#     ___ eat
#         p..
#
#
# c_ Worker A..W..
#
#     ___ work
#         print("I'm normal worker. I'm working.")
#
#     ___ eat
#         print("Lunch break....(5 secs)")
#         ti__.sl.. 5
#
#
# c_ SuperWorker A..W..
#
#     ___ work
#         print("I'm super worker. I work very hard!")
#
#     ___ eat
#         print("Lunch break....(3 secs)")
#         ti__.sl.. 3
#
#
# c_ Manager o...
#
#     ___  -
#         worker _ N..
#
#     ___ set_worker worker
#         ass... isi.. ? A..., "`worker` must be of type @".f.. A..
#
#         ??  ?
#
#     ___ manage
#         w___.w..
#
#     ___ lunch_break
#         w___.e..
#
#
# # Implement the `Robot` class. However, due to the api defined by `AbstractWorker`,
# # we have to reimplement `eat` method which is not necessary for a `Robot`.
#
# c_ RobotAW..
#
#     ___ work
#         print("I'm a robot. I'm working....")
#
#     ___ eat
#         print("I don't need to eat....")  # This code doing nothing but it is a must. (Bad!)
#
#
# ___ main
#     manager = Manager()
#     manager.set_worker(Worker())
#     # Make normal worker works.
#     manager.manage()
#     # lunch break
#     manager.lunch_break()
#
#     # super worker
#     manager.set_worker(SuperWorker())
#     manager.manage()
#     manager.lunch_break()
#
#     manager.set_worker(Robot())
#     manager.manage()
#     # However, a robot can eat.....
#     manager.lunch_break()
#
#
# main()
#
# # GOOD PRACTICE
# print('>' * 10)
# print('GOOD')
# print('>' * 10)
#
#
# c_ Workable o...
#     m...
#
#     ?a...
#     ___ work
#         p..
#
#
# c_ Eatable o...
#     m..
#
#     ?a...
#     ___ eat
#         p..
#
#
# c_ AbstractWorker(W... E..
#     p..
#
#
# c_ Worker A..W..
#
#     ___ work
#         print("I'm normal worker. I'm working.")
#
#     ___ eat
#         print("Lunch break....(5 secs)")
#         ti__.sl.. 5
#
#
# c_ SuperWorker(A..W..
#
#     ___ work
#         print("I'm super worker. I work very hard!")
#
#     ___ eat
#         print("Lunch break....(3 secs)")
#         ti__.sl.. 3
#
#
# c_ Manager o...
#
#     ___  -
#         ?worker _ N..
#
#
# c_ WorkManager M..
#
#     ___ set_worker  worker
#         ass... isi.. ? W... "`worker` must be of type @".f.. W..
#
#         ??  ?
#
#     ___ manage
#         w__.w..
#
#
# c_ BreakManager M..
#
#     ___ set_worker worker
#         ass..  isi.. ? E... "`worker` must be of type @".f.. E..
#         ??  ?
#
#     ___ lunch_break
#         w__.e..
#
#
# c_ Robot W..
#
#     ___ work
#         print("I'm a robot. I'm working....")
#
#     # No need for implementation of `eat` which is not neccessary for a `Robot`.
#
#
# ___ main
#     work_manager = W..
#     break_manager = B..
#     w___.se.. W..
#     b___.se.. W..
#     # Make normal worker works.
#     w__.ma..
#     # lunch break
#     b__.l_b..
#
#     # super worker
#     w__.se.. S..
#     b__.se.. S..
#     w__.ma..
#     b__.l_b..
#
#     w__.se.. R..
#     w__.ma..
#     __
#         b__.se.. R..
#         b__.l_b..
#     _______
#         p..
#
#
# m..
