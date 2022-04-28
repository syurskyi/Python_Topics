# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """

c_ Solution o..
    ___ longestCommonPrefix  strs):
        ls = l.. strs)
        __ ls __ 1:
            r_ strs[0]
        prefix = ''
        pos = 0
        w.. True:
            try:
                current = strs[0][pos]
            except IndexError:
                break
            index = 1
            w.. index < ls:
                try:
                    __ strs[index][pos] != current:
                        break
                except IndexError:
                    break
                index += 1
            __ index __ ls:
                prefix = prefix + current
            ____
                break
            pos += 1
        r_ prefix

    # def longestCommonPrefix(self, strs):
    #     # https://leetcode.com/discuss/89987/one-line-solution-using-itertools-takewhile
    #     return reduce(lambda s1, s2: ''.join(y[0] for y in itertools.takewhile(lambda x: x[0] == x[1], zip(s1, s2))), strs or [''])



__ ____ __ ____
    # begin
    s  ?
    print s.longestCommonPrefix(["aca","cba"])