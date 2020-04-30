# signal_child.py

_____ os
_____ signal
_____ time
_____ ___

pid _ os.getpid()
received _ False


def signal_usr1(signum, frame):
    "Callback invoked when a signal is received"
    global received
    received _ T..
    print('CHILD {:>6}: Received USR1'.f..(pid))
    ___.s_o_.f..


print('CHILD {:>6}: Setting up signal handler'.f..(pid))
___.s_o_.f..
signal.signal(signal.SIGUSR1, signal_usr1)
print('CHILD {:>6}: Pausing to wait for signal'.f..(pid))
___.s_o_.f..
time.sleep(3)

__ no. received:
    print('CHILD {:>6}: Never received signal'.f..(pid))

