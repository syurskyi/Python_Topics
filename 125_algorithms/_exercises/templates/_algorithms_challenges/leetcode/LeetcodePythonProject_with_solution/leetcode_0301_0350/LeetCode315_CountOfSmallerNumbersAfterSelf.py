'''
Created on Mar 15, 2017

@author: MT
'''

class TreeNode(object):
    ___ __init__(self, val, num=1):
        self.val = val
        self.num = num
        self.left = N..
        self.right = N..
    
    ___ __str__(self):
        r.. '<val: %s, num: %s>' % (self.val, self.num)
    
    ___ __repr__(self):
        r.. self.__str__()

class Solution(object):
    ___ countSmaller(self, nums):
        __ n.. nums: r.. []
        root = TreeNode(nums[-1])
        result = [0]
        ___ i __ r..(l..(nums)-2, -1, -1):
            result.insert(0, self.getVal(root, nums[i], 0))
        r.. result, root
    
    ___ getVal(self, root, val, num):
        __ root.val >= val:
            root.num += 1
            __ n.. root.left:
                root.left = TreeNode(val)
                r.. num
            ____:
                r.. self.getVal(root.left, val, num)
        ____:
            num += root.num
            __ n.. root.right:
                root.right = TreeNode(val)
                r.. num
            ____:
                r.. self.getVal(root.right, val, num)
    
    ___ test(self):
        testCases = [
            [5, 2, 6, 1],
            [-1, -1],
            [3, 2, 2, 6, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result, root = self.countSmaller(nums)
            print('result: %s' % (result))
            print('-='*20+'-')
            
            queue= [root]
            line    # list
            nextQueue    # list
            w.... queue:
                node = queue.pop(0)
                line.a..(node)
                __ node.left:
                    nextQueue.a..(node.left)
                __ node.right:
                    nextQueue.a..(node.right)
                __ n.. queue:
                    queue = nextQueue
                    nextQueue    # list
                    print(line)
                    line    # list
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

