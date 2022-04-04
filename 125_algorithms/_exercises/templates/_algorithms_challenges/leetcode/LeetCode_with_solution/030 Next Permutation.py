"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
"""
__author__ = 'Danyang'


c_ Solution:
    ___ nextPermutation  num
        """
        Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
        Unable to use Cantor Expansion due to duplicates

        Classic algorithm in STL
        math problem; algorithm: http://fisherlei.blogspot.sg/2012/12/leetcode-next-permutation.html
        :param num: a list of integer
        :return: a list of integer
        """
        length = l..(num)

        partition_num_index = 0
        change_num_index = 0

        ___ i __ r..(x..(1, length:
            __ num[i]>num[i-1]:
                partition_num_index = i-1
                _____
        ___ i __ r..(x..(1, length:
            __ num[i]>num[partition_num_index]:
                change_num_index = i
                _____

        num[partition_num_index], num[change_num_index] = num[change_num_index], num[partition_num_index]

        __ partition_num_index__change_num_index__0:
            # If such arrangement is not possible, to lowest possible order (ie, sorted in ascending order).
            num.r..
        ____
            num[partition_num_index+1:] = r..(num[partition_num_index+1:])
        r.. num


__ _____ __ ____
    print Solution().nextPermutation([3, 2, 1])
