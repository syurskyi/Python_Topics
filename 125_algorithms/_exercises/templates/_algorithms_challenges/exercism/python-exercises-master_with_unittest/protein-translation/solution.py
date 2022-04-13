CODONS {'AUG': "Methionine", 'UUU': "Phenylalanine",
          'UUC': "Phenylalanine", 'UUA': "Leucine", 'UUG': "Leucine",
          'UCU': "Serine", 'UCC': "Serine", 'UCA': "Serine",
          'UCG': "Serine", 'UAU': "Tyrosine", 'UAC': "Tyrosine",
          'UGU': "Cysteine", 'UGC': "Cysteine", 'UGG': "Tryptophan",
          'UAA': "STOP", 'UAG': "STOP", 'UGA': "STOP"}


___ of_codon(codon
    __ codon n.. __ CODONS:
        r.. V...('Invalid codon: %s' % codon)
    r.. CODONS[codon]


___ of_rna(strand
    proteins    # list
    ___ codon __ m.. of_codon, _chunkstring(strand, 3:
        __ codon __ 'STOP':
            _____
        proteins.a..(codon)
    r.. proteins


___ _chunkstring(s__, n
    r.. (s__[i:n + i] ___ i __ r..(0, l..(s__), n
