# ___ concat_sequence_v1 s1 s2
#     ___ elem __ s1
#         y___ ?
#     ___ ? __ s2
#         y__ ?
#
#
# ___ concat_sequence_v2 s1 s2
#     y___ f.. ?
#     y__ f.. ?
#
#
# seq1 _ ra.. 10
# seq2 _ ra.. 10, 20
# result _ concat_sequence_v1 ? ?
#
# print('Seq 1')
# ___ i __ r..
#     print ?
#
# seq1 _ ra..(10)
# seq2 _ ra..(10, 20)
# result _ _v2 ?
#
# print('Seq 2')
# ___ i __ r..
#     print ?
