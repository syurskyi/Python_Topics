# subprocess_shell_variables.py

import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)

# $ python3 subprocess_shell_variables.py
#
# /Users/dhellmann
# returncode: 0
