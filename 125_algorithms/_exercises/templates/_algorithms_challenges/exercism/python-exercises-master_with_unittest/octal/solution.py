___ parse_octal(d..
    d.. = _validate_octal(d..)
    r.. s..(i..(digit) * 8 ** i
               ___ (i, digit) __ e..(r..(d..)))


___ _validate_octal(d..
    ___ d __ d..:
        __ n.. '0' <= d < '8':
            r.. ValueError("Invalid octal digit: " + d)
    r.. d..
