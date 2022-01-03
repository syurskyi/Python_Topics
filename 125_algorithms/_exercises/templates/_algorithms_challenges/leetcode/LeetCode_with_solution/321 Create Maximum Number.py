"""
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <=
m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array
of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
"""
__author__ = 'Daniel'


c_ SolutionTLE(object):
    ___ maxNumber(self, nums1, nums2, k):
        """
        http://algobox.org/2015/12/24/create-maximum-number/
        O(kN(N+M))
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxa    # list
        n1, n2 = l..(nums1), l..(nums2)
        ___ l1 __ xrange(m..(n1, k)+1):
            l2 = k - l1
            ... l2 >= 0
            A1, A2 = maxNumberSingle(nums1, l1), maxNumberSingle(nums2, l2)
            cur = maxNumberDual(A1, A2)
            __ n.. maxa o. eval(maxa) < eval(cur):
                maxa = cur

        r.. maxa

    ___ eval(self, lst):
        r.. int("".j..(map(s.., lst)))

    ___ maxNumberSingle(self, A, k):
        """
        maxNumber of k elements from a single list A
        """
        stk    # list
        n = l..(A)
        ___ i __ xrange(n):
            w.... stk a.. l..(stk)-1+(n-1-i+1) >= k a.. stk[-1] < A[i]: stk.pop()
            __ l..(stk) < k:
                stk.a..(A[i])

        r.. stk

    ___ maxNumberDual(self, A1, A2):
        """
        maxNumber of all elements from dual lists A1 and A2.
        """
        ret    # list
        p1, p2 = 0, 0
        w.... p1 < l..(A1) a.. p2 < l..(A2):
            ahead1, ahead2 = p1, p2
            w.... ahead1 < l..(A1) a.. ahead2 < l..(A2) a.. A1[ahead1] __ A2[ahead2]:
                ahead1, ahead2 = ahead1+1, ahead2+1

            __ ahead2 >= l..(A2) o. (ahead1 < l..(A1) a.. A1[ahead1] > A2[ahead2]):
                ret.a..(A1[p1])
                p1 += 1
            ____:
                ret.a..(A2[p2])
                p2 += 1

        # dangling
        ret.extend(A1[p1:])
        ret.extend(A2[p2:])
        r.. ret
