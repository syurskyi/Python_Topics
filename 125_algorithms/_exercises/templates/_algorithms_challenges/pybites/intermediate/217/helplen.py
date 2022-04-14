____ contextlib _______ redirect_stdout
____ i. ______ S..
____ types _______ BuiltinFunctionType


___ get_len_help_text(builtin: BuiltinFunctionType) __ i..
    """Receives a builtin, and returns the length of its help text.
       You need to redirect stdout from the help builtin.
       If the the object passed in is not a builtin, raise a ValueError.
    """
    __ n.. isi..(builtin,BuiltinFunctionType
        r.. V...("Not a built in")
    

    w__ redirect_stdout(StringIO __ f:
        help(builtin)


    s f.getvalue()


    r.. l..(s)



