# 3 Sum
# Question: Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets.
# Solutions:


c_ Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    ___ threeSum(self, num):
        length _ le.(num)
        result _   # list

        __ length < 3:
            r_ result
        num.sort()

        ___ i __ ra..(length - 2):
            __ i > 0 an. num[i] __ num[i - 1]:
                c..
            low _ i + 1
            high _ length - 1
            target_gap _ 0 - num[i]

            w___ low < high:
                __ num[low] + num[high] < target_gap:
                    low +_ 1
                    w___ low < high an. num[low] __ num[i - 1]:
                        low +_ 1
                ____ num[low] + num[high] > target_gap:
                    high -_ 1
                    w___ low < high an. num[high] __ num[high + 1]:
                        high -_ 1
                ____
                    result.ap..([num[i], num[low], num[high]])
                    low +_ 1
                    w___ low < high an. num[low] __ num[low - 1]:
                        low +_ 1
                    high -_ 1

                w___ low < high an. num[high] __ num[high + 1]:
                    high -_ 1
        r_ result


Solution().threeSum([-1, 0, 1, 2, -1, -4])