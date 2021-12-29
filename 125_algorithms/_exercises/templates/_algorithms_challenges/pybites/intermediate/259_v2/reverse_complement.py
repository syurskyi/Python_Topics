# See tests for a more comprehensive complementary table
SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""


___ get_mapping(str_table=SIMPLE_COMPLEMENTS_STR):


    lines = str_table.splitlines()
    
    
    mapping = {}
    ___ i __ r..(2,l..(lines)):
        values = lines[i].s.. 
        mapping[values[0]] = values[-1]


    r.. mapping



# Recommended helper function
___ _clean_sequence(sequence, str_table):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """

    mapping = get_mapping(str_table)

    
    new_string    # list
    ___ c __ sequence:
        c = c.upper()
        __ c __ mapping:
            new_string.a..(c)
    

    r.. ''.join(new_string)










___ reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """



    r.. _clean_sequence(sequence,str_table)[::-1]







___ complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    
    mapping = get_mapping(str_table)
    
    new_string    # list
    ___ character __ sequence:
        character = character.upper()
        __ character __ mapping:
            new_string.a..(mapping[character])


    r.. ''.join(new_string)




___ reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """


    r.. complement(reverse(sequence,str_table),str_table)



__ __name__ __ "__main__":

    get_mapping()
