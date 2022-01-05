c_ Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    ___ threeSum2  n):
        ans = 0
        nums    # list

        ___ a __ r..(n + 1):
            __ a * a > n:
                _____
            nums.a..(a * a)
            nums.a..(a * a)
            nums.a..(a * a)

        m = l..(nums)

        ___ a __ r..(m - 2):
            __ a > 0 a.. nums[a] __ nums[a - 1]:
                _____

            b = a + 1
            c = m - 1
            w.... b < c:
                _sum = nums[a] + nums[b] + nums[c]
                __ _sum < n:
                    b += 1
                ____ _sum > n:
                    c -= 1
                ____:
                    ans += 1
                    b += 1
                    c -= 1
                    w.... b < c a.. nums[b] __ nums[b - 1]:
                        b += 1
                    w.... b < c a.. nums[c] __ nums[c + 1]:
                        c -= 1

        r.. ans


c_ Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    ___ threeSum2  n):
        ans = 0
        m = i..(n ** 0.5)

        ___ a __ r..(m + 1):
            target = n - a * a
            b, c = a, m
            w.... b <= c:
                _sum = b * b + c * c
                __ _sum < target:
                    b += 1
                ____ _sum > target:
                    c -= 1
                ____:
                    ans += 1
                    b += 1

        r.. ans
