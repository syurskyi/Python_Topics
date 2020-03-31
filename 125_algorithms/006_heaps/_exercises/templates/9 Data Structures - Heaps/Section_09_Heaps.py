# c_ Heap o..
#     HEAP_SIZE _ 10
#
#     ___ -
#         heap _ |0 * H__.H..
#         currentPosition _ -1
#
#     ___ insert item
#
#         __ isFull
#             print("Heap is full..")
#             r_
#
#         currentPosition _ ? + 1
#         h..|? _ i..
#         fU. ?
#
#     ___ fixUp index
#
#         parentIndex _ in. ? - 1) / 2
#
#         w___ ? >_ 0 an. h..|? < h..|i..
#             temp _ h..|i..
#             h..|i.. _ h..|?
#             h..|? _ temp
#             i.. _ ?
#             ? _ in. i... - 1) / 2
#
#     ___ heapsort
#
#         ___ i __ RA.. 0 c.. + 1
#             temp _ h..|0
#             print("@ "  ?   # digit
#             h..|0 _ h..[c.. - i]
#             h..[c.. - i] _ ?
#             fD.. 0 c.. - i - 1
#
#     ___ fixDown index upto
#
#         w__ ? <_ ?
#
#             leftChild _ 2 * i.. + 1
#             rightChild _ 2 * i.. + 2
#
#             __ l.. < u..
#                 cTS.. _ N..
#
#                 __ r.. > u..
#                     cTS.. _ l..
#                 ____
#                     __ h..|l.. > h..|r..
#                         cTS.. _ l..
#                     ____
#                         cTS.. _ r..
#
#                 __ h..|i.. < h..|cTS..
#                     temp _ h..|i..
#                     h..|i.. _ h..|cTS..
#                     h..|cTS.. _ t..
#                 ____
#                     b..
#
#                 i.. _ cTS..
#             ____
#                 b..
#
#     ___ isFull
#         __ cP.. __ H__.H..
#             r_ T..
#         ____
#             r_ F..
#
#
# __ _______ __ _____
#     heap _ ?
#     heap.insert(10)
#     heap.insert(-20)
#     heap.insert(0)
#     heap.insert(2)
#     heap.insert(4)
#     heap.insert(5)
#     heap.insert(6)
#     heap.insert(7)
#     heap.insert(20)
#     heap.insert(15)
#
#     heap.heapsort()
