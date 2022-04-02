# See tests for a more comprehensive complementary table
SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""

COMPLEMENTS_STR = """# Full table with ambigous bases
 Base	Name	Bases Represented	Complementary Base
 A	Adenine	A	T
 T	Thymidine	T 	A
 U	Uridine(RNA only)	U	A
 G	Guanidine	G	C
 C	Cytidine	C	G
 Y	pYrimidine	C T	R
 R	puRine	A G	Y
 S	Strong(3Hbonds)	G C	S
 W	Weak(2Hbonds)	A T	W
 K	Keto	T/U G	M
 M	aMino	A C	K
 B	not A	C G T	V
 D	not C	A G T	H
 H	not G	A C T	D
 V	not T/U	A C G	B
 N	Unknown	A C G T	N
"""


# Recommended helper function
___ _clean_sequence(sequence, str_table
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    sequence_clean = [char.u.. ___ char __ l..(sequence) __ char.isalpha() a.. char.u.. __ str_table]
    r.. "".j..(sequence_clean)


___ _str_table_lookup(str_table
    str_table_split = str_table.s..
    lookup    # dict
    ___ i __ r..(l..(str_table_split)):
        __ i __ [0, 1]:
            _____
        row = str_table_split[i].s..("\t")
        lookup[row[0].s..] = row[-1]
    r.. lookup


___ reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    sequence_clean = _clean_sequence(sequence, str_table)
    r.. sequence_clean[::-1]


___ complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    sequence_clean = l..(_clean_sequence(sequence, str_table))
    str_table_lookup = _str_table_lookup(str_table)

    ___ i __ r..(l..(sequence_clean)):
        sequence_clean[i] = str_table_lookup[sequence_clean[i]]

    r.. "".j..(sequence_clean)


___ reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    sequence_complement = complement(sequence, str_table)
    r.. sequence_complement[::-1]


#if __name__ == "__main__":
    #print(reverse("t!t%ttttAACCG", SIMPLE_COMPLEMENTS_STR))
    #print(complement("t!t%ttttAACCG", SIMPLE_COMPLEMENTS_STR))
    #print(reverse_complement("AGB Vnc gRy Tvv V", COMPLEMENTS_STR)) # 'BBBARYCGNBVCT'