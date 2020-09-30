# Length of Last Word
# Question: Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string. If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.
# For example,
# Given s = "Hello World",
# return 5.
# Solutions:

class Solution:
    # @param s, a string
    # @return an integer

    def lengthOfLastWord1(self, s):
        return len(s.split()[len(s.split())-1]) if s.split() != [] else 0

    # @param s, a string
    # @return an integer

    def lengthOfLastWord2(self, s):
        s = s.strip() # Remove the spaces at the beginning and end
        length = 0
        for letter in s:
            if letter == " ":
                length = 0 # Waiting for the next word
            else:
                length += 1 # Inside one word
        return length
        # @param s, a string
        # @return an integer

    def lengthOfLastWord3(self, s):
        preLength = 0 # Length of previous word
        length = 0 # Length of current word
        for letter in s:
            if letter == " ": # Waiting for the next word
                if length != 0: # This is a single zero or
                    # leading one in zeros
                    preLength = length
                    length = 0
                else: # A following zero in zeros
                    pass
            else:
                # Inside one word
                length += 1
        if length == 0:
            return preLength # s ends with zero(s)
        else:
            return length # s ends with word
        print ( Solution().lengthOfLastWord1("Hello World") )
        print ( Solution().lengthOfLastWord2("Hello Worlds") )
        print ( Solution().lengthOfLastWord3("Hello Everybody") )