'''
Created on Sep 29, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ subtreeWithAllDeepest(self, root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        r_ self.deep(root)[1]
    
    ___ deep(self, root
        __ not root:
            r_ 0, None
        l, r = self.deep(root.left), self.deep(root.right)
        __ l[0] > r[0]:
            r_ l[0]+1, l[1]
        ____ l[0] < r[0]:
            r_ r[0]+1, r[1]
        ____
            r_ l[0]+1, root
    
    ___ subtreeWithAllDeepest_own_twoPass(self, root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        hashmap = {}
        self.gatherDepths(root, 0, hashmap)
        maxDepth = max(hashmap.keys())
        nodes = hashmap[maxDepth]
        r_ self.getCommonParent(root, nodes)
    
    ___ gatherDepths(self, root, depth, hashmap
        __ not root:
            r_
        __ depth in hashmap:
            hashmap[depth].append(root)
        ____
            hashmap[depth] = [root]
        self.gatherDepths(root.left, depth+1, hashmap)
        self.gatherDepths(root.right, depth+1, hashmap)
    
    ___ getCommonParent(self, root, nodes
        __ not root:
            r_ None
        isLeft = True
        ___ node in nodes:
            __ not self.isSubTree(root.left, node
                isLeft = False
                break
        __ isLeft:
            r_ self.getCommonParent(root.left, nodes)
        isRight = True
        ___ node in nodes:
            __ not self.isSubTree(root.right, node
                isRight = False
                break
        __ isRight:
            r_ self.getCommonParent(root.right, nodes)
        ____
            r_ root
    
    ___ isSubTree(self, root, node
        __ not root:
            r_ False
        __ root __ node:
            r_ True
        __ self.isSubTree(root.left, node) or self.isSubTree(root.right, node
            r_ True

__ __name__ __ '__main__':
    Solution().test()
