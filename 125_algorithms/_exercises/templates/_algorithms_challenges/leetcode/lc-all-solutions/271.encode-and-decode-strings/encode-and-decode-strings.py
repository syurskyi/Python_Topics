c_ Codec:
  ___ encode  strs
    """Encodes a list of strings to a single string.
    
    :type strs: List[str]
    :rtype: str
    """
    ret = ""
    ___ s __ strs:
      ret += s..(l..(s + "|" + s

    r.. ret

  ___ decode  s
    """Decodes a single string to a list of strings.
    
    :type s: str
    :rtype: List[str]
    """
    ret    # list
    start = end = 0
    w.... end < l..(s
      __ s[end] != "|":
        end += 1
      ____
        length = i..(s[start:end])
        start = end + 1
        end = start + length
        ret.a..(s[start:end])
        start = end
    r.. ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
