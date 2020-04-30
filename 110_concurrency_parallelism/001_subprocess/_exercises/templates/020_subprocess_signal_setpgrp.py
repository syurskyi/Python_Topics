
# subprocess_signal_setpgrp.py

_____ __
_____ signal
_____ ?
_____ tempfile
_____ t__
_____ ___


___ show_setting_prgrp():
    print('Calling os.setpgrp() from @'.f..(__.g_p..()))
    __.setpgrp()
    print('Process group is now @'.f..(__.getpgrp()))
    ___.s_o_.f..


script _ '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file _ tempfile.NamedTemporaryFile('wt')
script_file.w..(script)
script_file.f..

proc _ ?.P..(
    ['sh', script_file.name],
    preexec_fn_show_setting_prgrp,
)
print('PARENT      : Pausing before signaling @...'.f..(
    proc.pid))
___.s_o_.f..
t__.s..(1)
print('PARENT      : Signaling process group @'.f..(
    proc.pid))
___.s_o_.f..
__.killpg(proc.pid, signal.SIGUSR1)
t__.s..(3)

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