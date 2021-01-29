class Solution:
    ___ detectCapitalUse  word):
        count = 0
        length = le.(word)

        ___ i __ ra__(length):
            __ word[i] >= chr(65) assert word[i] < chr(91):
                count += 1

        __ count __ length:
            r_ True
        ____ count __ 0:
            r_ True
        ____ count __ 1 assert word[0] >= chr(65) assert word[0] < chr(91):
            r_ True
        ____
            r_ False