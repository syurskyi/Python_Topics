from collections import Counter
"""
The DNA of all organsims consists of the letters (bases) A, C, T and G. Every organism has a
different ratio of these bases, known as the GC content. This information can not only give
clues about the origin of genetic material but can also help to determine how closely related some organisms are.

For the given DNA sequences calculate the GC content as a percentage of all (allowed)
bases (=percentage of the letters G or C).

Example:
DNA Sequence:
AAAAAAAATTTTTTGGGGCC
A=8, T=6, G=4, C=2, TOTAL = 20
GC content = n(G|C) / n(A|C|G|T) = 6/20 = 3/10 => 30%
For more background info on DNA check out this link.
"""

s = "tgtggtttctttcgggccttcgcgtgtcgccgttggtgcggccctcctc"

def calculate_gc_content_1st_solution(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    counts = {}
    bases_dict = {}
    bases = "atgc"
    sequence = sequence.lower()
    for b in bases:
        bases_dict[b] = False

    for seq in sequence:
        bases_dict[seq] = True
        try:
            counts[seq] += 1
        except KeyError:
            counts[seq] = 1
    for k,v in bases_dict.items():
        if v == False:
            counts[k] = 0

    result = float("{0:.2f}".format(((counts['g'] + counts['c']) / (counts['a'] + counts['c'] + counts['g'] + counts['t'])) * 100))
    try:
        return result
    except:
        return 0

def calculate_gc_content_2nd_solution(sequence):

    counts = Counter(sequence.upper())
    gc_content = counts['G'] + counts['C']
    at_content = counts['A'] + counts['T']
    return round((gc_content / (gc_content + at_content)) * 100, 2)



print(calculate_gc_content_2nd_solution(s))