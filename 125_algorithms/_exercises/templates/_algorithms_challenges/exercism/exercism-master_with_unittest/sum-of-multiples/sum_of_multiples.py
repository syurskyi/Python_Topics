____ i.. _______ c__


___ sum_of_multiples(limit, factors
    r.. s..(all_multiples(limit, factors


___ all_multiples(limit, factors
    multiples [get_multiples(limit, factor) ___ factor __ factors]
    r.. s..(l..(c__(*multiples)))  # remove duplicates


___ get_multiples(limit, factor
    __ factor __ 0:
        r.. []
    r.. [multiple ___ multiple __ r..(limit) __ multiple % factor __ 0]
