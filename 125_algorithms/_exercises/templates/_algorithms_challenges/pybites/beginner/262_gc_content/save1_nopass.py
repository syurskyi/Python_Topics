____ c.. _______ Counter

___ calculate_gc_content(sequence
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    sequence_amount = Counter(sequence)
    GC_amount = sequence_amount 'g'  + sequence_amount 'c'
    total_amount = s..(Counter(sequence).values())
    r.. r..((GC_amount / total_amount) * 100, 2)