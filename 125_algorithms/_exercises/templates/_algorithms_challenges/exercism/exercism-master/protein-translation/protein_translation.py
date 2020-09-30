# Codon                 | Protein
# :---                  | :---
# AUG                   | Methionine
# UUU, UUC              | Phenylalanine
# UUA, UUG              | Leucine
# UCU, UCC, UCA, UCG    | Serine
# UAU, UAC              | Tyrosine
# UGU, UGC              | Cysteine
# UGG                   | Tryptophan
# UAA, UAG, UGA         | STOP

CODON_TO_PROTEIN = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan"
}

STOP_CODONS = set({"UAA", "UAG", "UGA"})
CODON_LENGTH = 3


___ proteins(strand
    polypeptide =   # list
    codons = split_into_codons(strand)

    ___ codon __ codons:
        __ (codon __ STOP_CODONS
            r_ polypeptide
        ____
            polypeptide.append(CODON_TO_PROTEIN[codon])

    r_ polypeptide


___ split_into_codons(strand
    r_ [strand[i:i + CODON_LENGTH] ___ i __ range(0, le.(strand),
                                                      CODON_LENGTH)]
