____ contextlib _______ redirect_stdout
____ io _______ StringIO
____ types _______ BuiltinFunctionType


___ get_len_help_text(builtin: BuiltinFunctionType) -> int:
    """Receives a builtin, and returns the length of its help text.
       You need to redirect stdout from the help builtin.
       If the the object passed in is not a builtin, raise a ValueError.
    """
    __ n.. isi..(builtin,BuiltinFunctionType):
        raise ValueError("Not a built in")
    

    with redirect_stdout(StringIO()) as f:
        help(builtin)


    s = f.getvalue()


    r.. l..(s)



