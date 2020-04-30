# subprocess_run_output_error_trap.py

_____ ?

try:
    completed _ ?.r..(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell_True,
        stdout_?.PIPE,
        stderr_?.PIPE,
    )
except ?.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.r_c..)
    print('Have {} bytes in stdout: {!r}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8'))
    )
    print('Have {} bytes in stderr: {!r}'.format(
        len(completed.stderr),
        completed.stderr.decode('utf-8'))
    )

# $ python3 subprocess_run_output_error_trap.py
#
# returncode: 1
# Have 10 bytes in stdout: 'to stdout\n'
# Have 10 bytes in stderr: 'to stderr\n'

