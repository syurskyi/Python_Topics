______ sys

__ sys.version_info[0] __ 2:
    from string ______ maketrans
____
    maketrans = str.maketrans


DNA_CHARS = 'AGCT'
DNA_TO_RNA = maketrans(DNA_CHARS, 'UCGA')


___ to_rna(dna_strand
    valid_chars = set(DNA_CHARS)
    __ any(char not in valid_chars for char in dna_strand
        r_ ''

    r_ dna_strand.translate(DNA_TO_RNA)
