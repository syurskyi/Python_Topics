# ###Using a Semaphore to synchronize threads
#
# ______ th..
# ______ ti..
# ______ ra__
#
# ##The optional argument gives the initial value for the internal counter;
# ##it defaults to 1.
# ##If the value given is less than 0, ValueError is raised.
# semaphore _ ?.S.. 0
#
# ___ consumer
#     print ("consumer is waiting.")
#     ##Acquire a semaphore
#     ?.a..
#     ##The consumer have access to the shared resource
#     print ("Consumer notify : consumed item number @ " i..
#
#
# ___ producer
#     g.. item
#     t__.s.. 10
#     ##create a random item
#     item _ ra__.r_i.. 0,1000
#     print ("producer notify : producted item number @" i..
#
#     ##Release a semaphore, incrementing the internal counter by one.
#     ##When it was zero on entry and another thread is waiting for it
#     ##to become larger than zero again, wake up that thread.
#     s__.r..
#
#
# #Main program
# __ _______ __ _______
#     ___ i __ ra..  0,5
#         t1 _ ?.T.. t.._p
#         t2 _ ?.T.. t.._c
#         _1.s..
#         _2.s..
#         _1.r..
#         _2.r..
#     print ("program terminated")
#
#
#
#
