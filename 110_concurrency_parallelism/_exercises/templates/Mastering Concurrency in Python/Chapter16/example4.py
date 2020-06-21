# # ch16/example4.py
#
# ______ th..
# ____ c__.f.. ______ TPE..
# ______ ti..
# ______ matplotlib.pyplot __ plt
#
# c_ LockedCounter
#     ___  -
#         value _ 0
#         lock _ ?.L..
#
#     ___ i.. x
#         w__ l..
#             new_value _ v.. + ?
#             t__.s..(0.001) # creating a delay
#             value _ ?
#
#     ___ get_value
#         w__ l..
#             ? ?
#
#         r_ ?
#
# c_ ApproximateCounter
#     ___  -  global_counter
#         value _ 0
#         lock _ ?.L..
#         ? ?
#         threshold _ 10
#
#     ___ increment x
#         w__ l..
#             new_value _ v.. + ?
#             t__.s.. 0.001 # creating a delay
#             value _ ?
#
#             __ v >_ th..
#                 g__.i.. v..
#                 v.. _ 0
#
#     ___ get_value
#         w__ l..
#             ? ?
#
#         r_ ?
#
# ###########################################################################
# # Previous single-lock counter
#
# single_counter_n_threads _    # list
# single_counter_times _    # list
# ___ n_workers __ ra.. 1, 11
#     single_counter_n_threads.ap.. ?
#
#     counter _ LC..
#
#     start _ t__.t__
#
#     w__ TPE.. m_w.._? __ executor
#         ?.m.. c__.i.. 1 ___ i __ ra.. 100 * n_
#
#     s_c_t__.ap.. t__.t__ - s..
#
# ###########################################################################
# # New approximate counters
#
# ___ thread_increment counter
#     ?.i.. 1
#
# approx_counter_n_threads _    # list
# approx_counter_times _    # list
# ___ n_workers __ ra.. 1, 11
#     a__.ap.. ?
#
#     global_counter _ ?
#
#     start _ t__.t__
#
#     local_counters _ A.. g_c.. ___ i __ ra.. n_
#     w__ TPE.. m_w.._? __ executor
#         ___ i __ ra.. 100
#             ?.m.. t_i.. l_c..
#
#     a_c_t__.ap.. t__.t__ - s..
#
#     print _*Number of threads: |n_
#     print _*Final counter: |g_c_.g_v.. .
#     print('-' * 40)
#
# ###########################################################################
# # Plotting
#
# single_counter_line, _ ?.pl..(
#     single_counter_n_threads,
#     single_counter_times,
#     c _ 'blue',
#     label _ 'Single counter'
# )
# approx_counter_line, _ plt.plot(
#     approx_counter_n_threads,
#     approx_counter_times,
#     c _ 'red',
#     label _ 'Approximate counter'
# )
# plt.legend(handles_[single_counter_line, approx_counter_line], loc_2)
# plt.xlabel('Number of threads'); plt.ylabel('Time in seconds')
# plt.show()
