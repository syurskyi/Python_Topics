# """Composite pattern
# """
# ____ a.. ______ A.. a..
#
#
# c_ Component A..
#
#     ___  -  name
#         ?  ?
#         level _ 0
#         indentation _ ""
#
#     ??
#     ___ traverse
#         """Print the name of this component and all of its children.
#
#         Implement in Composite and Leaf
#         """
#         p..
#
#
# c_ Leaf C..
#
#     ___ traverse
#         print "@ @".f.. i..., self.n...
#
#
# c_ Composite C..
#
#     ___  -  name
#         # super().__init__(name)  # ok in Python 3.x, not in 2.x
#         s___ -c ____. - ?  # also ok in Python 2.x
#         c... _ li..
#
#     # we can design the "child management" interface here (we have safety,
#     # namely a client cannot append/remove a child ____ a Leaf), or design such
#     # interface in the Component class (we have transparency, but a client
#     # could try to perform meaningless things like appending a node to a Leaf)
#
#     ___ append_child, child
#         ?.level _ l.. + 1
#         ?.i... _ " " * ?.l.. * 2
#         c____.ap.. ?
#
#     ___ remove_child  child):
#         c...r.. ?
#
#     ___ traverse
#         print("@ @".f.. .i..., n..
#         |x.tr.. ___ ? __ c..
#
#
# ___ main
#     c0 _ C... ("/")
#     l0 _ L..  "hello.txt"
#     l1 _ L..  "readme.txt"
#     c1 _ C... "home"
#     c0.a_c.. l0
#     c0.a_c.. l1
#     c0.a_c.. c1
#
#     l2 _ L.. "notes.txt"
#     l3 _ L.. "todo.txt"
#     c2 _ C... "documents"
#     c1.a_c.. l2
#     c1.a_c.. l3
#     c1.a_c.. c2
#
#     l4 _ L.. ("draft.txt")
#     c2.a_c.. (l4)
#
#     print("Traverse the entire directory tree")
#     c0.traverse()
#
#     print('\nRemove "todo.txt" and traverse the tree once again')
#     c1.r_c.. l3
#     c0.tr..
#
#     print('\nRemove "home" and traverse the tree once again')
#     c0.r_c.. c1
#     c0.tr..
#
#
# __ _______ __ ______
#     ?
