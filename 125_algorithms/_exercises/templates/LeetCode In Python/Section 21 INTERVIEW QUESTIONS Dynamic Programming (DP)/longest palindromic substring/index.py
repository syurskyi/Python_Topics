class Solution:
    ___ longestPalindrome(self, s: str) -> str:
        n = le.(s)
        __(n<2
            r_ s
        left = 0
        right = 0

        palindrome = [[0]*n for _ in range(n)]

        for j in range(1,n
            for i in range(0,j
                innerIsPalindrome = palindrome[i+1][j-1] or j-i<=2
                __(s[i] __ s[j] and innerIsPalindrome
                    palindrome[i][j] = True
                    __(j-i>right-left
                        left = i
                        right = j

        r_ s[left:right+1]