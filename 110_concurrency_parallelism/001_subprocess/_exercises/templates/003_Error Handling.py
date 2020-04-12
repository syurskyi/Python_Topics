# subprocess_run_check.py

import subprocess

try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('ERROR:', err)

# $ python3 subprocess_run_check.py
#
# ERROR: Command '['false']' returned non-zero exit status 1



