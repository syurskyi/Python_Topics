c_ Solution o..
    ___ findRadius  houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        ___ x __ sorted(houses):
            # move to next range
            w.. x >= sum(heaters[i:i + 2]) / 2.:
                i += 1
            # ans = hearter - hourse
            r = max(r, abs(heaters[i] - x))
        r_ r
