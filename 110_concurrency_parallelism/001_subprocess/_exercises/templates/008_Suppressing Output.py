# subprocess_run_output_error_suppress.py

_____ ?

try:
    completed _ ?.r..(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        s.._T..,
        stdout_?.DEVNULL,
        stderr_?.DEVNULL,
    )
except ?.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.r_c..)
    print('stdout is {!r}'.format(completed.stdout))
    print('stderr is {!r}'.format(completed.stderr))

# $ python3 subprocess_run_output_error_suppress.py
#
# returncode: 1
# stdout is None
# stderr is None
