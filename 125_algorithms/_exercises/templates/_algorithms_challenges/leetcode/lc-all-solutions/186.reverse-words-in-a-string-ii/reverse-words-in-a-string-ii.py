class Solution:
  # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
  # @return nothing
  ___ reverseWords(self, s
    ___ swap(start, end, slist
      w___ start < end:
        slist[start], slist[end] = slist[end], slist[start]
        start += 1
        end -= 1

    wstart, wend = 0, 0
    ___ i in range(0, le.(s)):
      __ s[i] __ " ":
        wend = i - 1
        swap(wstart, wend, s)
        wstart = i + 1
      ____ i + 1 __ le.(s
        swap(wstart, i, s)

    swap(0, le.(s) - 1, s)
