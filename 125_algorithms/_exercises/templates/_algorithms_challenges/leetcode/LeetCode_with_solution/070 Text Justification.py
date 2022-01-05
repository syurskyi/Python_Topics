"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left
and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces
' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide
evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""
__author__ = 'Danyang'


c_ Solution:
    ___ fullJustify  words, L):
        """

        :param words: a list of str
        :param L: int
        :return: a list of str
        """
        result    # list
        break_line(words, L, result)
        r.. distribute_space(L, result)

    ___ break_line  words, L, result):
        __ n.. words:
            r..

        cur_length = -1
        lst    # list
        i = 0
        w.... i<l..(words):
            word = words[i]
            cur_length += 1 # space in left justified
            cur_length += l..(word)
            __ cur_length>L: break
            lst.a..(word)
            i += 1

        result.a..(lst)
        break_line(words[i:], L, result)


    ___ distribute_space  L, result):
        new_result    # list
        ___ ind, line __ e..(result):
            word_cnt = l..(line)
            str_builder    # list
            space_cnt = L-s..(l..(word) ___ word __ line)
            hole_cnt = word_cnt-1
            __ ind<l..(result)-1:
                __ hole_cnt>0:
                    space = space_cnt/hole_cnt
                    remain = space_cnt%hole_cnt

                    ___ word __ line[:-1]:
                        str_builder.a..(word)
                        str_builder.a..(" "*space)
                        __ remain>0:
                            str_builder.a..(" ")
                            remain -= 1

                    str_builder.a..(line[-1])
                ____:
                    str_builder.a..(line[-1])
                    str_builder.a..(" "*space_cnt)
            ____:  # last line, special handling
                str_builder = [" ".j..(line)]
                str_builder.a..(" "*(space_cnt-hole_cnt))

            new_result.a..("".j..(str_builder))

        r.. new_result



__ _____ __ ____
    print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    print Solution().fullJustify(["What","must","be","shall","be."], 12)
