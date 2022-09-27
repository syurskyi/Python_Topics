c_ ValidWordAbbr o..
    ___ -  dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        dictionary = set(dictionary)
        abb_dic  # dict
        ___ s __ dictionary:
            curr = getAbb(s)
            __ curr __ abb_dic:
                abb_dic[curr] = F..
            ____
                abb_dic[curr] = T..

    ___ isUnique  word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abb = getAbb(word)
        hasAbbr = abb_dic.get(abb, N..)
        r_ hasAbbr __ N.. or (hasAbbr and word __ dictionary)


    ___ getAbb  word):
        __ l.. word) <= 2:
            r_ word
        r_ word[0] + s..(l.. word) - 2) + word[-1]



        # Your ValidWordAbbr object will be instantiated and called as such:
        # vwa = ValidWordAbbr(dictionary)
        # vwa.isUnique("word")
        # vwa.isUnique("anotherWord")