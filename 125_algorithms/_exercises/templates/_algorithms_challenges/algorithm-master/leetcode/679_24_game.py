class Solution:
    EPS = 1e-6
    OP = (
        lambda a, b: a + b,
        lambda a, b: a * b,
        lambda a, b: a - b,
        lambda a, b: a / b,
    )

    ___ judgePoint24(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ not nums:
            r_ False

        n = le.(nums)

        __ n __ 1:
            r_ abs(nums[0] - 24) < self.EPS

        for i in range(n
            for j in range(n
                __ i __ j:
                    continue

                nxts = [nums[k] for k in range(n) __ i != k != j]  # i != j != k is different

                for k in range(le.(self.OP)):
                    __ i < j and k < 2:
                        # since a + b == b + a, so just do half in j >= i
                        # same for `*`
                        continue
                    __ nums[j] __ 0 and k __ 3:
                        # divide by 0
                        continue

                    nxts.append(self.OP[k](nums[i], nums[j]))

                    __ self.judgePoint24(nxts
                        r_ True

                    nxts.pop()

        r_ False
