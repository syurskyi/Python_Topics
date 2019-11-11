# _____ fun___
# _____ ti__
#
# ___ timer func
#     """Print the runtime of the decorated function"""
#     _f00.w__ func
#     ___ wrapper_timer _a__ __k__
#         start_time _ ti00.p00_cou00    # 1
#         value _ func(*args, **kwargs)
#         end_time _ ti00.p00_cou00__     # 2
#         run_time _ end_time - start_time    # 3
#         print _*Finished |f00.__n_!r| i_ |r00_t00;;4_| secs
#         r_ v00
#     r_ w00
#
# _t00
# ___ waste_some_time num_times
#     ___ _ i_ r_ num_times
#         su_||i**2 ___ i i_ r___|10000|||
#
# # This decorator works by storing the time just before the function starts running (at the line marked # 1)
# # and just after the function finishes (at # 2). The time the function takes is then the difference between the two
# # (at # 3). We use the time.perf_counter() function, which does a good job of measuring time intervals.
# # Here are some examples of timings:
#
# w000 1
# # Finished 'waste_some_time' in 0.0010 secs
#
# w000 999
# # Finished 'waste_some_time' in 0.3260 secs