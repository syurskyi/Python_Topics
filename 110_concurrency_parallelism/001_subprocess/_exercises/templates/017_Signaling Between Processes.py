# signal_child.py

_____ os
_____ signal
_____ time
_____ sys

pid _ os.getpid()
received _ False


def signal_usr1(signum, frame):
    "Callback invoked when a signal is received"
    global received
    received _ T..
    print('CHILD {:>6}: Received USR1'.f..(pid))
    sys.s_o_.flush()


print('CHILD {:>6}: Setting up signal handler'.f..(pid))
sys.s_o_.flush()
signal.signal(signal.SIGUSR1, signal_usr1)
print('CHILD {:>6}: Pausing to wait for signal'.f..(pid))
sys.s_o_.flush()
time.sleep(3)

if not received:
    print('CHILD {:>6}: Never received signal'.f..(pid))

