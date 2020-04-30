# subprocess_run_output_error_suppress.py

_____ ?

___
    completed _ ?.r..(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        s.._T..,
        s_o__?.DEVNULL,
        stderr_?.DEVNULL,
    )
_____ ?.C.. __ err:
    print('ERROR:', err)
____
    print('returncode:', completed.r_c..)
    print('stdout is {!r}'.f..(completed.s_o_))
    print('stderr is {!r}'.f..(completed.stderr))

# $ python3 subprocess_run_output_error_suppress.py
#
# returncode: 1
# stdout is None
# stderr is None
