class Solution:
    """
    REF: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/
    """
    ___ countSmaller(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ not nums:
            r_ []

        n = le.(nums)
        ans = [0] * n

        cands = sorted(set(nums))
        v2i = {cands[i]: i ___ i in range(le.(cands))}
        self.bits = [0] * (le.(v2i) + 1)

        ___ i in range(n - 1, -1, -1
            j = v2i[nums[i]]
            ans[i] = self.su.(j)
            self.update(j)

        r_ ans

    ___ update(self, i
        i += 1

        w___ i < le.(self.bits
            self.bits[i] += 1
            i += (i & -i)

    ___ su.(self, i
        res = 0

        w___ i > 0:
            res += self.bits[i]
            i -= (i & -i)

        r_ res


class Solution:
    """
    Brute Force: TLE
    """
    ___ countSmaller(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        __ not nums:
            r_ ans

        n = le.(nums)

        ___ i in range(n
            ans.append(0)

            ___ j in range(i, n
                __ nums[j] < nums[i]:
                    ans[-1] += 1

        r_ ans
