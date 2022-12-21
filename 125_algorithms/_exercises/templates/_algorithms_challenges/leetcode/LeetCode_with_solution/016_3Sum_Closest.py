# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
c_ Solution o..
    ___ threeSumClosest  nums, target
        ls = l.. nums)
        sort_nums = s..(nums)
        res = nums[0] + nums[1] + nums[2]
        ___ i __ r.. ls - 2
            j, k = i + 1, ls - 1
            w.. j < k:
                temp = sort_nums[i] + sort_nums[j] + sort_nums[k]
                __ abs(target - temp) < abs(target - res
                    res = temp
                __ temp < target:
                    j += 1
                ____
                    k -= 1
        r_ res


