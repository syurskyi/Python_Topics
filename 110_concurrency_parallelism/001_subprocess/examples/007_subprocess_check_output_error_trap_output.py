# subprocess_check_output_error_trap_output.py

import subprocess

try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2',
        shell=True,
        stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('Have {} bytes in output: {!r}'.format(
        len(output),
        output.decode('utf-8'))
    )

# $ python3 subprocess_check_output_error_trap_output.py
#
# Have 20 bytes in output: 'to stdout\nto stderr\n'
