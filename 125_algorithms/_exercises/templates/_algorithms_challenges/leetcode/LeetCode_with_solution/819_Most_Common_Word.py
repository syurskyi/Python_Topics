c_ Solution o..
    ___ mostCommonWord  paragraph, banned
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # https://leetcode.com/problems/most-common-word/discuss/193268/python-one-liner
        banned = s..(banned)
        count = collections.Counter(word ___ word __ re.split('[ !?\',;.]',
                                    paragraph.lower()) __ word)
        r_ m..((item ___ item __ count.items() __ item[0] n.. __ banned),
                   key=operator.itemgetter(1))[0]
