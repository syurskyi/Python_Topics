c_ Solution o..
    ___ compress  chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # https://leetcode.com/problems/string-compression/solution/
        anchor = write = 0
        ___ read, c __ e.. chars):
            __ read + 1 __ l.. chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                __ read > anchor:
                    ___ digit __ s..(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        r_ write