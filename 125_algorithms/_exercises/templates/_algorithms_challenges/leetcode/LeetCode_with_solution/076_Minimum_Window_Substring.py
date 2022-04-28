c_ Solution o..
    # def minWindow(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: str
    #     """
    #     letters = set(t)
    #     ls = len(s)
    #
    #     # find the first substring that works
    #     first_match = self.first_match(s, t)
    #     if not first_match:
    #         return ''
    #     else:
    #         start, end, extra = first_match
    #         min_window = (end - start, start, end)
    #
    #     # traverse the string and update start and end
    #     while start < end < ls:
    #         discard = s[start]
    #
    #         # move start on to the next letter
    #         while start < end:
    #             start += 1
    #             if s[start] in letters:
    #                 break
    #
    #         # if discarded letter has extra, no need update end
    #         if discard in extra:
    #             extra[discard] -= 1
    #             if extra[discard] == 0:
    #                 extra.pop(discard)
    #             min_window = min(min_window, (end - start, start, end))
    #             continue
    #
    #         # otherwise move end until it points to the discarded letter
    #         while end < ls:
    #             end += 1
    #             if end == ls:
    #                 continue
    #
    #             letter = s[end]
    #             if letter == discard:
    #                 min_window = min(min_window, (end - start, start, end))
    #                 break
    #
    #             if letter in letters:
    #                 extra[letter] += 1
    #
    #     _, start, end = min_window
    #     return s[start: end + 1]
    #
    # def first_match(self, s, t):
    #     letters = set(t)
    #     to_find = collections.defaultdict(lambda: 0)
    #     extra = collections.defaultdict(lambda: 0)
    #
    #     # build hash table
    #     for i in t:
    #         to_find[i] += 1
    #
    #     # find the start position
    #     for index, letter in enumerate(s):
    #         if letter in to_find:
    #             start = index
    #             break
    #     else:
    #         return False
    #
    #     # find the end position
    #     for index, letter in enumerate(s[start:], start):
    #         if letter not in letters:
    #             continue
    #         if letter in to_find:
    #             to_find[letter] -= 1
    #             if to_find[letter] == 0:
    #                 to_find.pop(letter)
    #         else:
    #             extra[letter] += 1
    #         if not to_find:
    #             end = index
    #             break
    #     else:
    #         return False
    #     return start, end, extra
    ___ minWindow  s, t):
        # http://articles.leetcode.com/finding-minimum-window-in-s-which/
        ls_s, ls_t = l.. s), l.. t)
        need_to_find = [0] * 256
        has_found = [0] * 256
        min_begin, min_end = 0, -1
        min_window = 100000000000000
        ___ index __ r.. ls_t):
            need_to_find[o.. t[index])] += 1
        count, begin = 0, 0
        ___ end __ r.. ls_s):
            end_index = o.. s[end])
            __ need_to_find[end_index] __ 0:
                continue
            has_found[end_index] += 1
            __ has_found[end_index] <= need_to_find[end_index]:
                count += 1
            __ count __ ls_t:
                begin_index = o.. s[begin])
                w.. need_to_find[begin_index] __ 0 or\
                    has_found[begin_index] > need_to_find[begin_index]:
                    __ has_found[begin_index] > need_to_find[begin_index]:
                        has_found[begin_index] -= 1
                    begin += 1
                    begin_index = o.. s[begin])
                window_ls = end - begin + 1
                __ window_ls < min_window:
                    min_begin = begin
                    min_end = end
                    min_window = window_ls
        # print min_begin, min_end
        __ count __ ls_t:
            r_ s[min_begin: min_end + 1]
        ____
            r_ ''


__ ____ __ ____
    s  ?
    print s.minWindow('a', 'a')

