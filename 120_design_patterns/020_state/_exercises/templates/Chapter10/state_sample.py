# ____ a.. ______ a.. A..
#
# c_ State m..
#
#     ??
#     ___ doThis
#         p..
#
# c_ StartState S..
#     ___ doThis
#         print("TV Switching ON..")
#
# c_ StopState S...
#     ___ doThis
#         print("TV Switching OFF..")
#
# c_ TVContext S..
#
#     ___ -
#         state _ N..
#
#     ___ getState
#         r_ st..
#
#     ___ setState state
#         ?  ?
#
#     ___ doThis
#         s___.dT..
#
#
# context = T..
# ?.gS..
# start = StartS..
# stop = StopState()
#
# context.setState(stop)
# context.doThis()