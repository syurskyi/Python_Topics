from collections import Counter

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    sequence_amount = Counter(sequence)
    GC_amount = sequence_amount['g'] + sequence_amount['c']
    total_amount = sequence_amount['a'] + sequence_amount['g'] + \
                   sequence_amount['c'] + sequence_amount['t']
    return round((GC_amount / total_amount) * 100, 2)