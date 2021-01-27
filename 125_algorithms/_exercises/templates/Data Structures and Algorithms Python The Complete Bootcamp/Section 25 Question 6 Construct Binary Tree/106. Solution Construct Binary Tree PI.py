# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ___ buildTree(self, preorder, inorder):
        memory = {}
        ___ i, e __ enumerate(inorder):
            memory[e] = i

        root = self.helper(preorder[::-1], inorder, 0, le.(inorder), memory)
        r_ root

    ___ helper(self, preorder, inorder, leftPointer, rightPointer, memory):
        __ leftPointer >= rightPointer:
            r_ None

        num = preorder.pop()
        root = TreeNode(num)
        idx = memory.get(num)

        root.left = self.helper(preorder, inorder, leftPointer, idx, memory)
        root.right = self.helper(preorder, inorder, idx + 1, rightPointer, memory)

        r_ root