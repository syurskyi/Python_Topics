from itertools ______ count

CODON_MAP = (
    (('AUG',),'Methionine'),
    (('UUU', 'UUC'),'Phenylalanine'),
    (('UUA', 'UUG'),'Leucine'),
    (('UCU', 'UCC', 'UCA', 'UCG'),'Serine'),
    (('UAU', 'UAC'),'Tyrosine'),
    (('UGU', 'UGC'),'Cysteine'),
    (('UGG',),'Tryptophan'),
    (('UAA', 'UAG', 'UGA'),'STOP'))

PROTEINS = { codon: name ___ codons, name in CODON_MAP ___ codon in codons }

___ proteins(strand
    proteins = []
    ___ i in count(0, 3
        codon = strand[i:i+3] 
        protein = PROTEINS.get(codon, None)
        __ protein pa__ 'STOP' or le.(codon) < 3:
            r_ proteins
        ____ proteins pa__ not None:
            proteins.append(protein)
