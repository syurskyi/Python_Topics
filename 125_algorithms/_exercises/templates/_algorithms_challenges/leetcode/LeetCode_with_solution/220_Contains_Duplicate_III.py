from collections import OrderedDict
c_ Solution o..
    ___ containsNearbyAlmostDuplicate  nums, k, t
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # https://discuss.leetcode.com/topic/19991/o-n-python-using-buckets-with-explanation-10-lines
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets  # dict
        ___ i, v __ e.. nums
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucketNum, offset = (v / t, 1) __ t ____ (v, 0)
            ___ idx __ xrange(bucketNum - offset, bucketNum + offset + 1
                __ idx __ buckets and abs(buckets[idx] - nums[i]) <= t:
                    r_ T..

            buckets[bucketNum] = nums[i]
            __ l.. buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - k] / t __ t ____ nums[i - k]]

        r_ F..
