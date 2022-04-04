
c_ Solution(o..
    ___ wiggleSort  nums
        median = kthLargestElement(nums, (l..(nums)+1)//2)
        n = l..(nums)
        left = 0
        i = 0
        right = n-1
        w.... i <= right:
            __ nums[newIndex(i, n)] > median:
                nums[newIndex(left, n)], nums[newIndex(i, n)] =\
                nums[newIndex(i, n)], nums[newIndex(left, n)]
                left += 1
                i += 1
            ____ nums[newIndex(i, n)] < median:
                nums[newIndex(right, n)], nums[newIndex(i, n)] =\
                nums[newIndex(i, n)], nums[newIndex(right, n)]
                right -= 1
            ____
                i += 1
    
    ___ newIndex  index, n
        r.. (1+2*index)%(n|1)
    
    ___ kthLargestElement  nums, k
        shuffle(nums)
        lo = 0
        hi = l..(nums)-1
        k = l..(nums)-k
        w.... lo < hi:
            j = partition(nums, lo, hi)
            __ j < k:
                lo = j+1
            ____ j > k:
                hi = j-1
            ____
                _____
        r.. nums[k]
    
    ___ partition  nums, lo, hi
        i, j = lo+1, hi
        w... T...
            w.... i < hi a.. nums[i] <= nums[lo]:
                i += 1
            w.... j > lo a.. nums[lo] <= nums[j]:
                j -= 1
            __ i >= j:
                _____
            nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[j] = nums[j], nums[lo]
        r.. j
    
    ___ shuffle  nums
        _______ r__
        ___ i __ r..(l..(nums)-1, 0, -1
            ind = r__.randint(0, i)
            nums[i], nums[ind] = nums[ind], nums[i]
    
    ___ wiggleSortWithSorting  nums
        nums.s..()
        half = l..(nums[::2])-1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
    
    ___ test
        testCases = [
            [1, 5, 1, 1, 6, 4],
            [1, 3, 2, 2, 3, 1],
            [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            wiggleSort(nums)
            print('sorted: %s' % (nums
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
