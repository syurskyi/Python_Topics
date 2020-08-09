CODONS = {'AUG': "Methionine", 'UUU': "Phenylalanine",
          'UUC': "Phenylalanine", 'UUA': "Leucine", 'UUG': "Leucine",
          'UCU': "Serine", 'UCC': "Serine", 'UCA': "Serine",
          'UCG': "Serine", 'UAU': "Tyrosine", 'UAC': "Tyrosine",
          'UGU': "Cysteine", 'UGC': "Cysteine", 'UGG': "Tryptophan",
          'UAA': "STOP", 'UAG': "STOP", 'UGA': "STOP"}


___ of_codon(codon
    __ codon not in CODONS:
        raise ValueError('Invalid codon: %s' % codon)
    r_ CODONS[codon]


___ of_rna(strand
    proteins = []
    for codon in map(of_codon, _chunkstring(strand, 3)):
        __ codon __ 'STOP':
            break
        proteins.append(codon)
    r_ proteins


___ _chunkstring(string, n
    r_ (string[i:n + i] for i in range(0, le.(string), n))
