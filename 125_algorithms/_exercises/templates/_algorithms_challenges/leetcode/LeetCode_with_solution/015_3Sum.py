
c_ Solution o..
    # def threeSum(self, nums):
    #     # skip duplicate
    #     # O(n^3)
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()
    #     ls = len(nums)
    #     result = []
    #     for i in range(0, ls - 2):
    #         if nums[i] > 0:
    #             break
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         j = i + 1
    #         k = ls - 1
    #         while(j < k):
    #             temp = [nums[i], nums[j], nums[k]]
    #             s = sum(temp)
    #             jtemp = nums[j]
    #             ktemp = nums[k]
    #             if s <= 0:
    #                 j += 1
    #                 while(j < k and jtemp == nums[j]):
    #                     j += 1
    #                 if s == 0:
    #                     result.append(temp)
    #             else:
    #                 k -= 1
    #                 while(j < k and ktemp == nums[k]):
    #                     k -= 1
    #     return result
    # def threeSum(self, nums):
    #     """
    #         :type nums: List[int]
    #         :rtype: List[List[int]]
    #     """
    #     # using multiple 2 sum
    #     nums.sort()
    #     result, visited = set(), {}
    #     for i in xrange(len(nums) - 2):
    #         table, target = {}, -nums[i]
    #         if nums[i] not in visited:
    #             for j in xrange(i + 1, len(nums)):
    #                 if nums[j] not in table:
    #                     table[target - nums[j]] = j
    #                 else:
    #                     result.add((nums[i], target - nums[j], nums[j]))
    #             visited[nums[i]] = 1
    #     return list(result)

    ___ threeSum  nums
        res =    # list
        nums.s..
        ls = l.. nums)
        ___ i __ r.. ls - 2
            __ i > 0 a.. nums[i] __ nums[i - 1]:
                c_
            j = i + 1
            k = ls - 1
            w.. j < k:
                curr = nums[i] + nums[j] + nums[k]
                __ curr __ 0:
                    res.append([nums[i], nums[j], nums[k]])
                    w.. j < k a.. nums[j] __ nums[j + 1]:
                        j += 1
                    w.. j < k a.. nums[k] __ nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                ____ curr < 0:
                    j += 1
                ____
                    k -= 1
        r_ res
