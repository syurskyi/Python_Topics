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
def get_complement_pair(str_table=SIMPLE_COMPLEMENTS_STR):
    pair_dict = {}
    pair_list = [base.strip() for base in str_table.splitlines() if base[0] != '#' and base[:5] != ' Base']
    for each_pair in pair_list:
        pair_dict[each_pair.split('\t')[0]] = each_pair.split('\t')[-1]
    return pair_dict


def _clean_sequence(sequence, str_table):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    bases = ''.join([base.strip().split('\t')[0] for base in str_table.splitlines() if base[0] != '#' and base[:5] != ' Base'])
    return_str = ''.join([char.upper() for char in sequence if char.upper() in bases])
    return return_str


def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    clear_sequence = _clean_sequence(sequence, str_table)
    return clear_sequence[::-1]


def complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    pair_dict = get_complement_pair(str_table)
    clean_sequence = _clean_sequence(sequence, str_table)
    return ''.join([pair_dict[base] for base in clean_sequence])


def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    pair_dict = get_complement_pair(str_table)
    clean_sequence = reverse(sequence, str_table)
    return ''.join([pair_dict[base] for base in clean_sequence])

#print(reverse('t!t%ttttAACCG', SIMPLE_COMPLEMENTS_STR))

#if (reverse('t!t%ttttAACCG', SIMPLE_COMPLEMENTS_STR)) == 'GCCAATTTTTT':
#    print('correct')


#print(get_complement_pair(COMPLEMENTS_STR))

print(reverse_complement('t!t%ttttAACCG', COMPLEMENTS_STR))