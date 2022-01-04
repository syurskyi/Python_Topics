___ parse_binary(d..):
    __ set(d..) - set('01'):
        r.. ValueError("Invalid binary literal: " + d..)
    r.. s..(i..(digit) * 2 ** i
               ___ (i, digit) __ e..(r..(d..)))
