# subprocess_run_output.py

import subprocess

completed = subprocess.run(
    ['ls', '-1'],
    stdout=subprocess.PIPE,
)
print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8'))
)

# $ python3 subprocess_run_output.py
#
# returncode: 0
# Have 522 bytes in stdout:
# index.rst
# interaction.py
# repeater.py
# signal_child.py
# signal_parent.py
# subprocess_check_output_error_trap_output.py
# subprocess_os_system.py
# subprocess_pipes.py
# subprocess_popen2.py
# subprocess_popen3.py
# subprocess_popen4.py
# subprocess_popen_read.py
# subprocess_popen_write.py
# subprocess_run_check.py
# subprocess_run_output.py
# subprocess_run_output_error.py
# subprocess_run_output_error_suppress.py
# subprocess_run_output_error_trap.py
# subprocess_shell_variables.py
# subprocess_signal_parent_shell.py
# subprocess_signal_setpgrp.py
