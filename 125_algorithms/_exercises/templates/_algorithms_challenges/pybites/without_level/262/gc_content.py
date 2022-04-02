____ c.. _______ Counter


___ calculate_gc_content(sequence
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    seq = [c ___ c __ sequence.l.. __ c __ 'agct'
    counts = d..(Counter(seq))

    total = s..(counts.values())
    gc_pct = s..([count ___ key, count
                  __ counts.i.. __ key __ 'gc' ) / total

    r.. r..(100 * gc_pct, 2)
