_______ sys
____ operator _______ add, mul, sub

__ sys.version_info[0] __ 2:
    ____ operator _______ div
____:
    ____ operator _______ floordiv as div


VALID_OPERATIONS = {"plus": add, "minus": sub,
                    "multiplied by": mul, "divided by": div}


___ calculate(stmt):
    __ n.. (stmt.startswith("What is ") and stmt.endswith("?")):
        raise ValueError("Ill-formed question")
    l = stmt[8:-1].strip().lower().s.. 
    __ n.. l:
        raise ValueError("Ill-formed question")
    l.reverse()
    try:
        op1 = int(l.pop())
    except ValueError:
        raise ValueError("Ill-formed question")
    while l:
        oprt = [l.pop()]
        while l:
            try:
                next_tk = l.pop()
                op2 = int(next_tk)
                break
            except ValueError:
                oprt.a..(next_tk)
        ____:
            raise ValueError("Ill-formed question")
        oprt = " ".join(oprt)
        try:
            op1 = VALID_OPERATIONS[oprt](op1, op2)
        except KeyError:
            raise ValueError("Ill-formed question")
    r.. op1
