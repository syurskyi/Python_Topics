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


c_ Solution(o..
    ___ -
        hours = (1, 2, 4, 8)
        minutes = (1, 2, 4, 8, 16, 32)

    ___ readBinaryWatch  num
        """
        orderly backtracking

        :type num: int
        :rtype: List[str]
        """
        ___ gen
            ___ hour_n __ x..(m..(num, 4)+1
                ___ hour __ hour(hour_n
                    ___ minute __ minute(num-hour_n
                        hour = s..(hour)
                        minute = ('0' + s..(minute[-2:]
                        y.. hour + ':' + minute

        r.. l..(gen

    ___ gen  n, head, lst, func
        __ head __ l..(lst
            y.. N..

        __ n __ 0:
            y.. 0

        ___ i __ x..(head, l..(lst:
            ___ rest __ gen(n-1, i+1, lst, func
                __ rest __ n.. N..
                    ret = lst[i]+rest
                    __ func(ret
                        y.. ret
                    ____
                        _____

    ___ hour  n
        r.. gen(n, 0, hours, l.... x: x < 12)

    ___ minute  n
        r.. gen(n, 0, minutes, l.... x: x < 60)


__ _______ __ _______
    ... Solution().readBinaryWatch(1) __  '0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00',
                                             '8:00'
