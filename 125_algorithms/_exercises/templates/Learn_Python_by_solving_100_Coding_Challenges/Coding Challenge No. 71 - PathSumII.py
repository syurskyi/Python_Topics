# Path Sum II
# Question: Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
# 5
# / \
# 4 8
# / / \
# 11 13 4
# / \ / \
# 7 2 5 1
# return
# [ [5,4,11,2], [5,8,4,5] ]
# Solutions:


class TreeNode:
    ___ __init__(self, x):
        self.val _ x
        self.left _ N..
        self.right _ N..


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    ___ pathSum(self, root, su.):
        solution _   # list
        self.pathSumRec(root, su., 0,   # list, solution)
        r_ solution

    ___ pathSumRec(self, root, su., tempSum, tempList, solution):
        __ root __ N..:
            r_
        tempList.ap..(root.val)
        tempSum +_ root.val
        __ root.left __ N.. an. root.right __ N..:
            __ tempSum __ su.:
                solution.ap..(li..(tempList))
            ____
                self.pathSumRec(root.left, su., tempSum, tempList, solution)
                self.pathSumRec(root.right, su., tempSum, tempList, solution)
        tempList.p..()


__  -n __ '__main__':
    BT, BT.right, BT.right.left, BT.left _ TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(10)
    print ( Solution().pathSum(BT, 6) )