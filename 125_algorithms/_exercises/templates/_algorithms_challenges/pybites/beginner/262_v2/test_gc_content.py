# """
# Tests for gc_content.py
# Uses various DNA sequences retrieved from NCBI as input
# Compares user function with calculated GC content
# Inputs are modified to check how the function deals with unknown characters
# """
#
# _______ p__
# ____ ? _______ ?
#
# DNA_SEQUENCES = [
#     (
#         (  # from https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3
#             "tagtgaaagatattcatttcgaaggccttcagcgtgtcgccgttggtgcggccctcctca"
#             "gtatgccggtgcgcacaggcgacacggttaatgatgaagatatcagtaataccattcgcg"
#             "ctctgtttgctaccggcaactttgaggatgttcgcgtccttcgtgatggtgatacccttc"
#             "tggttcaggtaaaagaacgtccgaccattgccagcattactttctccggtaacaaatcgg"
#             "tgaaagatgacatgctgaagcaaaacctcgaggcttctggtgtgcgtgtgggcgaatccc"
#             "tcgatcgcaccaccattgccgatatcgagaaaggtctggaagacttctactacagcgtcg"
#             "gtaaatatagcgccagcgtaaaagctgtcgtgaccccgctgccgcgcaaccgtgttgacc"
#             "taaaactggtgttccaggaaggtgtgtcagctgaaatccagcaaattaacattgttggta"
#             "accatgctttcaccaccgacgaactgatctctcatttccaactgcgtgacgaagtgccgt"
#             "ggtggaacgtggtaggcgatcgtaaataccagaaacagaaactggcgggcgaccttgaaa"
#             "ccctgcgcagctactatctggatcgcggttatgcccgtttcaacatcgactctacccagg"
#             "tcagtctgacgccagataaaaaaggtatttacgtcacggtgaacatcaccgaaggcgatc"
#             "agtacaagctttctggcgttgaagtgagcggcaaccttgccgggcactccgctgaaattg"
#             "agcagctgactaagatcgagccgggtgagctgtataacggcaccaaagtgaccaagatgg"
#             "aagatgacatcaaaaagcttctcggtcgctatggttatgcctatccgcgcgtacagtcga"
#             "tgcccgaaattaacgatgccgacaaaaccgttaaattacgtgtgaacgttgatgcgggta"
#             "accgtttctacgtgcgtaagatccgttttgaaggtaacgatacctcgaaagatgccgtcc"
#             "tgcgtcgcgaaatgcgtcagatggaaggtgcatggctggggagcgatctggtcgatcagg"
#             "gtaaggagcgtctgaatcgtctgggcttctttgaaactgtcgataccgatacccaacgtg"
#             "ttccgggtagcccggaccaggttgatgtcgtctacaaggtaaaagagcgcaacaccggta"
#             "gcttcaactttggtattggttacggtactgaaagtggcgtgagcttccaggctggtgtgc"
#         ),
#         51.35,
#     ),
#     (
#         (  # from https://www.ncbi.nlm.nih.gov/nuccore/CP010052.1
#             "gttaatatttatgattcctgaaaagaaatcaatcgcaatcatgaaagaactaagcattgg"
#             "aaatacaaagcaaatgctgatgattaatggagttgacgtgaaaaatccattgctgctttt"
#             "tttacatggcgggccgggaacgccgcaaatcggatatgttagacattatcaaaaagagct"
#             "ggaacagtattttacagtagttcattgggatcagagaggatcggggctttcttattctaa"
#             "gcgaatttcgcatcactctatgacaataaatcacttcattaaagatacaatccaagtcac"
#             "tcaatggcttttagctcatttttcaaaatcaaaactttacctagccggtcattcttgggg"
#             "atcaatactggcgcttcatgtgctgcagcagcgtcctgatttattttacacgtattatgg"
#             "aatcagccaggttgttaacccgcaagatgaagaatcaactgcttatcaacatattcgtga"
#             "aatttccgaatcaaaaaaagccagcatattatctttccttacacgtttcattggtgctcc"
#             "gccttggaagcaggatatccagcaccttatctatcggttttgtgttgagctaaccagggg"
#             "aggattcactcaccgtcatcgtcaatctctcgctgtattatttcaaatgcttactggcaa"
#             "tgagtatggagtgcggaacatgcacagcttccttaatggattgcgcttcagtaaaaaaca"
#             "tttaactgatgagttgtaccggtttaatgcttttacatcagttccttctattaaagtacc"
#             "gtgtgttttcatttcagggaaacatgacttaattgttcctgcagaaatatcgaaacagta"
#             "ttatcaagaacttgaggcacctgaaaagcgctggtttcaatttgagaattcagctcacac"
#             "cccgcatattgaggagccatcattattcgcgaacacattaagtcggcatgcacgacacca"
#             "tttatgatagatccttgataaataagaaaaacccctgtataataaaaaaagtgtgcaaat"
#             "catgcatattttaaataagtcttgcaacatgcgcctattttctgtataatggtgtatgtt"
#             "ggtctttgactgcgatgaagtgagaggttgctgacacacccggccgctttgccatggcaa"
#             "ggtgttcaggtttttctcacggagaactgtctaacgtgatgtaggcgaaaaggagggaaa"
#             "ataatggcaaaacaaaaaattcgtattcgtttgaaagcatatgatcatagaatccttgat"
#         ),
#         39.37,
#     ),
#     (
#         (  # from https://www.ncbi.nlm.nih.gov/nuccore/CP010052.1
#             # but all As removed, upper and lower case
#             "gtttttttgttcctggtctcgctctggctgcttgg"
#             "tcgctgctgtgtttgggttgcgtgtccttgctgctttt"
#             "tttctggcgggccgggcgccgctcggttgttgctttcggct"
#             "ggcgtttttcgtgttcttgggtcggggtcggggctttcttttct"
#             "gcgtttcgctcctcttgcttccttcttgtctccgtcc"
#             "tctggcttttgctctttttctcctttcctgccggtcttcttgggg"
#             "tctctggcgcttctgtgctgcgcgcgtcctgtttttttccgttttgg"
#             "tcgccggttgttcccgcgtGGtcctgctttcctttcgtg"
#             "tttccgtcgccgcttttctttccttccgtttcttggtgctcc"
#             "gccttgggcggttccgccctttcttcggttttgtgttggctccgggg"
#             "ggttcctcccgtctcgtctctctcgctgttttttctgcttctggc"
#             "tggttgggtgcggctgccgcttcctttggttgcgcttcgtc"
#             "tttctgtggttgtccggttttgcttttctcgttccttctttgtcc"
#             "gtgtgttttctttcgggCtgcttttgttcctgcgttcgcgt"
#         ),
#         55.88,
#     ),
# ]
#
#
# ?p__.m__.p. "dna,gc_content" ?
# ___ test_calculate_gc_content dna gc_content
#
#     ... ? ? __ ?
#
#     dna_with_spaces  "".j.. ? + " " ___ ? __ ?
#     ... ? ? __ ?
#
#     dna_with_special_chars  "".j.. ? + ".!?/," ___ ? __ ?
#     ... ? ? __ ?
#
#     dna_line_breaks  "\n" + ? + "\n" + ? + "\n"
#     ... ? ? __ ?