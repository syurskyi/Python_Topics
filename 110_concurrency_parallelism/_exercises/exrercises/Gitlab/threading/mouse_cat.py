# ____ _ ______ ?
# ______ t__
#
# ___ mouse_runs               # The mouse action.
#     w___ T..                  # It keeps the thread alive.
#         print "The mouse runs."
#         t__.s.. 4            # It waits 4 seconds till it's next move.
#
# ___ cat_chases_mouse          # The cat's action.
#     w___ T..:                 # It keeps the thread alive.
#         print "The cat chases the rat."
#         t__.s.. 5            # It waits 5 seconds till it's next move.
#
# ___ action
#
#     mouse_thread  ? ?_?) # Sets the ___ as target.
#     cat_thread  ? ?_?
#
#     ?.s.. T.. # Always set daemon as True.
#     ?.s.. T..   # Always set daemon as True.
#
#     ?.s..         # It starts the mouse thread.
#     ?.s..           # It starts the cat thread.
#
# __ ____ __ ______       # In case of execution by using terminal.
#
#     ?
#
#     w___ T..
#         t__.s.. 1            # Without this wait t__, the thread would
#                                  # consume 90% up of CPU processing t__.
