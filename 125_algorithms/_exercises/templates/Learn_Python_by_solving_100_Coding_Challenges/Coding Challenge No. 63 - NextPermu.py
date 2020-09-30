# Next Permutation
# Question: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# Solutions:


class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        back = len(num) - 2
        while back >= 0:
            front = len(num) - 1
            while front > back :
                if num[back] < num[front]:
                    # Rule breaker found.
                    num[back], num[front] = num[front], num[back]
                    num[back+1:] = sorted(num[back+1:])
                    return num
                else:
                    front -= 1
            back -= 1
        num.sort()
        return num


Solution().nextPermutation([1,2,3])