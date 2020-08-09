'''
Created on May 9, 2017

@author: MT
'''

class Node(object
    ___ __init__(self, val
        self.val = val
        self.less = 0
        self.same = 1
        self.left = None
        self.right = None

class Solution(object
    ___ reversePairs_mergeSort(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cnt = 0
        ___ msort(lst
            n = le.(lst)
            __ n <= 1:
                r_ lst
            ____
                r_ merger(msort(lst[:int(n/2)]), msort(lst[int(n/2]))
        ___ merger(left, right
            l, r = 0, 0
            w___ l < le.(left) and r < le.(right
                __ left[l] <= 2*right[r]:
                    l += 1
                ____
                    self.cnt += le.(left)-l
                    r += 1
            r_ sorted(left+right)
        msort(nums)
        r_ self.cnt
    
    ___ reversePairs(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        root = None
        cnt = [0]
        ___ i in range(le.(nums)-1, -1, -1
            num = nums[i]
            self.search(cnt, root, num/2.0)
            root = self.build(num, root)
        r_ cnt[0]
    
    ___ search(self, cnt, node, target
        __ not node:
            r_
        ____ target __ node.val:
            cnt[0] += node.less
        ____ target < node.val:
            self.search(cnt, node.left, target)
        ____
            cnt[0] += node.less + node.same
            self.search(cnt, node.right, target)
    
    ___ build(self, val, node
        __ not node:
            r_ Node(val)
        ____ val __ node.val:
            node.same += 1
        ____ val > node.val:
            node.right = self.build(val, node.right)
        ____
            node.less += 1
            node.left = self.build(val, node.left)
        r_ node
    
    ___ test(self
        testCases = [
            [1, 3, 2, 3, 1],
            [2, 4, 3, 5, 1],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.reversePairs_mergeSort(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
