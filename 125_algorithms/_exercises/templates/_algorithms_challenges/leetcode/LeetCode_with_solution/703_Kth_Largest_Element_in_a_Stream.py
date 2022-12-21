c_ KthLargest o..

    ___ -  k, nums
        nums = nums
        k = k
        # build min heap
        heapq.heapify(nums)
        # remove n - k smallest number
        w.. l.. nums) > k:
            heapq.heappop(nums)

    ___ add  val
        # add to heaq if it's less then k
        __ l.. nums) < k:
            heapq.heappush(nums, val)
        ____ val > nums[0]:
            # if len(heaq) == k, and val greater than smallest num
            # then pop smallest num than add val to heap
            heapq.heapreplace(nums, val)
        # return k largest
        r_ nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
