c_ Solution o..
    # def strStr(self, haystack, needle):
    #     """
    #     :type haystack: str
    #     :type needle: str
    #     :rtype: int
    #     """
    #     lsh, lsn = len(haystack), len(needle)
    #     if lsn == 0:
    #         return 0
    #     pos, index = 0, 0
    #     while index <= lsh - lsn:
    #         if haystack[index] == needle[pos]:
    #             backup = index
    #             while index < lsh and pos < lsn and haystack[index] == needle[pos]:
    #                 pos += 1
    #                 index += 1
    #             if pos == len(needle):
    #                 return index - pos
    #             index = backup
    #         index += 1
    #         pos = 0
    #     return -1

    # def strStr(self, haystack, needle):
    #     lsh, lsn = len(haystack), len(needle)
    #     if lsn == 0:
    #         return 0
    #     pos, index = 0, 0
    #     while index <= lsh - lsn:
    #         if haystack[index] == needle[0]:
    #             # slice index:index + lsn
    #             if haystack[index:index + lsn] == needle:
    #                 return index
    #         index += 1
    #     return -1

    # KMP
    # https://discuss.leetcode.com/topic/3576/accepted-kmp-solution-in-java-for-reference/2
    ___ strStr  haystack, needle
        lsh, lsn = l.. haystack), l.. needle)
        __ lsn __ 0:
            r_ 0
        next = makeNext(needle)
        i = j = 0
        w.. i < lsh:
            __ j __ -1 or haystack[i] __ needle[j]:
                i += 1
                j += 1
                __ j __ lsn:
                    r_ i - lsn
            __ i < lsh and haystack[i] != needle[j]:
                j = next[j]
        r_ -1

    ___ makeNext  needle
        ls = l.. needle)
        next = [0] * ls
        next[0], i, j = -1, 0, -1
        w.. i < ls - 1:
            __ j __ -1 or needle[i] __ needle[j]:
                next[i + 1] = j + 1
                __ needle[i + 1] __ needle[j + 1]:
                    next[i + 1] = next[j + 1]
                i += 1
                j += 1
            __ needle[i] != needle[j]:
                j = next[j]
        r_ next

