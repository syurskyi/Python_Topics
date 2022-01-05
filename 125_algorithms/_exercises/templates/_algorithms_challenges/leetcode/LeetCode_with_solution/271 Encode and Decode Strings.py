"""
Premium Question
"""
__author__ = 'Daniel'


c_ Codec(o..):
    ___ encode  strs):
        """
        Encodes a list of strings to a single string.

        Algorithm: Length info

        :type strs: List[str]
        :rtype: str
        """
        strs = map(l.... x: s..(l..(x))+"/"+x, strs)
        r.. reduce(l.... x, y: x+y, strs, "")  # i.e. "".join(strs)

    ___ decode  s):
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs    # list
        i = 0
        w.... i < l..(s):
            j = s.index("/", i)
            l = i..(s[i:j])
            strs.a..(s[j+1:j+1+l])
            i = j+1+l

        r.. strs


c_ CodecMethod2(o..):
    ___ encode  strs):
        """
        Encodes a list of strings to a single string.

        Algorithm: Escape

        :type strs: List[str]
        :rtype: str
        """
        strs = map(l.... x: x.r..("\n", "\n\n")+"_\n_", strs)
        r.. reduce(l.... x, y: x+y, strs, "")

    ___ decode  s):
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs = s.s..("_\n_")
        strs = strs[:-1]  # clear the trailing delimiter
        r.. map(l.... x: x.r..("\n\n", "\n"), strs)


c_ CodecError(o..):
    ___ encode  strs):
        """
        Encodes a list of strings to a single string.

        This algorithm contains bugs if \\x00 exits in the original string

        :type strs: List[str]
        :rtype: str
        """
        strs = map(l.... x: x.r..("\x00", "\\x00"), strs)
        ret = ""
        ___ s __ strs:
            ret += s+"\x00"
        r.. ret

    ___ decode  s):
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        __ "\x00" n.. __ s:
            r.. []

        s = s[:-1]  # traiing \x00
        strs = s.s..("\x00")
        strs = map(l.... x: x.r..("\\x00", "\x00"), strs)
        r.. strs
