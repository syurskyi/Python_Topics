_______ ___
____ operator _______ add, mul, sub

__ ___.version_info[0] __ 2:
    ____ operator _______ div
____:
    ____ operator _______ floordiv __ div


VALID_OPERATIONS = {"plus": add, "minus": sub,
                    "multiplied by": mul, "divided by": div}


___ calculate(stmt
    __ n.. (stmt.startswith("What is ") a.. stmt.e.. "?":
        r.. V...("Ill-formed question")
    l = stmt[8:-1].s...l...s..
    __ n.. l:
        r.. V...("Ill-formed question")
    l.r..
    ___
        op1 = i..(l.pop
    ______ V..
        r.. V...("Ill-formed question")
    w.... l:
        oprt = [l.pop()]
        w.... l:
            ___
                next_tk = l.pop()
                op2 = i..(next_tk)
                _____
            ______ V..
                oprt.a..(next_tk)
        ____:
            r.. V...("Ill-formed question")
        oprt = " ".j..(oprt)
        ___
            op1 = VALID_OPERATIONS[oprt](op1, op2)
        ______ KeyError:
            r.. V...("Ill-formed question")
    r.. op1
