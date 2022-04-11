'''
Created on Sep 29, 2019

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x
        val x
        left N..
        right N..

c_ Solution(o..
    ___ subtreeWithAllDeepest  root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        r.. deep(root)[1]
    
    ___ deep  root
        __ n.. root:
            r.. 0, N..
        l, r deep(root.left), deep(root.right)
        __ l[0] > r[0]:
            r.. l[0]+1, l[1]
        ____ l[0] < r[0]:
            r.. r[0]+1, r[1]
        ____
            r.. l[0]+1, root
    
    ___ subtreeWithAllDeepest_own_twoPass  root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        hashmap    # dict
        gatherDepths(root, 0, hashmap)
        maxDepth m..(hashmap.keys
        nodes hashmap[maxDepth]
        r.. getCommonParent(root, nodes)
    
    ___ gatherDepths  root, depth, hashmap
        __ n.. root:
            r..
        __ depth __ hashmap:
            hashmap[depth].a..(root)
        ____
            hashmap[depth] [root]
        gatherDepths(root.left, depth+1, hashmap)
        gatherDepths(root.right, depth+1, hashmap)
    
    ___ getCommonParent  root, nodes
        __ n.. root:
            r.. N..
        isLeft T..
        ___ node __ nodes:
            __ n.. isSubTree(root.left, node
                isLeft F..
                _____
        __ isLeft:
            r.. getCommonParent(root.left, nodes)
        isRight T..
        ___ node __ nodes:
            __ n.. isSubTree(root.right, node
                isRight F..
                _____
        __ isRight:
            r.. getCommonParent(root.right, nodes)
        ____
            r.. root
    
    ___ isSubTree  root, node
        __ n.. root:
            r.. F..
        __ root __ node:
            r.. T..
        __ isSubTree(root.left, node) o. isSubTree(root.right, node
            r.. T..

__ _____ __ _____
    Solution().test()
