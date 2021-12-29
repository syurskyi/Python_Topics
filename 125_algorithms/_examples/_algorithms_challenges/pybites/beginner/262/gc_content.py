from collections import Counter

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    count = Counter(sequence.lower())
    total_acgt = count['a'] + count['c'] + count['g'] + count['t']
    total_gc = count['c'] + count['g']
    return round( (total_gc/total_acgt) *100,2)

