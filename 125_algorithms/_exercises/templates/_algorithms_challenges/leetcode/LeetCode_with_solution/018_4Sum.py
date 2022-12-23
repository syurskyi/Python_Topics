# class Solution(object):
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """


c_ Solution o..
    ___ fourSum  nums, target
        sort_nums = s..(nums)
        ls = l.. nums)
        res  # dict
        pairs  # dict
        ___ i __ r.. ls - 3
            ___ j __ r.. i + 1, ls - 2
                res_2 = sort_nums[i] + sort_nums[j]
                try:
                    pairs[target - res_2].a.. [i, j])
                except KeyError:
                    pairs[target - res_2] = [[i, j]]
        ___ key, temp __ pairs.items(
            ___ pair __ temp:
                j = pair[1] + 1
                k = ls - 1
                w.. j < k:
                    current = sort_nums[j] + sort_nums[k]
                    __ current __ key:
                        result = (sort_nums[pair[0]], sort_nums[pair[1]], sort_nums[j], sort_nums[k])
                        res[result] = T..
                        j += 1
                    ____ current < key:
                        j += 1
                    ____
                        k -= 1
        r_ res.keys()

    # def fourSum(self, nums, target):
    #     # https://leetcode.com/discuss/89989/why-is-python-o-n-3-tle
    #     index_pairs = dict()
    #     combos = dict()
    #     n = len(nums)
    #     for i in range(0,n):
    #         for j in range(i+1,n):
    #             sum = nums[i] + nums[j]
    #             if index_pairs.get(target - sum) is not None:
    #                 for pair in index_pairs[target - sum]:
    #                     if i != pair[0] and i != pair[1] and j != pair[0] and j != pair[1]: # Avoid overuse
    #                         combo = sorted((nums[i], nums[j], nums[pair[0]], nums[pair[1]])) # Avoid duplicate
    #                         combos[tuple(combo)] = True
    #             if index_pairs.get(sum) is not None:
    #                 index_pairs[sum].append((i,j))
    #             else:
    #                 index_pairs[sum] = [(i,j)]
    #     return combos.keys()

__ ____ __ ____
    # begin
    s  ?
    print s.fourSum([0, 0, 0, 0], 0)