_______ sys

__ sys.version_info[0] __ 2:
    ____ string _______ maketrans
____:
    maketrans = s...maketrans


DNA_CHARS = 'AGCT'
DNA_TO_RNA = maketrans(DNA_CHARS, 'UCGA')


___ to_rna(dna_strand):
    valid_chars = set(DNA_CHARS)
    __ any(char n.. __ valid_chars ___ char __ dna_strand):
        r.. ''

    r.. dna_strand.translate(DNA_TO_RNA)
