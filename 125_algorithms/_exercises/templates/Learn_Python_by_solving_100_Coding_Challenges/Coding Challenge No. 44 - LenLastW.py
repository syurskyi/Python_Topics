# Length of Last Word
# Question: Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string. If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.
# For example,
# Given s = "Hello World",
# return 5.
# Solutions:

c_ Solution
    # @param s, a string
    # @return an integer

    ___ lengthOfLastWord1 , s:
        r_ le. s.sp.. [le. s.sp..-1] __ s.sp..  !_   # list else 0

    # @param s, a string
    # @return an integer

    ___ lengthOfLastWord2 , s:
        s _ s.s..  # Remove the spaces at the beginning and end
        length _ 0
        ___ letter __ s:
            __ letter __ " ":
                length _ 0 # Waiting for the next word
            ____
                length +_ 1 # Inside one word
        r_ length
        # @param s, a string
        # @return an integer

    ___ lengthOfLastWord3 , s:
        preLength _ 0 # Length of previous word
        length _ 0 # Length of current word
        ___ letter __ s:
            __ letter __ " ": # Waiting for the next word
                __ length !_ 0: # This is a single zero or
                    # leading one in zeros
                    preLength _ length
                    length _ 0
                ____ # A following zero in zeros
                    p_
            ____
                # Inside one word
                length +_ 1
        __ length __ 0:
            r_ preLength # s ends with zero(s)
        ____
            r_ length # s ends with word
        print   Solution .lengthOfLastWord1 "Hello World"
        print   Solution .lengthOfLastWord2 "Hello Worlds"
        print   Solution .lengthOfLastWord3 "Hello Everybody"