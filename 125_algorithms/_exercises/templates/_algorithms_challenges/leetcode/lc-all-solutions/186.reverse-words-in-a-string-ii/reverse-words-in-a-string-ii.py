c_ Solution:
  # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
  # @return nothing
  ___ reverseWords  s
    ___ swap(start, end, slist
      w.... start < end:
        slist[start], slist[end] = slist[end], slist[start]
        start += 1
        end -= 1

    wstart, wend = 0, 0
    ___ i __ r..(0, l..(s:
      __ s[i] __ " ":
        wend = i - 1
        swap(wstart, wend, s)
        wstart = i + 1
      ____ i + 1 __ l..(s
        swap(wstart, i, s)

    swap(0, l..(s) - 1, s)
