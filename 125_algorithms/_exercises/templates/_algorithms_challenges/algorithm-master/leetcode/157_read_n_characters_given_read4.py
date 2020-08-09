"""
The read4 API is already defined for you.
@param buf, a list of characters
@return an integer

___ read4(buf
    pass
"""


class Solution:
    ___ read(self, buf, n
        """
        :type buf: List[str], Destination buffer
        :type n: int, Maximum number of characters to read
        :rtype: int, The number of characters read
        """
        __ not buf or n <= 0:
            r_ 0

        i = 0
        k = 4
        tmp = [0] * k

        w___ i < n and k __ 4:
            k = read4(tmp)
            j = 0

            w___ i < n and j < k:
                buf[j] = tmp[j]
                i += 1
                j += 1

        r_ i


__ __name__ __ '__main__':
    data = 'abcdferrdsjfklsdjfdsr'
    n = le.(data)
    i = 0
    k = 4

    ___ read4(buf
        global i
        j = 0

        w___ i < n and j < k:
            buf[j] = data[i]
            i += 1
            j += 1

        r_ j

    s = Solution()
    res = s.read([0] * 4, 4)
    print(res)
