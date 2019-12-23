# signal_ignore.py

import signal
import os
import time


def do_exit(sig, stack):
    raise SystemExit('Exiting')


signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print('My PID:', os.getpid())

signal.pause()

# $ python3 signal_ignore.py
#
# My PID: 72598
# ^C^C^C^CExiting

