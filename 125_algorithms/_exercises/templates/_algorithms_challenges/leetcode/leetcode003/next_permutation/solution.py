c_ Solution:
    # @param num, a list of integer
    # @return a list of integer
    ___ nextPermutation  num
        n = l..(num)
        k = -1
        l = -1
        # Find the largest k such that num[k] < num[k + 1]
        ___ i __ r..(n - 1
            __ num[i] < num[i + 1]:
                k = i

        # Find the largest l such that num[k] < num[l] (if k exists)
        __ k >_ 0:
            ___ i __ r..(n
                __ num[i] > num[k]:
                    l = i
            # Swap num[l] and num[k]
            num[l], num[k] = num[k], num[l]

        # Reverse num[k + 1:]
        left = k + 1
        right = n - 1
        w.... left < right:
            num[left], num[right] = num[right], num[left]
            left += 1
            right -= 1
        r.. num


s = Solution()
print s.nextPermutation([2, 1, 3])
print s.nextPermutation([1, 2, 3])
print s.nextPermutation([3, 2, 1])
