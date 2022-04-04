____ c.. _______ C..
___ calculate_gc_content(sequence
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    

    dna =  'A','G','C','T'

    counts = C..()

    ___ character __ sequence.u..:
        __ character __ dna:
            counts[character] += 1

    

    all_counts = s..(count ___ count __ counts.values
    percent = (counts.g.. 'G',0) + counts.g.. 'C',0/all_counts

    r.. r..(percent * 100,2)


