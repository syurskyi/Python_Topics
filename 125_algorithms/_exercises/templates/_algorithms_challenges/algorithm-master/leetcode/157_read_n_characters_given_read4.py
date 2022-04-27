"""
The read4 API is already defined for you.
@param buf, a list of characters
@return an integer

def read4(buf):
    pass
"""


c_ Solution:
    ___ read  buf, n
        """
        :type buf: List[str], Destination buffer
        :type n: int, Maximum number of characters to read
        :rtype: int, The number of characters read
        """
        __ n.. buf o. n <_ 0:
            r.. 0

        i 0
        k 4
        tmp  [0] * k

        w.... i < n a.. k __ 4:
            k read4(tmp)
            j 0

            w.... i < n a.. j < k:
                buf[j] tmp[j]
                i += 1
                j += 1

        r.. i


__ _____ __ _____
    data 'abcdferrdsjfklsdjfdsr'
    n l.. ?
    i 0
    k 4

    ___ read4(buf
        g.. i
        j 0

        w.... i < n a.. j < k:
            buf[j] data[i]
            i += 1
            j += 1

        r.. j

    s Solution()
    res s.read([0] * 4, 4)
    print(res)
