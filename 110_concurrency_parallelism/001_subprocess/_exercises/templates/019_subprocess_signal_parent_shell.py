# subprocess_signal_parent_shell.py

_____ __
_____ signal
_____ ?
_____ tempfile
_____ t__
_____ ___

script _ '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file _ tempfile.NamedTemporaryFile('wt')
script_file.w..(script)
script_file.f..

proc _ ?.P..(['sh', script_file.name])
print('PARENT      : Pausing before signaling @...'.f..(
    proc.pid))
___.s_o_.f..
t__.s..(1)
print('PARENT      : Signaling child @'.f..(proc.pid))
___.s_o_.f..
__.kill(proc.pid, signal.SIGUSR1)
t__.s..(3)

# $ python3 subprocess_signal_parent_shell.py
#
# PARENT      : Pausing before signaling 26984...
# Shell script in process 26984
# + python3 signal_child.py
# CHILD  26985: Setting up signal handler
# CHILD  26985: Pausing to wait for signal
# PARENT      : Signaling child 26984
# CHILD  26985: Never received signal
