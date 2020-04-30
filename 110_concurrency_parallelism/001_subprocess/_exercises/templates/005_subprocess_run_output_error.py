# subprocess_run_output_error.py

_____ ?

___
    completed _ ?.r..(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        c.._T..,
        s.._T..,
        stdout_?.PIPE,
    )
_____ ?.C.. __ err:
    print('ERROR:', err)
else:
    print('returncode:', completed.r_c..)
    print('Have {} bytes in stdout: {!r}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8'))
    )

# $ python3 subprocess_run_output_error.py
#
# to stderr
# ERROR: Command 'echo to stdout; echo to stderr 1>&2; exit 1'
# returned non-zero exit status 1
