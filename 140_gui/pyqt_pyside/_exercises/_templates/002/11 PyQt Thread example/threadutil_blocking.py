# """
# A more powerful, synchronous implementation of run_in_main_thread(...).
# It allows you to receive results from the function invocation:
#
#     @run_in_main_thread
#     def return_2():
#         return 2
#
#     # Runs the above function in the main thread and prints '2':
#     print(return_2())
# """
#
# ____ functools ______ wraps
# ____ ?.?C.. ______ pS.., ?O.., ?T..
# ____ ?.?W.. ______ ?A..
# ____ th.. ______ Event, get_ident
#
# ___ run_in_thread thread_fn
#     ___ decorator f
#         ?w.. ?
#         ___ result $ $$
#             thread _ ?
#             r_ E__.i.. .r_i_t.. th.. f a.. kw..
#         r_ r..
#     r_ d..
#
# ___ _main_thread
#     app _ ?A...i..
#     __ ?
#         r_ ?.th..
#     # We reach here in tests that don't (want to) create a QApplication.
#     __ in. ?T...cTI. __ g_i..
#         r_ ?T...cT..
#     r_ R.. Could not determine main thread
#
# run_in_main_thread _ r_i_t.. _m..
#
# ___ is_in_main_thread
#     r_ ?T...cT.. __ _m..
#
# c_ Executor
#
#     _INSTANCE _ N..
#
#     ??
#     ___ instance ___
#         __ ___._I.. __ N..
#             ___._I.. _ ___ ?A...i..
#         r_ ___._I..
#     ___  -   app
#         _pending_tasks _   # list
#         _app_is_about_to_quit _ F..
#         ?.aTQ__.c.. _a..
#     ___ _a...
#         _app_is_about_to_quit _ T..
#         ___ task __ _p_t..
#             ?.s_e.. SE..
#             ?.h_r_.s..
#     ___ run_in_thread  thread f a.. kw..
#         __ ?T...cT.. __ t..
#             r_ f $ $$
#         ____ _app_is_about_to_quit
#             # In this case, the target thread's event loop most likely is not
#             # running any more. This would mean that our task (which is
#             # submitted to the event loop via signals/slots) is never run.
#             r_ S..
#         task _ T.. f a.. kw..
#         _p___.ap.. ?
#         ___
#             receiver _ R.. ?
#             ?.mTT.. th..
#             sender _ S..
#             ?.si__.c.. r__.sl..
#             ?.si__.e..
#             t__.h_r_.w..
#             r_ t__.r..
#         f..
#             _p___.r.. t..
#
# c_ Task
#     ___  -   fn a.. kw..
#         _? _ ?
#         _? _ ?
#         _? _ ?
#         has_run _ E..
#         _result _ _exception _ N..
#     ___ -c
#         ___
#             _result _ _f_ $_ $$_
#         _____ E.. __ e
#             _e.. _ ?
#         f..
#             h_r_.s..
#     ___ s_e..  ex..
#         _e.. _ ex..
#     ??
#     ___ result
#         __ no. h_r_.i_s..
#             r_ V.. Hasn't run.
#         __ _e__
#             r_ _e__
#         r_ _r..
#
# c_ Sender ?O..
#     signal _ pS..
#
# c_ Receiver ?O..
#     ___  -   callback, parent_N..
#         s_. - p..
#         c.. _ c..
#     ___ slot
#         c..