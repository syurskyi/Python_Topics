c_ Solution(o..
    ___ sortArray  nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ n.. nums: r.. nums
        quickSort(0, l..(nums)-1, nums)
        r.. nums

    ___ quickSort  i, j, nums
        __ i < j:
            pi = partition(i, j, nums)
            quickSort(i, pi-1, nums)
            quickSort(pi+1, j, nums)

    ___ partition  low, high, nums
        pivot = nums[high]
        i = low-1
        ___ j __ r..(low, high
            __ nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        r.. i+1

    ___ test
        testCases = [
            [0,3,1,2],
            # [1,1,1,1],
            # [0,1,2,3],
            # [3,2,1,0],
        ]
        ___ nums __ testCases:
            res = sortArray(nums)
            print('res: %s' % res)
            print('-='*30+'-')


__ _____ __ _____
    Solution().test()
