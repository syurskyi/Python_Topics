'''
Created on May 9, 2017

@author: MT
'''

c_ Node(o..
    ___ - , val
        val val
        less 0
        same 1
        left N..
        right N..

c_ Solution(o..
    ___ reversePairs_mergeSort  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt 0
        ___ msort(lst
            n l..(lst)
            __ n <_ 1:
                r.. ?
            ____
                r.. merger(msort(lst[:i..(n/2)]), msort(lst[i..(n/2]
        ___ merger(left, right
            l, r 0, 0
            w.... l < l..(left) a.. r < l..(right
                __ left[l] <_ 2*right[r]:
                    l += 1
                ____
                    cnt += l..(left)-l
                    r += 1
            r.. s..(left+right)
        msort(nums)
        r.. cnt
    
    ___ reversePairs  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        root N..
        cnt [0]
        ___ i __ r..(l..(nums)-1, -1, -1
            num nums[i]
            s..(cnt, root, num/2.0)
            root build(num, root)
        r.. cnt[0]
    
    ___ s..  cnt, node, target
        __ n.. node:
            r..
        ____ target __ node.val:
            cnt[0] += node.less
        ____ target < node.val:
            s..(cnt, node.left, target)
        ____
            cnt[0] += node.less + node.same
            s..(cnt, node.right, target)
    
    ___ build  val, node
        __ n.. node:
            r.. Node(val)
        ____ val __ node.val:
            node.same += 1
        ____ val > node.val:
            node.right build(val, node.right)
        ____
            node.less += 1
            node.left build(val, node.left)
        r.. node
    
    ___ test
        testCases [
            [1, 3, 2, 3, 1],
            [2, 4, 3, 5, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result reversePairs_mergeSort(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
