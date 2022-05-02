c_ Solution o..
    ___ nextPermutation  nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ls = l.. nums)
        __ ls <= 1:
            r_
        pair =    # list
        ___ i __ r.. ls):
            ___ j __ r.. i + 1, ls):
                # append ascending order pair
                __ nums[i] < nums[j]:
                    pair.append([i,j])
        pos = 0
        __ l.. pair) > 0:
            swap(nums, pair[-1][0], pair[-1][1])
            pos = pair[-1][0] + 1
        # sort from pos
        ___ i __ r.. pos, ls):
            ___ j __ r.. i + 1, ls):
                __ nums[i] > nums[j]:
                    swap(nums, i, j)

    ___ swap  nums, index1, index2):
        __ index1 __ index2:
            r_
        nums[index1], nums[index2] = nums[index2], nums[index1]

    # def nextPermutation(self, nums):
    #     # https://leetcode.com/discuss/86630/fast-and-easy-python-solution-beaten-79%25
    #     pos = -1
    #     ls = len(nums)
    #     for i in range(ls - 1, 0, -1):
    #         if nums[i] > nums[i - 1]:
    #             pos = i - 1
    #             break
    #     if pos == -1:
    #         self.re_order(nums, 0, ls - 1)
    #         return
    #     for i in range(ls - 1, -1, -1):
    #         if nums[pos] < nums[i]:
    #             nums[pos], nums[i] = nums[i], nums[pos]
    #             self.re_order(nums, pos + 1, ls - 1)
    #             break
    #
    # def re_order(self, a, start, end):
    #     for i in range(0, (end - start + 1) // 2):
    #         a[start + i], a[end - i] = a[end - i], a[start + i]




