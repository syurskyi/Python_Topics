c_ Solution o..
    ___ canConstruct  ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letter_map  # dict
        ___ letter __ magazine:
            letter_map[letter] = letter_map.get(letter, 0) + 1
        ___ letter __ ransomNote:
            letter_map[letter] = letter_map.get(letter, 0) - 1
            __ letter_map[letter] < 0:
                r_ False
        r_ True

    # def canConstruct(self, ransomNote, magazine):
    #     return not collections.Counter(ransomNote) - collections.Counter(magazine)
