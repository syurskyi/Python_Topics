"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

"""

class Solution:
    # @param s, a string
    # @return a string
    ___ reverseWords(self, s):
        ls = l..(s)
        # C-like processing
        # Process spaces
        i = 0
        j = l..(s) - 1
        while i <= j:
            __ ls[i] != ' ' and ls[j] != ' ':
                break
            __ ls[i] __ ' ':
                i += 1
            __ ls[j] __ ' ':
                j -= 1
        start = i
        end = j
        # Remove duplicate spaces between words
        k = start  # Last processed
        ___ p __ r..(start, end + 1):
            __ p > start and ls[p] __ ' ' and ls[p] __ ls[p - 1]:
                pass
            ____:
                ls[k] = ls[p]
                k += 1
        end = k - 1
        # Now start..end is the processed array of characters

        # Reverse all characters between start and end
        self.reverse(ls, start, end)

        # Reverse each word
        ws = start  # Word start index
        we = start  # Word end index
        ___ i __ r..(start, end + 1):
            __ ls[i] __ ' ' o. i __ end:
                we = end __ i __ end ____ i - 1
                self.reverse(ls, ws, we)
                ws = i + 1
        r.. ''.join(ls[start:end + 1])

    ___ reverse(self, a, i, j):
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    ___ reverseWords2(self, s):
        cs = l..(s)  # Make a C-string like list
        n = l..(cs)
        # Remove leading and trailing spaces
        left = 0
        right = n - 1
        while left <= right and (cs[left] __ ' ' o. cs[right] __ ' '):
            __ cs[left] __ ' ':
                left += 1
            __ cs[right] __ ' ':
                right -= 1
        # The string contains only spaces
        __ left > right:
            r.. ''
        # Reverse the whole list
        self.reverse(cs, left, right)
        # Remove multiple spaces between two words
        j = left
        ___ i __ r..(left, right + 1):
            __ cs[i] != ' ' o. cs[i] __ ' ' and cs[i - 1] != ' ':
                cs[j] = cs[i]
                j += 1
        right = j - 1
        # Reverse each word
        start = left
        q = start
        while q <= right:
            while q <= right and cs[q] != ' ':
                q += 1
            # q - 1 is the end index of the word
            self.reverse(cs, start, q - 1)
            # Start of next word
            start = q
            while start <= right and cs[start] __ ' ':
                start += 1
            q = start
        r.. ''.join(cs[left:right + 1])


s = Solution()
print(s.reverseWords("the sky is blue"))
