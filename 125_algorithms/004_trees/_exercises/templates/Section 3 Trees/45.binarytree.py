# #!/usr/bin/python
#
# c_ Node
#     ___ - data
#         l _ N..
#         r _ N..
#         v _ ?
#
# c_ binTree
#     ___ -
#         root _ N..
#
#     ___ getRoot
#         r_ ?
#
#     ___ addnode data
#         __ |r.. __ N..
#             r.. _ ? ?
#         ____
#             _add ? r..
#
#     ___ _add data node
#         __ |? < n__.v
#             __ |n__.l !_ N..
#                 _?| n__.l
#             ____
#                 n__.l _ ? ?
#         ____
#             __ |n__.r !_ N..
#                 _? ? ?.r
#             ____
#                 n__.r _ ? ?
#
#     ___ findnode data
#         __ |r.. !_ N..
#             r_ _? ? r..
#         ____
#             r_ N..
#
#     ___ _find data node
#         __ |? __ n__.v
#             r_ n..
#         ____ |? < n__.v an. n__.l !_ N..
#             _? ? n__.l
#         ____ |? > n__.v an. n__.r !_ N..
#             _? ? N__.r
#
#     ___ deleteTree
#         r.. _ N..
#
#     ___ printFullTree
#         __ |r.. !_ N..
#             _? r..
#
#     ___ _printTree node
#         __ |node !_ N..
#             _? n__.l
#             print st. n__.v| + ' '
#             _? n__.r
#
#
# ___ checkwhetheritsabintree root
#     __ r.. __ N..
#         r_ 1
#     # false __ left is > than root
#     __ r...l !_ N.. an. r...l.v > r...v
#         r_ 0
#
#     # false __ right is < than root
#     __ r...r !_ N.. an. r...r.v < r...v:
#         r_ 0
#
#     # false __, recursively, the left or right is not a BST
#     __ no. checkwhetheritsabintree(r...l) o. no. checkwhetheritsabintree(r...r):
#         r_ 0
#
#     # passing all that, it's a BST
#     r_ 1
#
#
# ___ levelOrder root
#     items _    # list
#     count _ 0
#     i__.i.. c.. r..
#     elements _ ""
#     w__ i.. !_    # list
#         temp _ i__.p..
#         e.. _ e.. + st. ?.v + " "
#         __ t__.l !_ N..
#             i__.i.. 0 t__.l
#         __ t__.r !_ N..
#             i__.i.. 0, t__.r
#     print("Level order traversal of BST: " + ?
#
#
# ___ findsize tree
#     __ no. ?
#         r_ 0
#     r_ ?|?.l + ?|?.r + 1
#
#
# ___ printReverse root
#     items _    # list
#     count _ 0
#     i__.i.. c.. r..
#     elements _ ""
#     w__ i.. !_    # list
#         temp _ i__.p..
#         e... _ st. t__.v + " " + e..
#         __ t__.l !_ N..
#             i__.i.. 0 t__.l
#         __ t__.r !_ N..
#             i__.i.. 0 t__.r
#     print("Level order traversal of BST: " + ?
#
#
# ___ maximumDepthOfTree root
#     __ r.. __ N..
#         r_ 0
#     r_ ma. ?|r...l ?|r...r|| + 1
#
#
# ___ deepestNode root
#     items _    # list
#     count _ 0
#     i__.i.. ? r..
#     elements _ ""
#     w__ i.. !_    # list
#         temp _ i__.p..
#         e.. _ st. t__.v + " " + e..
#         __ t__.l !_ N..
#             i__.i.. 0 t__.l
#         __ t__.r !_ N..
#             i__.i.. 0 t__.r
#         ___ p __ i__: print(p.v)
#         print("####")
#
#     print("Deepest node is " t__.v
#
#
# ___ countLeaves root
#     items _    # list
#     count _ 0
#     i__.i..|? r..
#     elements _ ""
#     w__ i__ !_    # list
#         temp _ i__.p..
#         __ t__.l is N.. an. t__.r __ N..
#             c.. +_ 1
#         __ t__.l !_ N..
#             i__.i.. 0 t__.l
#         __ t__.r !_ N..
#             i__.i.. 0 t__.r
#
#     print("number of leafs in the tree " ?
#
#
# ___ countFullNodes root
#     items _    # list
#     count _ 0
#     i__.i.. c.., r..
#     w__ i__ !_    # list:
#         temp _ i__.p..
#         __ t__.l __ no. N.. an. t__.r __ no. N..
#             c.. +_ 1
#         __ t__.l !_ N..
#             i__.i.. 0 t__.l
#         __ t__.r !_ N..
#             i__.i.. 0 t__.r
#
#     print("number of full nodes in the tree " ?
#
#
# ___ countHalfNodes root
#     items _    # list
#     count _ 0
#     items.i.. c.. r..
#     w__ i__ !_    # list:
#         temp _ i__.p..
#         __ (t__.l __ N.. an. t__.r __ no. N..) o. \
#                 (t__.l __ no. N.. an. t__.r __ N..)
#             c.. +_ 1
#         __ t__.l !_ N..
#             i__.i.. 0 t__.l
#         __ t__.r !_ N..
#             i__.i.. 0 t__.r
#
#     print("number of half nodes in the tree " ?
#
#
# ptr _ 0
#
#
# ___ diaTree root
#     g.. ?
#     __ |no. r..
#         r_ 0
#     left _ ?|r...l
#     right _ ?|r...r
#
#     __ |l.. + r.. > p..
#         p.. _ l.. + r..
#     r_ ma. l.. r.. + 1
#
#
# ___ appendpath root path paths
#     __ no. r..
#         r_ 0
#
#     p__.ap.. r...v
#     print "PATH:", p__
#     p___.ap..(p__)
#     print("PATHS:", ?
#     ? r...l, p__ + |r...v p..
#     ? r...r, p__ + |r...v p..
#
#
# ___ getthepathofeachnode rootnode
#     nodepaths _    # list
#     appendpath ?,    # list, nodepaths)
#     print('p__ of nodes:', n..
#
# ___ getthepath root val path paths
#     print("r..", r..
#     print("r...data", r...v
#     print("val", ?
#     print("p__", p__)
#     print("paths", ?
#
#     __ no. r..
#         r_ F..
#
#     __ no. r...l an. no. r...r
#         __ r...v __ val
#             p__.ap.. r...v
#             p__.ap.. p__
#             r_ T..
#         ____
#             r_ F..
#
#     left _ g.. r...l v.. - r...v, p__ + |r...v p..
#     right _ g.. r...r v.. - r...v, p__ + |r...v p..
#     r_ ? o. ?
#
#
# ___ checkwhetherpathhassum root val
#     paths _    # list
#     g.. r.. ?    # list, paths)
#     print('sum:', ?
#     print('paths:' ?
#
#
# ___ sumOfNodes root
#     items _    # list
#     count _ 0
#     i__.i.. count, r..
#     sum _ 0
#     w__ i__ !_    # list:
#         temp _ i__.p..
#         s.. +_ t__.v
#         __ t__.l !_ N..
#             i__.i.. 0 t__.l
#         __ t__.r !_ N..
#             i__.i.. 0 t__.r
#         ___ p __ i__: print(p.v)
#         print("####")
#
#     print("Total sum of all nodes is " ?
#
#


#     3
# 0     4
#   2      8
# tree = binTree()
# tree.addnode(3)
# tree.addnode(4)
# tree.addnode(0)
# tree.addnode(-1)
# tree.addnode(8)
# tree.addnode(2)
# tree.addnode(3.5)
#tree.addnode(10)
# tree.printFullTree()
#print (tree.findnode(3)).v
#print tree.findnode(10)
#tree.deleteTree()
#tree.printFullTree()
#print "CHECK WHETHER IT'S A BINARY TREE"
#print(checkwhetheritsabintree(tree.root))
#levelOrder(tree.root)
#print(findsize(tree.root))
#printReverse(tree.root)
#print(maximumDepthOfTree(tree.root))
#deepestNode(tree.root)
#countLeaves(tree.root)
#countFullNodes(tree.root)
#countHalfNodes(tree.root)
#print(diaTree(tree.root))
#getthepathofeachnode(tree.root)
#print "check whether the path has sum" 
#checkwhetherpathhassum(tree.root,7)
#sumOfNodes(tree.root)
