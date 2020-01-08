# _____ fun___
# _____ ti__
#
# ___ timer func
#     """Print the runtime of the decorated function"""
#     ??.? ?
#     ___ wrapper_timer $ $$
#         start_time _ ti__.p00_cou00    # 1
#         value _ ? $ $$
#         end_time _ ti__.p00_cou00__     # 2
#         run_time _ e... - s...    # 3
#         print _*Finished |?. -n!r| in |r00_t00:.4f| secs   # look formating
#         r_ ?
#     r_ ??
#
# ??
# ___ waste_some_time num_times
#     ___ _ i_ ra.. ?      # the first _ is original
#         su_||i**2 ___ i __ ra.. 10000
#
# # This decorator works by storing the time just before the function starts running (at the line marked # 1)
# # and just after the function finishes (at # 2). The time the function takes is then the difference between the two
# # (at # 3). We use the time.perf_counter() function, which does a good job of measuring time intervals.
# # Here are some examples of timings:
#
# ? 1
# # Finished 'waste_some_time' in 0.0010 secs
#
# ? 999
# # Finished 'waste_some_time' in 0.3260 secs