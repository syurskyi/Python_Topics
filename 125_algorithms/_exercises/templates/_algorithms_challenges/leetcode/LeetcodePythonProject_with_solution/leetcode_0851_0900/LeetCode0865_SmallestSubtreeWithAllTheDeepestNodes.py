'''
Created on Sep 29, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        r.. self.deep(root)[1]
    
    ___ deep(self, root):
        __ n.. root:
            r.. 0, N..
        l, r = self.deep(root.left), self.deep(root.right)
        __ l[0] > r[0]:
            r.. l[0]+1, l[1]
        ____ l[0] < r[0]:
            r.. r[0]+1, r[1]
        ____:
            r.. l[0]+1, root
    
    ___ subtreeWithAllDeepest_own_twoPass(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        hashmap = {}
        self.gatherDepths(root, 0, hashmap)
        maxDepth = max(hashmap.keys())
        nodes = hashmap[maxDepth]
        r.. self.getCommonParent(root, nodes)
    
    ___ gatherDepths(self, root, depth, hashmap):
        __ n.. root:
            r..
        __ depth __ hashmap:
            hashmap[depth].a..(root)
        ____:
            hashmap[depth] = [root]
        self.gatherDepths(root.left, depth+1, hashmap)
        self.gatherDepths(root.right, depth+1, hashmap)
    
    ___ getCommonParent(self, root, nodes):
        __ n.. root:
            r.. N..
        isLeft = True
        ___ node __ nodes:
            __ n.. self.isSubTree(root.left, node):
                isLeft = False
                break
        __ isLeft:
            r.. self.getCommonParent(root.left, nodes)
        isRight = True
        ___ node __ nodes:
            __ n.. self.isSubTree(root.right, node):
                isRight = False
                break
        __ isRight:
            r.. self.getCommonParent(root.right, nodes)
        ____:
            r.. root
    
    ___ isSubTree(self, root, node):
        __ n.. root:
            r.. False
        __ root __ node:
            r.. True
        __ self.isSubTree(root.left, node) o. self.isSubTree(root.right, node):
            r.. True

__ __name__ __ '__main__':
    Solution().test()
