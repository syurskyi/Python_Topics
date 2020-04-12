
# subprocess_signal_setpgrp.py

import os
import signal
import subprocess
import tempfile
import time
import sys


def show_setting_prgrp():
    print('Calling os.setpgrp() from {}'.format(os.getpid()))
    os.setpgrp()
    print('Process group is now {}'.format(os.getpgrp()))
    sys.stdout.flush()


script = '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(
    ['sh', script_file.name],
    preexec_fn=show_setting_prgrp,
)
print('PARENT      : Pausing before signaling {}...'.format(
    proc.pid))
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling process group {}'.format(
    proc.pid))
sys.stdout.flush()
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