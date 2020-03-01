# ____ a.. ______ A...
# ____ col___.a.. ______ It..
#
#
# c_ Connectable It.. A..
#     ___ connect_to  other
#         __ _____ __ ?
#             r_
#
#         ___ s in ____
#             ___ o __ ?
#                 s.o__.ap.. ?
#                 o.i__.ap.. ?
#
#
# c_ Neuron C...
#     ___ - name
#         ?  ?
#         inputs     # list
#         outputs    # list
#
#     # ___ connect_to(self, other):
#     #     self.outputs.ap..(other)
#     #     other.inputs.ap..(self)
#
#     ___ -it
#         y... ____
#
#     ___ -s
#         r_ _*|n.. |l.. in.. inp.. |le. o.. outputs'
#
#
# c_ NeuronLayer list C..
#     ___ - name count
#         s___ . -
#         ?  ?
#         ___ x _ ra.. 0 ?
#             .ap.. N.. _*|n..-|x '
#
#     ___ -s
#         r_ _*|n.. with |le. ____ neurons'
#
#
# ___ connect_to other
#     __ ____ __ ?
#         r_
#
#     ___ s in ____
#         ___ o in ?
#             s.o___.ap.. ?
#             o.i___.ap.. ?
#
#
# __ _______ __ ______
#     neuron1 = N.. 'n1'
#     neuron2 = N.. 'n2'
#     layer1 = NL.. 'L1', 3
#     layer2 = NL.. 'L2', 4
#
#     # Neuron.connect_to = connect_to
#     # NeuronLayer.connect_to = connect_to
#
#     _1.c.. _2
#     n_1.c___ l_1
#     l_1.c___ n_2
#     l_1.c___l_2
#
#     print n_1
#     print n_2
#     print l_1
#     print l_2
