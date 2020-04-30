# subprocess_run_output_error_trap.py

_____ ?

___
    completed _ ?.r..(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        s.._T..,
        s_o__?.P..,
        stderr_?.P..,
    )
_____ ?.C.. __ err:
    print('ERROR:', err)
____
    print('returncode:', completed.r_c..)
    print('Have @ bytes in stdout: {!r}'.f..(
        le.(completed.s_o_),
        completed.s_o_.d..('utf-8'))
    )
    print('Have @ bytes in stderr: {!r}'.f..(
        le.(completed.stderr),
        completed.stderr.d..('utf-8'))
    )

# $ python3 subprocess_run_output_error_trap.py
#
# returncode: 1
# Have 10 bytes in stdout: 'to stdout\n'
# Have 10 bytes in stderr: 'to stderr\n'

