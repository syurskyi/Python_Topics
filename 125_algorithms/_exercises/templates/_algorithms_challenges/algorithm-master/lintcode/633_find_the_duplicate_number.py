"""
Binary Searching

`a`: the duplicated num
`cnt(b)`: the cnt of children less than or equal `b`

for each `num < a`: `cnt(num) == num`
for each `num >= a`: `cnt(num) > num`
"""
class Solution:
    ___ findDuplicate(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        __ not A:
            r_ -1

        left, right = 1, le.(A) - 1

        w___ left + 1 < right:
            mid = (left + right) // 2
            __ self.after_dup(A, mid
                right = mid
            ____
                left = mid

        __ self.after_dup(A, left
            r_ left
        __ self.after_dup(A, right
            r_ right
        r_ -1

    ___ after_dup(self, A, mid
        cnt = 0

        for a in A:
            __ a <= mid:
                cnt += 1
            __ cnt > mid:
                r_ True

        r_ False


"""
Floyd Circle Detection

example: [5,4,4,3,2,1]

i  0, 1, 2, 3, 4, 5
a  5, 4, 4, 3, 2, 1
-------------------
   s              f
      f           s
      s  f
         f     s
         sf
-------------------
   f     s
               s  f
      f  s
               sf
"""
class Solution:
    """
    @param: A: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    ___ findDuplicate(self, A
        __ not A:
            r_ -1

        slow = A[0]
        fast = A[A[0]]

        w___ slow != fast:
            slow = A[slow]
            fast = A[A[fast]]

        fast = 0

        w___ slow != fast:
            slow = A[slow]
            fast = A[fast]

        r_ slow
