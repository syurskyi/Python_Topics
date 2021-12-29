class Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    ___ threeSum2(self, n):
        ans = 0
        nums = []

        for a in range(n + 1):
            __ a * a > n:
                break
            nums.append(a * a)
            nums.append(a * a)
            nums.append(a * a)

        m = len(nums)

        for a in range(m - 2):
            __ a > 0 and nums[a] == nums[a - 1]:
                continue

            b = a + 1
            c = m - 1
            while b < c:
                _sum = nums[a] + nums[b] + nums[c]
                __ _sum < n:
                    b += 1
                elif _sum > n:
                    c -= 1
                else:
                    ans += 1
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1

        return ans


class Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    ___ threeSum2(self, n):
        ans = 0
        m = int(n ** 0.5)

        for a in range(m + 1):
            target = n - a * a
            b, c = a, m
            while b <= c:
                _sum = b * b + c * c
                __ _sum < target:
                    b += 1
                elif _sum > target:
                    c -= 1
                else:
                    ans += 1
                    b += 1

        return ans
