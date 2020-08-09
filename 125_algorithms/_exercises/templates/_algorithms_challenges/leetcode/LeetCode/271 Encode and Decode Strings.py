"""
Premium Question
"""
__author__ = 'Daniel'


class Codec(object
    ___ encode(self, strs
        """
        Encodes a list of strings to a single string.

        Algorithm: Length info

        :type strs: List[str]
        :rtype: str
        """
        strs = map(lambda x: str(le.(x))+"/"+x, strs)
        r_ reduce(lambda x, y: x+y, strs, "")  # i.e. "".join(strs)

    ___ decode(self, s
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        w___ i < le.(s
            j = s.index("/", i)
            l = int(s[i:j])
            strs.append(s[j+1:j+1+l])
            i = j+1+l

        r_ strs


class CodecMethod2(object
    ___ encode(self, strs
        """
        Encodes a list of strings to a single string.

        Algorithm: Escape

        :type strs: List[str]
        :rtype: str
        """
        strs = map(lambda x: x.replace("\n", "\n\n")+"_\n_", strs)
        r_ reduce(lambda x, y: x+y, strs, "")

    ___ decode(self, s
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs = s.split("_\n_")
        strs = strs[:-1]  # clear the trailing delimiter
        r_ map(lambda x: x.replace("\n\n", "\n"), strs)


class CodecError(object
    ___ encode(self, strs
        """
        Encodes a list of strings to a single string.

        This algorithm contains bugs if \\x00 exits in the original string

        :type strs: List[str]
        :rtype: str
        """
        strs = map(lambda x: x.replace("\x00", "\\x00"), strs)
        ret = ""
        ___ s in strs:
            ret += s+"\x00"
        r_ ret

    ___ decode(self, s
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        __ "\x00" not in s:
            r_ []

        s = s[:-1]  # traiing \x00
        strs = s.split("\x00")
        strs = map(lambda x: x.replace("\\x00", "\x00"), strs)
        r_ strs
