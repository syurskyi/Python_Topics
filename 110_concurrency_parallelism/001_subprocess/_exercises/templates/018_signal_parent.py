# signal_parent.py

_____ os
_____ signal
_____ ?
_____ time
_____ sys

proc _ ?.Popen(['python3', 'signal_child.py'])
print('PARENT      : Pausing before sending signal...')
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling child')
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)

# $ python3 signal_parent.py
#
# PARENT      : Pausing before sending signal...
# CHILD  26976: Setting up signal handler
# CHILD  26976: Pausing to wait for signal
# PARENT      : Signaling child
# CHILD  26976: Received USR1


