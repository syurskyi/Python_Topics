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
    for i in range(2,len(lines)):
        values = lines[i].split()
        mapping[values[0]] = values[-1]


    return mapping



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

    
    new_string = []
    for c in sequence:
        c = c.upper()
        __ c in mapping:
            new_string.append(c)
    

    return ''.join(new_string)










___ reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """



    return _clean_sequence(sequence,str_table)[::-1]







___ complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    
    mapping = get_mapping(str_table)
    
    new_string = []
    for character in sequence:
        character = character.upper()
        __ character in mapping:
            new_string.append(mapping[character])


    return ''.join(new_string)




___ reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """


    return complement(reverse(sequence,str_table),str_table)



__ __name__ == "__main__":

    get_mapping()
