CODONS = {'AUG': "Methionine", 'UUU': "Phenylalanine",
          'UUC': "Phenylalanine", 'UUA': "Leucine", 'UUG': "Leucine",
          'UCU': "Serine", 'UCC': "Serine", 'UCA': "Serine",
          'UCG': "Serine", 'UAU': "Tyrosine", 'UAC': "Tyrosine",
          'UGU': "Cysteine", 'UGC': "Cysteine", 'UGG': "Tryptophan",
          'UAA': "STOP", 'UAG': "STOP", 'UGA': "STOP"}


___ of_codon(codon):
    __ codon not in CODONS:
        raise ValueError('Invalid codon: %s' % codon)
    return CODONS[codon]


___ of_rna(strand):
    proteins = []
    for codon in map(of_codon, _chunkstring(strand, 3)):
        __ codon == 'STOP':
            break
        proteins.append(codon)
    return proteins


___ _chunkstring(string, n):
    return (string[i:n + i] for i in range(0, len(string), n))
