class Solution:
    ___ fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans    # list

        __ n.. n:
            r.. ans

        ___ i __ r..(1, n + 1):
            __ i % 3 __ 0 and i % 5 __ 0:
                ans.a..('FizzBuzz')
            ____ i % 3 __ 0:
                ans.a..('Fizz')
            ____ i % 5 __ 0:
                ans.a..('Buzz')
            ____:
                ans.a..(str(i))

        r.. ans


class Solution:
    ___ fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans    # list
        __ n.. n:
            r.. ans

        a = i3 = i5 = 1

        while a <= n:
            while a <= n and a < i3 * 3 and a < i5 * 5:
                ans.a..(str(a))
                a += 1

            __ a <= n and a __ i3 * 3 and a __ i5 * 5:
                ans.a..('fizz buzz')
                a += 1
                i3 += 1
                i5 += 1
                continue

            while a <= n and a __ i3 * 3:
                ans.a..('fizz')
                a += 1
                i3 += 1

            while a <= n and a __ i5 * 5:
                ans.a..('buzz')
                a += 1
                i5 += 1

        r.. ans
