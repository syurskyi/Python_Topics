# signal_threads_alarm.py

import signal
import time
import threading


def signal_handler(num, stack):
    print(time.ctime(), 'Alarm in',
          threading.currentThread().name)


signal.signal(signal.SIGALRM, signal_handler)


def use_alarm():
    t_name = threading.currentThread().name
    print(time.ctime(), 'Setting alarm in', t_name)
    signal.alarm(1)
    print(time.ctime(), 'Sleeping in', t_name)
    time.sleep(3)
    print(time.ctime(), 'Done with sleep in', t_name)


# Start a thread that will not receive the signal
alarm_thread = threading.Thread(
    target=use_alarm,
    name='alarm_thread',
)
alarm_thread.start()
time.sleep(0.1)

# Wait for the thread to see the signal (not going to happen!)
print(time.ctime(), 'Waiting for', alarm_thread.name)
alarm_thread.join()

print(time.ctime(), 'Exiting normally')

# $ python3 signal_threads_alarm.py
#
# Sat Apr 22 14:49:01 2017 Setting alarm in alarm_thread
# Sat Apr 22 14:49:01 2017 Sleeping in alarm_thread
# Sat Apr 22 14:49:01 2017 Waiting for alarm_thread
# Sat Apr 22 14:49:02 2017 Alarm in MainThread
# Sat Apr 22 14:49:04 2017 Done with sleep in alarm_thread
# Sat Apr 22 14:49:04 2017 Exiting normally

