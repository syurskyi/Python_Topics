#!/usr/bin/python3
"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""
____ typing _______ List


c_ Solution:
    ___ fullJustify  words: List[s..], maxWidth: i..) __ List[s..]:
        """
        Round robin distribution of spaces

        Jump and then backtrack
        """
        ret    # list
        char_cnt = 0  # char exclude spaces
        cur_words    # list

        ___ w __ words:
            cur_words.a..(w)
            char_cnt += l..(w)
            __ char_cnt + l..(cur_words) - 1 > maxWidth:
                # break
                cur_words.pop()
                char_cnt -= l..(w)
                ___ i __ r..(maxWidth - char_cnt
                    cur_words[i % m..(1, l..(cur_words) - 1)] += " "

                ret.a..("".j..(cur_words))

                cur_words = [w]
                char_cnt = l..(w)

        # last line
        last = " ".j..(cur_words)
        ret.a..(last + " " * (maxWidth - l..(last)))
        r.. ret


c_ Solution2:
    ___ fullJustify  words: List[s..], maxWidth: i..) __ List[s..]:
        """
        Round robin distribution of spaces

        Look before jump
        Look before you leap
        """
        ret    # list
        char_cnt = 0
        cur_words    # list

        ___ w __ words:
            # len(cur_words) is the space needed with len(cur_words) + 1 words
            __ char_cnt + l..(w) + l..(cur_words) > maxWidth:
                # break, move w into the next line
                # Round robin distribut the spaces except for the last word
                ___ i __ r..(maxWidth - char_cnt
                    cur_words[i % m..(1, l..(cur_words) - 1)] += " "  # insert in between
                    # len(cur_words) - 1 can be 0
                ret.a..("".j..(cur_words))

                cur_words    # list
                char_cnt = 0

            cur_words.a..(w)
            char_cnt += l..(w)

        # last line
        last = " ".j..(cur_words)
        ret.a..(last + " " * (maxWidth - l..(last)))
        r.. ret


__ _______ __ _______
    ... Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) __ ["This    is    an","example  of text","justification.  "]
    ... Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16) __ ["What   must   be","acknowledgment  ","shall be        "]
