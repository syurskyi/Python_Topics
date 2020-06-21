# signal_signal.py

import signal
import os
import time


def receive_signal(signum, stack):
    print('Received:', signum)


# Register signal handlers
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

# Print the process ID so it can be used with 'kill'
# to send this program signals.
print('My PID is:', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)

# $ python3 signal_signal.py
#
# My PID is: 71387
# Waiting...
# Waiting...
# Waiting...
# Received: 30
# Waiting...
# Waiting...
# Received: 31
# Waiting...
# Waiting...
# Traceback (most recent call last):
#   File "signal_signal.py", line 28, in <module>
#     time.sleep(3)
# KeyboardInterrupt

