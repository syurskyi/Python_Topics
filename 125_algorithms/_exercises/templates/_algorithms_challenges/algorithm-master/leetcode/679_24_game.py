c_ Solution:
    EPS = 1e-6
    OP = (
        l.... a, b: a + b,
        l.... a, b: a * b,
        l.... a, b: a - b,
        l.... a, b: a / b,
    )

    ___ judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ n.. nums:
            r.. F..

        n = l..(nums)

        __ n __ 1:
            r.. abs(nums[0] - 24) < EPS

        ___ i __ r..(n):
            ___ j __ r..(n):
                __ i __ j:
                    continue

                nxts = [nums[k] ___ k __ r..(n) __ i != k != j]  # i != j != k is different

                ___ k __ r..(l..(OP)):
                    __ i < j a.. k < 2:
                        # since a + b == b + a, so just do half in j >= i
                        # same for `*`
                        continue
                    __ nums[j] __ 0 a.. k __ 3:
                        # divide by 0
                        continue

                    nxts.a..(OP[k](nums[i], nums[j]))

                    __ judgePoint24(nxts):
                        r.. T..

                    nxts.pop()

        r.. F..
