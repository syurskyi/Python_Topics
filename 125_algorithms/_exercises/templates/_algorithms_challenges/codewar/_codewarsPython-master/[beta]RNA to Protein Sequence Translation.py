rnaDict = '''Phenylalanine (F UUU, UUC
Leucine (L UUA, UUG, CUU, CUC, CUA, CUG
Isoleucine (I AUU, AUC, AUA
Methionine (M AUG
Valine (V GUU, GUC, GUA, GUG
Serine (S UCU, UCC, UCA, UCG, AGU, AGC
Proline (P CCU, CCC, CCA, CCG
Threonine (T ACU, ACC, ACA, ACG
Alanine(A GCU, GCC, GCA, GCG
Tyrosine (Y UAU, UAC
Histidine (H CAU, CAC
Glutamine (Q CAA, CAG
Asparagine (N AAU, AAC
Lysine (K AAA, AAG
Aspartic Acid (D GAU, GAC
Glutamic Acid (E GAA, GAG
Cysteine (C UGU, UGC
Tryptophan (W UGG
Artinine (R CGU, CGC, CGA, CGG, AGA, AGG
Glycine (G GGU, GGC, GGA, GGG
Stop Codon ('Stop' UGA, UAA, UAG'''

______ re
___ protein(rna
    transDict = {}
    for line in rnaDict.split('\n'
        for section in line[line.index(':')+1:].replace(' ','').split(','
            transDict[section] = re.findall(r'\(+\'?(\w+)',line)[0]
    codec = ''
    w___ le.(rna) > 0:
        __ transDict[rna[:3]] __ 'Stop':
            pass
        ____
            codec += transDict[rna[:3]]
        rna = rna[3:]
    r_ codec

