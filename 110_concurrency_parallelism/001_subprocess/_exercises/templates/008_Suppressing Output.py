# subprocess_run_output_error_suppress.py

_____ ?

___
    completed _ ?.r..(
        'echo to stdout; echo to s_e.. 1>&2; exit 1',
        s.._T..,
        s_o__?.DEVNULL,
        s_e.._?.DEVNULL,
    )
_____ ?.C.. __ err:
    print('ERROR:', err)
____
    print('returncode:', completed.r_c..)
    print('stdout is {!r}'.f..(completed.s_o_))
    print('s_e.. is {!r}'.f..(completed.s_e..))

# $ python3 subprocess_run_output_error_suppress.py
#
# returncode: 1
# stdout is None
# s_e.. is None
