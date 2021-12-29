from collections import Counter
___ calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    

    dna = ['A','G','C','T']

    counts = Counter()

    for character in sequence.upper():
        __ character in dna:
            counts[character] += 1

    

    all_counts = sum(count for count in counts.values())
    percent = (counts.get('G',0) + counts.get('C',0))/all_counts

    return round(percent * 100,2)


