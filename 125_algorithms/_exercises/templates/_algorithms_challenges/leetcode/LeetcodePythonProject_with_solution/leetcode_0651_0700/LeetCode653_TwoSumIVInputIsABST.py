'''
Created on Oct 4, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ findTarget  root, k
        r.. dfs(root, s..(), k)
    
    ___ dfs  root, hashset, k
        __ n.. root:
            r.. F..
        __ k-root.val __ hashset:
            r.. T..
        hashset.add(root.val)
        r.. dfs(root.left, hashset, k) o.\
            dfs(root.right, hashset, k)
    
    ___ findTargetSpace  root, k
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        __ n.. root: r.. F..
        arr    # list
        stack    # list
        node = root
        w.... node:
            stack.a..(node)
            node = node.left
        w.... stack:
            node = stack.p.. )
            arr.a..(node.val)
            node0 = node.right
            w.... node0:
                stack.a..(node0)
                node0 = node0.left
        i, j = 0, l..(arr)-1
        w.... i < j:
            __ k __ arr[i]+arr[j]:
                r.. T..
            ____ k > arr[i]+arr[j]:
                i += 1
            ____
                j -= 1
        r.. F..
    
    ___ test
        testCases = [
            [
                TreeNode(2, TreeNode(1), TreeNode(3,
                4,
            ],
            [
                TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4, TreeNode(6, N.., TreeNode(7))),
                9
            ],
            [
                TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4, TreeNode(6, N.., TreeNode(7))),
                28,
            ],
        ]
        ___ root, k __ testCases:
            result = findTarget(root, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
