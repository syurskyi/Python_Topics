_______ sys
____ operator _______ add, mul, sub

__ sys.version_info[0] __ 2:
    ____ operator _______ div
____:
    ____ operator _______ floordiv as div


VALID_OPERATIONS = {"plus": add, "minus": sub,
                    "multiplied by": mul, "divided by": div}


___ calculate(stmt):
    __ n.. (stmt.startswith("What is ") a.. stmt.endswith("?")):
        raise ValueError("Ill-formed question")
    l = stmt[8:-1].s...l...s..
    __ n.. l:
        raise ValueError("Ill-formed question")
    l.reverse()
    try:
        op1 = int(l.pop())
    except ValueError:
        raise ValueError("Ill-formed question")
    w.... l:
        oprt = [l.pop()]
        w.... l:
            try:
                next_tk = l.pop()
                op2 = int(next_tk)
                break
            except ValueError:
                oprt.a..(next_tk)
        ____:
            raise ValueError("Ill-formed question")
        oprt = " ".j..(oprt)
        try:
            op1 = VALID_OPERATIONS[oprt](op1, op2)
        except KeyError:
            raise ValueError("Ill-formed question")
    r.. op1
