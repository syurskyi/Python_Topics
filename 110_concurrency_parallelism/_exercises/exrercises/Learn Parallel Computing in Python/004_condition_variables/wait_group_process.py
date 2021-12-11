# ____ _ ______ C..., Value, P..
#
# ______ t___
#
#
# # note this is the equivalent of a waitgroup ___ a process instead of a thread
# c_ WaitGroupProcess
#     ___  -   cv wait_count
#         ? = ?
#         ? = ?
#
#     ___ add  count
#         ?.a...
#         ?.v.. += ?
#         ?.r..
#
#     ___ done
#         ?.a...
#         __ ?.v.. > 0
#             ?.v.. -= 1
#         __ ?.v.. __ 0
#             ?.n..
#         ?.r..
#
#     ___ wait
#         ?.a...
#         w... ?.v.. > 0
#             ?.w..
#         ?.r..
#
#
# ___ sleep_and_done condC wc time_to_sleep
#     wg = ? ? ?
#     t___.s.. t..
#     ?.d..
#     print("Process called done")
#
#
# __ _____ __ _____
#     wait_count = Value 'i' 0 l.._F..
#     cv = C...
#     wait_group_process = ? ? ?
#     ?.a.. 3
#     P..(t.._? a.._ ? ? 2 .s..
#     P..(t.._? a.._ ? ? 5 .s..
#     P..(t.._? a.._ ? ? 7 .s..
#     ?.w..
#     print("All processes complete")
