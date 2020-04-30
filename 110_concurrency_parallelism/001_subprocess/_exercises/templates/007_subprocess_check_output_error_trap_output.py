# subprocess_check_output_error_trap_output.py

_____ ?

___
    output _ ?.c.._output(
        'echo to stdout; echo to stderr 1>&2',
        s.._T..,
        stderr_?.STDOUT,
    )
_____ ?.C.. __ err:
    print('ERROR:', err)
____
    print('Have @ bytes in output: {!r}'.f..(
        le.(output),
        output.d..('utf-8'))
    )

# $ python3 subprocess_check_output_error_trap_output.py
#
# Have 20 bytes in output: 'to stdout\nto stderr\n'
