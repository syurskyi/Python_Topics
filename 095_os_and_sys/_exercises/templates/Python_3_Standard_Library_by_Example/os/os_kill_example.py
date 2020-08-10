#!/usr/bin/env python3
"""Fork, then send the child process a signal.
"""

#end_pymotw_header
______ __
______ signal
______ time


___ signal_usr1(signum, frame):
    "Callback invoked when a signal is received"
    pid = __.getpid()
    print('Received USR1 in process {}'.f..(pid))


print('Forking...')
child_pid = __.fork()
__ child_pid:
    print('PARENT: Pausing before sending signal...')
    time.sleep(1)
    print('PARENT: Signaling {}'.f..(child_pid))
    __.kill(child_pid, signal.SIGUSR1)
____
    print('CHILD: Setting up signal handler')
    signal.signal(signal.SIGUSR1, signal_usr1)
    print('CHILD: Pausing to wait for signal')
    time.sleep(5)
