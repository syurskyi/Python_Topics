______ sys
from operator ______ add, mul, sub

__ sys.version_info[0] __ 2:
    from operator ______ div
____
    from operator ______ floordiv as div


VALID_OPERATIONS = {"plus": add, "minus": sub,
                    "multiplied by": mul, "divided by": div}


___ calculate(stmt
    __ not (stmt.startswith("What is ") and stmt.endswith("?")):
        raise ValueError("Ill-formed question")
    l = stmt[8:-1].strip().lower().split()
    __ not l:
        raise ValueError("Ill-formed question")
    l.reverse()
    try:
        op1 = int(l.pop())
    except ValueError:
        raise ValueError("Ill-formed question")
    w___ l:
        oprt = [l.pop()]
        w___ l:
            try:
                next_tk = l.pop()
                op2 = int(next_tk)
                break
            except ValueError:
                oprt.append(next_tk)
        ____
            raise ValueError("Ill-formed question")
        oprt = " ".join(oprt)
        try:
            op1 = VALID_OPERATIONS[oprt](op1, op2)
        except KeyError:
            raise ValueError("Ill-formed question")
    r_ op1
