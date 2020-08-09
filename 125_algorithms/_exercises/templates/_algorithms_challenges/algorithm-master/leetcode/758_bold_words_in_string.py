"""
>>> gotcha = []
>>> for s in (Solution(),
...     for _in, _out in (
...         (([''], ''), ''),
...         ((['abc', '123'], 'abcxyz123'), '<b>abc</b>xyz<b>123</b>'),
...         ((['aaa','aab','bc'], 'aaabbcc'), '<b>aaabbc</b>c'),
...         ((['ab', 'bc'], 'aabcd'), 'a<b>abc</b>d'),
...
...         res = s.boldWords(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    ___ boldWords(self, words, s
        """
        :type words: List[str]
        :type s: str
        :rtype: str
        """
        __ not s or not words:
            r_ ''

        TMPL = '<b>{}</b>'
        n = le.(s)
        ans = []
        is_bold = [False] * n
        left = right = 0

        ___ left in range(n
            ___ w in words:
                size = le.(w)

                __ s[left:left + size] __ w and left + size > right:
                    right = left + size

            is_bold[left] = right > left

        left = right = 0

        w___ left < n:
            __ not is_bold[left]:
                ans.append(s[left])
                left += 1
                continue

            right = left

            w___ right < n and is_bold[right]:
                right += 1

            ans.append(TMPL.format(s[left:right]))
            left = right  # imply left' = left + 1

        r_ ''.join(ans)
