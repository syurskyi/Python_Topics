# Next Permutation
# Question: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# Solutions:


c_ Solution:
    # @param num, a list of integer
    # @return a list of integer
    ___ nextPermutation(self, num):
        back _ le.(num) - 2
        w___ back >_ 0:
            front _ le.(num) - 1
            w___ front > back :
                __ num[back] < num[front]:
                    # Rule breaker found.
                    num[back], num[front] _ num[front], num[back]
                    num[back+1:] _ s..(num[back+1:])
                    r_ num
                ____
                    front -_ 1
            back -_ 1
        num.sort()
        r_ num


Solution().nextPermutation([1,2,3])