# subprocess_signal_parent_shell.py

import os
import signal
import subprocess
import tempfile
import time
import sys

script = '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(['sh', script_file.name])
print('PARENT      : Pausing before signaling {}...'.format(
    proc.pid))
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling child {}'.format(proc.pid))
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
time.sleep(3)

# $ python3 subprocess_signal_parent_shell.py
#
# PARENT      : Pausing before signaling 26984...
# Shell script in process 26984
# + python3 signal_child.py
# CHILD  26985: Setting up signal handler
# CHILD  26985: Pausing to wait for signal
# PARENT      : Signaling child 26984
# CHILD  26985: Never received signal
