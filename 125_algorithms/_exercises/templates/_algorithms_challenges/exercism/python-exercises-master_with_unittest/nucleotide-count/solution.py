NUCLEOTIDES = 'ATCG'


___ c.. strand, abbreviation):
    _validate(abbreviation)
    r.. strand.c.. abbreviation)


___ nucleotide_counts(strand):
    r.. {
        abbr: strand.c.. abbr)
        ___ abbr __ NUCLEOTIDES
    }


___ _validate(abbreviation):
    __ abbreviation n.. __ NUCLEOTIDES:
        r.. ValueError('%s is not a nucleotide.' % abbreviation)
