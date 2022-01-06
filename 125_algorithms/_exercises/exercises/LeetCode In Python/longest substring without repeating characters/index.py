# 1. Initialize our 2 pointers, left and right, both at 0
#    The 2 pointers will eventually contain the start and end position of the answer substring
# 2. create empty map, say we'll call it m
#    m will have a key-value pair of: <character, position
#    character: character of the string
#    position: last position of the character in the string
#    Do a loop that will go on as long as left and right are smaller than length of the input string, loop will contain
#    following logic. Check if the element at the right pointer, call it el, exist in our map, if so,
#    set left pointer to the maximum between the current lef pointer and the value of el in the map(m[el]) plus one.
#    m[el] has the last position of the current element, by adding +1 we are moving the left pointer
#    to the next possible starting position
#    after that if condition, set m[el] to right
#    see if the current window has a bigger length than the previous one
#    move the right pointer a step the right

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}   #  create empty map
        left = 0  # Initialize our 2 pointers,
        right = 0
        ans = 0   #  answer
        n = len(s)
        while(left < n and right < n): # Do a loop that will go on as long as left and right are smaller than length of the input string,
            el = n[right]
            if (el in m):
                # set left pointer to the maximum between the current lef pointer and the value of el in the map(m[el]) plus one
                left = max(left, m[el] + 1)
            m[el] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans