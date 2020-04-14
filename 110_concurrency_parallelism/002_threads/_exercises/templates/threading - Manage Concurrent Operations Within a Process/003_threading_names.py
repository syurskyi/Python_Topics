# # threading_names.py
#
# ______ th..
# ______ ti..
#
#
# ___ worker
#     print(?.c_t__.gN.. 'Starting'
#     t__.s.. 0.2
#     print ?.c_t__ .gN.. 'Exiting'
#
#
# ___ my_service
#     print ?.c_t__ .gN.. 'Starting'
#     t__.s.. 0.3
#     print ?.c_t__ .gN.. 'Exiting'
#
#
# t _ ?.T.. n.._'my_service', t.._?
# w _ ?.T.. n.._'worker', t.._?
# w2 _ ?.T.. t.._? # use default name
#
# w.s..
# w2.s..
# t.s..
#
# # $ python3 threading_names.py
# #
# # worker Starting
# # Thread-1 Starting
# # my_service Starting
# # worker Exiting
# # Thread-1 Exiting
# # my_service Exiting
#
#
