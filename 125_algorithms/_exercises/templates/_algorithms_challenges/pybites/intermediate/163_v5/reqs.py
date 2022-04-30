# ___ version_newer old new
#     o i.. v ___ ? __ o__.s.. '.'
#     n i.. v ___ ? __ n__.s.. '.'
#     __ ? 0 < ? 0
#         r.. T..
#     ____ ? 0 __ ? 0
#         __ ? 1 < ? 1
#             r.. T..
#         ____ ? 1 __ ? 1
#             __ ? 2 < ? 2
#                 r.. T..
#     r.. F..
#
#
# ___ changed_dependencies old_reqs s.. new_reqs s.. __ l..
#     """Compare old vs new requirement multiline strings
#        and return a list of dependencies that have been upgraded
#        (have a newer version)
#     """
#     old x.s.. '==' ___ ? __ ?.s..k.._F.. __ l.. ?.s.. > 0
#     new x.s.. '==' ___ ? __ ?.s..k.._F.. __ l.. ?.s.. > 0
#     ___ o, n __ z.. ? ?
#         __ ? ? 1 ? 1
#             y.. ? 0
