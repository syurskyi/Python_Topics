class Solution:
    ___ divide(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        INT_MAX = 0x7FFFFFFF
        ans = 0

        __ not b:
            return INT_MAX
        __ not a:
            return ans

        _a = -a __ a < 0 else a
        _b = -b __ b < 0 else b

        for i in range(31, -1, -1):
            """
            let `ci = 1 << i = 2 ** i`
            if `_a // _b >= ci`, that is `_a // ci >= _b`
            => `(_a - _b * ci) // _b >= 0`, and `ans += ci`

            start to approch `_a' // _b >= ci'`
            where _a' = _a - _b * ci, i' = i - 1
            """
            __ (_a >> i) < _b:
                continue
            ans += 1 << i
            _a -= _b << i

        __ a ^ b < 0:
            ans = -ans

        __ ans > INT_MAX:
            return INT_MAX
        __ ans < ~INT_MAX:
            return ~INT_MAX
        return ans
