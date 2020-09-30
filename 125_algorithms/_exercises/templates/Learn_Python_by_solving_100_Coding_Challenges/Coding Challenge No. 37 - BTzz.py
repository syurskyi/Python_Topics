# Return binary zigzag level order traversal
# Question: Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# For example: Given binary tree {3,9,20,#,#,15,7},
# 3
# / \
# 9 20
# / \
# 15 7
# return its zigzag level order traversal as:
# [ [3], [20,9], [15,7] ]
# Solutions:


c_ TreeNode:
    ___  -(self, x):
        val _ x
        left _ N..
        right _ N..


c_ Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    ___ zigzagLevelOrder(self, root):
        solution _   # list
        thisLevel _  # list
        __ root !_ N..:
            thisLevel.ap..(root)
        leftToRight _ T..
        while le.(thisLevel)>0:
            levelSolution _   # list
            nextLevel _   # list
            while le.(thisLevel)>0:
                node _ thisLevel.p..()
                levelSolution.ap..(node.val)
                __ leftToRight:
                    __ node.left !_ N..:
                        nextLevel.ap..(node.left)
                    __ node.right !_ N..:
                        nextLevel.ap..(node.right)
                ____
                    __ node.right !_ N..:
                        nextLevel.ap..(node.right)
                    __ node.left !_ N..:
                        nextLevel.ap..(node.left)
            thisLevel _ nextLevel
            solution.ap..(levelSolution)
            leftToRight _ no. leftToRight
        r_ solution


__  -n __ '__main__':
    BT, BT.left, BT.right, BT.right.left, BT.right.right _ TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
    print ( Solution().zigzagLevelOrder(BT) )