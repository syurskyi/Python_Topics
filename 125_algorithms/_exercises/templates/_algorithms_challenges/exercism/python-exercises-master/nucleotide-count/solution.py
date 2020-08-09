NUCLEOTIDES = 'ATCG'


___ count(strand, abbreviation
    _validate(abbreviation)
    r_ strand.count(abbreviation)


___ nucleotide_counts(strand
    r_ {
        abbr: strand.count(abbr)
        for abbr in NUCLEOTIDES
    }


___ _validate(abbreviation
    __ abbreviation not in NUCLEOTIDES:
        raise ValueError('%s is not a nucleotide.' % abbreviation)
