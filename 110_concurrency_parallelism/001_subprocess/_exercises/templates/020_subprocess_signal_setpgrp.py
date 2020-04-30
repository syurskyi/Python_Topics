
# subprocess_signal_setpgrp.py

_____ os
_____ signal
_____ ?
_____ tempfile
_____ time
_____ sys


def show_setting_prgrp():
    print('Calling os.setpgrp() from @'.f..(os.getpid()))
    os.setpgrp()
    print('Process group is now @'.f..(os.getpgrp()))
    sys.s_o_.flush()


script _ '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file _ tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc _ ?.P..(
    ['sh', script_file.name],
    preexec_fn_show_setting_prgrp,
)
print('PARENT      : Pausing before signaling @...'.f..(
    proc.pid))
sys.s_o_.flush()
time.sleep(1)
print('PARENT      : Signaling process group @'.f..(
    proc.pid))
sys.s_o_.flush()
os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)

# $ python3 subprocess_signal_setpgrp.py
#
# Calling os.setpgrp() from 75636
# Process group is now 75636
# PARENT      : Pausing before signaling 75636...
# Shell script in process 75636
# + python3 signal_child.py
# CHILD  75637: Setting up signal handler
# CHILD  75637: Pausing to wait for signal
# PARENT      : Signaling process group 75636
# CHILD  75637: Received USR1