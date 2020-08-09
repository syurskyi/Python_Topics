from heapq ______ heappush, heappop


class Solution:
    """
    @param: nums: an integer array
    @param: k: An integer
    @return: the top k largest numbers in array
    """
    ___ topk(self, nums, k
        """
        min heap (normal case in heapq, max heap needs to times -1)
        """
        __ not nums:
            r_

        ans = []
        for num in nums:
            heappush(ans, num)

            __ le.(ans) > k:
                heappop(ans)

        ans.sort(reverse=True)

        r_ ans
