'''
Created on May 9, 2018

@author: tongq
'''
c_ TreeNode(o..
    ___ - , start, end, sumVal=0
        sumVal = sumVal
        start = start
        end = end
        left = N..
        right = N..

c_ NumArray(o..

    ___ - , nums
        """
        :type nums: List[int]
        """
        __ n.. nums:
            root = N..
        ____
            root = buildTree(nums, 0, l..(nums)-1)
    
    ___ buildTree  nums, i, j
        __ n.. nums o. i > j:
            r.. N..
        __ i __ j:
            r.. TreeNode(i, j, nums[i])
        root = TreeNode(i, j, -1)
        mid = (i+j)//2
        root.left = buildTree(nums, i, mid)
        root.right = buildTree(nums, mid+1, j)
        root.sumVal = root.left.sumVal+root.right.sumVal
        r.. root

    ___ update  i, val
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        updateHelper(root, i, val)
    
    ___ updateHelper  root, i, val
        __ n.. root: r..
        __ i __ root.start a.. i __ root.end:
            root.sumVal = val
            r..
        mid = (root.start+root.end)//2
        __ i <= mid:
            updateHelper(root.left, i, val)
        ____
            updateHelper(root.right, i, val)
        root.sumVal = root.left.sumVal+root.right.sumVal
    
    ___ sumRange  i, j
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        r.. sumRangeHelper(root, i, j)
    
    ___ sumRangeHelper  root, i, j
        __ n.. root o. i > j o. j < root.start o. i > root.end:
            r.. 0
        __ i __ root.start a.. j __ root.end:
            r.. root.sumVal
        mid = (root.start+root.end)//2
        res = sumRangeHelper(root.left, i, m..(j, mid+\
            sumRangeHelper(root.right, m..(i, mid+1), j)
        r.. res
