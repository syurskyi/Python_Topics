____ collections _______ Counter
___ calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    

    dna = ['A','G','C','T']

    counts = Counter()

    ___ character __ sequence.upper():
        __ character __ dna:
            counts[character] += 1

    

    all_counts = s..(count ___ count __ counts.values())
    percent = (counts.get('G',0) + counts.get('C',0))/all_counts

    r.. round(percent * 100,2)


