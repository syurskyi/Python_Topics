"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

将一个数组洗牌。

直接用 random.sample 即可。

sample 中的算法直接用了 set() 以及无限从数组下标中选择然后判断是否在set中...有点无脑。

在后面的例子中看到一种非常有趣的：

sorted 可以指定key，把这个key指定为 random.random()即可。

测试地址：
https://leetcode.com/problems/shuffle-an-array/description/

平均 beat 30% 左右。

用 sample 完全取决于运气，因为底层的源码就是取决于运气的...

"""
import random

c.. Solution o..

    ___ __init__  nums
        """
        :type nums: List[int]
        """
        self.nums = nums

    ___ reset(self
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        r_ self.nums

    ___ shuffle(self
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        r_ random.sample(self.nums, l..(self.nums))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
