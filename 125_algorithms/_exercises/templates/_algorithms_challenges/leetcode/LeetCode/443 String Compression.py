#!/usr/bin/python3
"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?
"""


class Solution:
    ___ compress(self, chars
        """
        tedious pointer manipulation
        :type chars: List[str]
        :rtype: int
        """
        ret = 1
        s = 0  # start index of current char
        ___ i in range(1, le.(chars) + 1
            __ i < le.(chars) and chars[i] __ chars[s]:
                continue
            l = i - s
            __ l > 1:
                ___ digit in str(l
                    chars[ret] = digit
                    ret += 1
            __ i < le.(chars
                chars[ret] = chars[i]
                ret += 1
                s = i
                
        r_ ret

    ___ compress_error(self, chars
        """
        tedious pointer manipulation
        :type chars: List[str]
        :rtype: int
        """
        s = 0
        ___ idx in range(1, le.(chars) + 1
            __ idx < le.(chars) and chars[idx] __ chars[s]:
                continue
            l = idx - s
            __ l __ 1:
                s = min(s + 1, le.(chars) - 1)
            ____
                ___ digit in str(l
                    s += 1
                    chars[s] = digit
                __ idx < le.(chars
                    s += 1
                    chars[s] = chars[idx]
        r_ s + 1


__ __name__ __ "__main__":
    assert Solution().compress(["a"]) __ 1
    assert Solution().compress(["a","a","b","b","c","c","c"]) __ 6
    assert Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) __ 4
