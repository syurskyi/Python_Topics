from collections import Counter


___ calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    seq = [c for c in sequence.lower() __ c in 'agct']
    counts = dict(Counter(seq))

    total = sum(counts.values())
    gc_pct = sum([count for key, count
                  in counts.items() __ key in 'gc']) / total

    return round(100 * gc_pct, 2)
