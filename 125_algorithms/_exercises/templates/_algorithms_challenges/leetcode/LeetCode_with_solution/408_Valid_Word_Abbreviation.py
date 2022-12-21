c_ Solution o..
    # def validWordAbbreviation(self, word, abbr):
    #     """
    #     :type word: str
    #     :type abbr: str
    #     :rtype: bool
    #     """
    #     if word == abbr:
    #         return True
    #     pos1 = pos2 = 0
    #     curr = 0
    #     while pos1 < len(abbr) and pos2 < len(word):
    #         try:
    #             num = int(abbr[pos1])
    #             # start with 0
    #             if num == 0 and curr == 0:
    #                 return False
    #             curr = curr * 10 + num
    #         except ValueError:
    #             if curr > 0:
    #                 pos2 += curr
    #             # when number exceeds the end of word
    #             if pos2 >= len(word):
    #                 return False
    #             curr = 0
    #             if abbr[pos1] != word[pos2]:
    #                 return False
    #             pos2 += 1
    #         pos1 += 1
    #     # abbr ends with number
    #     if curr > 0:
    #         pos2 += curr
    #     if pos1 == len(abbr) and pos2 == len(word):
    #         return True
    #     return False
    ___ validWordAbbreviation  word, abbr
        pos = curr = 0
        ___ i __ r.. l.. abbr)):
            try:
                num = i..(abbr[i])
                __ num __ 0 a.. curr __ 0:
                    r_ F..
                curr = curr * 10 + num
            except ValueError:
                pos += curr
                curr = 0
                __ pos >= l.. word
                    r_ F..
                __ word[pos] != abbr[i]:
                    r_ F..
                pos += 1
        pos += curr
        __ pos __ l.. word
            r_ T..
        r_ F..


        