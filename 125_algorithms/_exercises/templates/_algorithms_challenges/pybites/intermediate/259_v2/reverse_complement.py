# # See tests for a more comprehensive complementary table
# SIMPLE_COMPLEMENTS_STR """#Reduced table with bases A, G, C, T
#  Base	Complementary Base
#  A	T
#  T	A
#  G	C
#  C	G
# """
#
#
# ___ get_mapping str_table_?
#
#
#     lines ?.s..
#
#
#     mapping    # dict
#     ___ i __ r.. 2,l.. ?
#         values ? ?.s..
#         m.. ? 0 ? -1
#
#
#     r.. ?
#
#
#
# # Recommended helper function
# ___ _clean_sequence sequence str_table
#     """
#     Receives a DNA sequence and a str_table that defines valid (and
#     complementary) bases
#     Returns all sequences converted to upper case and remove invalid
#     characters
#     t!t%ttttAACCG --> TTTTTTAACCG
#     """
#
#     mapping ? ?
#
#
#     new_string    # list
#     ___ c __ ?
#         c c.u..
#         __ c __ m..
#             n__.a.. ?
#
#
#     r.. ''.j.. ?
#
#
#
# ___ reverse sequence str_table_?
#     """
#     Receives a DNA sequence and a str_table that defines valid (and
#     complementary) bases
#     Returns a reversed string of sequence while removing all characters
#     not found in str_table characters
#     e.g. t!t%ttttAACCG --> GCCAATTTTTT
#     """
#
#
#
#     r.. _? ? ? ||-1
#
#
#
# ___ complement sequence str_table_?
#     """
#     Receives a DNA sequence and a str_table that defines valid (and
#     complementary) bases
#     Returns a string containing complementary bases as defined in
#     str_table while removing non input_sequence characters
#     e.g. t!t%ttttAACCG --> AAAAAATTGGC
#     """
#
#     mapping ? ?
#
#     new_string    # list
#     ___ character __ ?
#         ? ?.u..
#         __ ? __ m..
#             n__.a.. m.. ?
#
#     r.. ''.j.. n..
#
#
# ___ reverse_complement sequence str_table_?
#     """
#     Receives a DNA sequence and a str_table that defines valid (and
#     complementary) bases
#     Returns a string containing complementary bases as defined in str_table
#     while removing non input_sequence characters
#     e.g. t!t%ttttAACCG --> CGGTTAAAAAA
#     """
#
#
#     r.. c.. r.. ? ? ?
#
#
#
# __ _______ __ _______
#
#     get_mapping()
