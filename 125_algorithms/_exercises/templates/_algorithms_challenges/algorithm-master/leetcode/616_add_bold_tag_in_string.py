"""
>>> gotcha = []
>>> for s in (Solution(),):
...     for _in, _out in (
...         (('', ['']), ''),
...         (('abcxyz123', ['abc', '123']), '<b>abc</b>xyz<b>123</b>'),
...         (('aaabbcc', ['aaa','aab','bc']), '<b>aaabbc</b>c'),
...         (('aabcd', ['ab', 'bc']), 'a<b>abc</b>d'),
...     ):
...         res = s.addBoldTag(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


c_ Solution:
    ___ addBoldTag  s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        __ n.. s o. n.. words:
            r.. ''

        TMPL = '<b>{}</b>'
        n = l..(s)
        ans    # list
        is_bold = [F..] * n
        left = right = 0

        ___ left __ r..(n):
            ___ w __ words:
                size = l..(w)

                __ s[left:left + size] __ w a.. left + size > right:
                    right = left + size

            is_bold[left] = right > left

        left = right = 0

        w.... left < n:
            __ n.. is_bold[left]:
                ans.a..(s[left])
                left += 1
                _____

            right = left

            w.... right < n a.. is_bold[right]:
                right += 1

            ans.a..(TMPL.f..(s[left:right]))
            left = right  # imply left' = left + 1

        r.. ''.j..(ans)
