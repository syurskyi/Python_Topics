"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the
minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the
watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be
"10:02".
"""
__author__ = 'Daniel'


class Solution(object
    ___ __init__(self
        self.hours = (1, 2, 4, 8)
        self.minutes = (1, 2, 4, 8, 16, 32)

    ___ readBinaryWatch(self, num
        """
        orderly backtracking

        :type num: int
        :rtype: List[str]
        """
        ___ gen(
            ___ hour_n in xrange(min(num, 4)+1
                ___ hour in self.hour(hour_n
                    ___ minute in self.minute(num-hour_n
                        hour = str(hour)
                        minute = ('0' + str(minute))[-2:]
                        yield hour + ':' + minute

        r_ list(gen())

    ___ gen(self, n, head, lst, func
        __ head __ le.(lst
            yield None

        __ n __ 0:
            yield 0

        ___ i in xrange(head, le.(lst)):
            ___ rest in self.gen(n-1, i+1, lst, func
                __ rest is not None:
                    ret = lst[i]+rest
                    __ func(ret
                        yield ret
                    ____
                        break

    ___ hour(self, n
        r_ self.gen(n, 0, self.hours, lambda x: x < 12)

    ___ minute(self, n
        r_ self.gen(n, 0, self.minutes, lambda x: x < 60)


__ __name__ __ "__main__":
    assert Solution().readBinaryWatch(1) __ ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00',
                                             '8:00']
