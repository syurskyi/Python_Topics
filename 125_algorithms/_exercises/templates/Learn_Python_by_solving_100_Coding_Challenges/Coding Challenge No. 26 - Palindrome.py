# Palindrome
# Question: Checking whether or not a string is a palindrome. It spells the same forward as backwards. Write a method to determine if a string is a palindrome
# Note: remove any extraneous things like spaces or punctuation from the string. So the following strings would all be palindromes. "racecar", "race car" "race, car ".
# Solutions:


c_ Solution:
    # @param s, a string
    # @return a boolean
    ___ isPalindrome(self, s):
        __ le.(s) < 2:
            r_ T..
        head, tail _ 0, le.(s)-1
        w___ head < tail:
            __ no. s[head].isalnum
                head +_ 1
            ____ no. s[tail].isalnum
                tail -_ 1
            ____
                __ s[head].l.. __ s[tail].lower
                    head +_ 1
                    tail -_ 1
                ____
                    r_ F..
        r_ T..


Solution().isPalindrome(["racecar","race car","race, car"])