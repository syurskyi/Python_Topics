# Recover Binary Search Tree
# Question: Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.
# Note: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# Solutions:


c_ TreeNode:
    ___  -(self, x):
        val _ x
        left _ N..
        right _ N..


c_ Solution:
    # @param root, a tree node
    # @return a tree node
    ___ FindTwoNodes(self, root):
        __ root:
            FindTwoNodes(root.left)
            __ prev an. prev.val > root.val:
                n2 _ root
                __ n1 __ N..:
                    n1 _ prev
                prev _ root
                FindTwoNodes(root.right)

    ___ recoverTree(self, root):
        n1 _ n2 _ N..
        prev _ N..
        FindTwoNodes(root)
        n1.val, n2.val _ n2.val, n1.val
        r_ root