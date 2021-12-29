____ collections _______ Counter


___ calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    seq = [c ___ c __ sequence.lower() __ c __ 'agct']
    counts = d..(Counter(seq))

    total = s..(counts.values())
    gc_pct = s..([count ___ key, count
                  __ counts.items() __ key __ 'gc']) / total

    r.. round(100 * gc_pct, 2)
