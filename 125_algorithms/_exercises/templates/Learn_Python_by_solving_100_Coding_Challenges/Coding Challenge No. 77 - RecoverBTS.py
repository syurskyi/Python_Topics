# Recover Binary Search Tree
# Question: Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.
# Note: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# Solutions:


class TreeNode:
    ___ __init__(self, x):
        self.val _ x
        self.left _ N..
        self.right _ N..


class Solution:
    # @param root, a tree node
    # @return a tree node
    ___ FindTwoNodes(self, root):
        __ root:
            self.FindTwoNodes(root.left)
            __ self.prev an. self.prev.val > root.val:
                self.n2 _ root
                __ self.n1 __ N..:
                    self.n1 _ self.prev
                self.prev _ root
                self.FindTwoNodes(root.right)

    ___ recoverTree(self, root):
        self.n1 _ self.n2 _ N..
        self.prev _ N..
        self.FindTwoNodes(root)
        self.n1.val, self.n2.val _ self.n2.val, self.n1.val
        r_ root