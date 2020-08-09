from contextlib ______ redirect_stdout
from io ______ StringIO
from types ______ BuiltinFunctionType


___ get_len_help_text(builtin: BuiltinFunctionType) -> int:
    """Receives a builtin, and returns the length of its help text.
       You need to redirect stdout from the help builtin.
       If the the object passed in is not a builtin, raise a ValueError.
    """
    __ not isinstance(builtin, BuiltinFunctionType
        raise ValueError()
    f = StringIO()
    with redirect_stdout(f
        help(builtin)
    r_ le.(f.getvalue())
