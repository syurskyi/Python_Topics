____ contextlib _______ redirect_stdout
____ io _______ StringIO
____ types _______ BuiltinFunctionType


___ get_len_help_text(builtin: BuiltinFunctionType) __ i..:
    """Receives a builtin, and returns the length of its help text.
       You need to redirect stdout from the help builtin.
       If the the object passed in is not a builtin, raise a ValueError.
    """
    __ t..(builtin) __ n.. BuiltinFunctionType:
        r.. V...
    std_out StringIO()
    w__ redirect_stdout(std_out
        help(builtin)
    r.. l..(std_out.getvalue


get_len_help_text(pow)