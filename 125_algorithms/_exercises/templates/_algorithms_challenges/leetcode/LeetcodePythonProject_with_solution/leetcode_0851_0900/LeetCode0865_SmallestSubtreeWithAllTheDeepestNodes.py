'''
Created on Sep 29, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.deep(root)[1]
    
    ___ deep(self, root):
        __ not root:
            return 0, None
        l, r = self.deep(root.left), self.deep(root.right)
        __ l[0] > r[0]:
            return l[0]+1, l[1]
        elif l[0] < r[0]:
            return r[0]+1, r[1]
        else:
            return l[0]+1, root
    
    ___ subtreeWithAllDeepest_own_twoPass(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        hashmap = {}
        self.gatherDepths(root, 0, hashmap)
        maxDepth = max(hashmap.keys())
        nodes = hashmap[maxDepth]
        return self.getCommonParent(root, nodes)
    
    ___ gatherDepths(self, root, depth, hashmap):
        __ not root:
            return
        __ depth in hashmap:
            hashmap[depth].append(root)
        else:
            hashmap[depth] = [root]
        self.gatherDepths(root.left, depth+1, hashmap)
        self.gatherDepths(root.right, depth+1, hashmap)
    
    ___ getCommonParent(self, root, nodes):
        __ not root:
            return None
        isLeft = True
        for node in nodes:
            __ not self.isSubTree(root.left, node):
                isLeft = False
                break
        __ isLeft:
            return self.getCommonParent(root.left, nodes)
        isRight = True
        for node in nodes:
            __ not self.isSubTree(root.right, node):
                isRight = False
                break
        __ isRight:
            return self.getCommonParent(root.right, nodes)
        else:
            return root
    
    ___ isSubTree(self, root, node):
        __ not root:
            return False
        __ root == node:
            return True
        __ self.isSubTree(root.left, node) or self.isSubTree(root.right, node):
            return True

__ __name__ == '__main__':
    Solution().test()
