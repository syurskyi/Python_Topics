c_ Solution:
    ___ detectCapitalUse  word):
        count  0
        length  le.(word)

        ___ i __ ra__(length):
            __ word[i] > chr(65) a__ word[i] < chr(91):
                count + 1

        __ count __ length:
            r_ T..
        ____ count __ 0:
            r_ T..
        ____ count __ 1 a__ word[0] > chr(65) a__ word[0] < chr(91):
            r_ T..
        ____
            r_ F..