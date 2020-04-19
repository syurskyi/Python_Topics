# # signal_threads_alarm.py
#
# ______ si..
# ______ ti..
# ______ th..
#
#
# ___ signal_handler num stack
#     print(t__.ct.. 'Alarm in',
#           ?.cT.. .n..
#
#
# si__.si__ si__.S.. ?
#
#
# ___ use_alarm
#     t_name _ ?.cT.. .n..
#     print t__.ct.. 'Setting alarm in' ?
#     si__.al.. 1
#     print t__.ct.. 'Sleeping in' ?
#     t__.sl.. 3
#     print t__.ct.. 'Done with sleep in' ?
#
#
# # Start a thread that will not receive the signal
# alarm_thread _ ?.T..|
#     target_u..
#     name_'alarm_thread',
# |
# ?.st..
# t__.sl.. 0.1
#
# # Wait for the thread to see the signal (not going to happen!)
# print(t__.ct.. 'Waiting for', ?.n..
# ?.j..
#
# print(t__.ct.. 'Exiting normally')
#
# # $ python3 signal_threads_alarm.py
# #
# # Sat Apr 22 14:49:01 2017 Setting alarm in alarm_thread
# # Sat Apr 22 14:49:01 2017 Sleeping in alarm_thread
# # Sat Apr 22 14:49:01 2017 Waiting for alarm_thread
# # Sat Apr 22 14:49:02 2017 Alarm in MainThread
# # Sat Apr 22 14:49:04 2017 Done with sleep in alarm_thread
# # Sat Apr 22 14:49:04 2017 Exiting normally
#
