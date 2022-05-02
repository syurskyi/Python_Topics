'''
Created on Mar 15, 2017

@author: MT
'''

c_ TreeNode(o..
    ___ - , val, num=1
        val val
        num num
        left N..
        right N..
    
    ___ -s
        r.. '<val: %s, num: %s>' % (val, num)
    
    ___  -r
        r.. -s()

c_ Solution(o..
    ___ countSmaller  nums
        __ n.. nums: r..    # list
        root TreeNode(nums[-1])
        result [0]
        ___ i __ r..(l..(nums)-2, -1, -1
            result.i.. 0, getVal(root, nums[i], 0
        r.. result, root
    
    ___ getVal  root, val, num
        __ root.val >_ val:
            root.num += 1
            __ n.. root.left:
                root.left TreeNode(val)
                r.. num
            ____
                r.. getVal(root.left, val, num)
        ____
            num += root.num
            __ n.. root.right:
                root.right TreeNode(val)
                r.. num
            ____
                r.. getVal(root.right, val, num)
    
    ___ test
        testCases [
            [5, 2, 6, 1],
            [-1, -1],
            [3, 2, 2, 6, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result, root countSmaller(nums)
            print('result: %s' % (result
            print('-='*20+'-')
            
            queue= [root]
            line    # list
            nextQueue    # list
            w.... queue:
                node queue.p.. 0)
                line.a..(node)
                __ node.left:
                    nextQueue.a..(node.left)
                __ node.right:
                    nextQueue.a..(node.right)
                __ n.. queue:
                    queue nextQueue
                    nextQueue    # list
                    print(line)
                    line    # list
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

