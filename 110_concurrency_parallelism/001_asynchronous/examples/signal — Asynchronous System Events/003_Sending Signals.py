# signal_alarm.py

import signal
import time


def receive_alarm(signum, stack):
    print('Alarm :', time.ctime())


# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print('Before:', time.ctime())
time.sleep(4)
print('After :', time.ctime())

# $ python3 signal_alarm.py
#
# Before: Sat Apr 22 14:48:57 2017
# Alarm : Sat Apr 22 14:48:59 2017
# After : Sat Apr 22 14:49:01 2017


