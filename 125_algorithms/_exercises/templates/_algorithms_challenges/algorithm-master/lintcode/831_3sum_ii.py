class Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    ___ threeSum2(self, n):
        ans = 0
        nums    # list

        ___ a __ r..(n + 1):
            __ a * a > n:
                break
            nums.a..(a * a)
            nums.a..(a * a)
            nums.a..(a * a)

        m = l..(nums)

        ___ a __ r..(m - 2):
            __ a > 0 and nums[a] __ nums[a - 1]:
                continue

            b = a + 1
            c = m - 1
            while b < c:
                _sum = nums[a] + nums[b] + nums[c]
                __ _sum < n:
                    b += 1
                ____ _sum > n:
                    c -= 1
                ____:
                    ans += 1
                    b += 1
                    c -= 1
                    while b < c and nums[b] __ nums[b - 1]:
                        b += 1
                    while b < c and nums[c] __ nums[c + 1]:
                        c -= 1

        r.. ans


class Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    ___ threeSum2(self, n):
        ans = 0
        m = int(n ** 0.5)

        ___ a __ r..(m + 1):
            target = n - a * a
            b, c = a, m
            while b <= c:
                _sum = b * b + c * c
                __ _sum < target:
                    b += 1
                ____ _sum > target:
                    c -= 1
                ____:
                    ans += 1
                    b += 1

        r.. ans
