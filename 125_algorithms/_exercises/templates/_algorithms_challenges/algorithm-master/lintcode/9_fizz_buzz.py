class Solution:
    ___ fizzBuzz(self, n
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        __ not n:
            r_ ans

        ___ i in range(1, n + 1
            __ i % 3 __ 0 and i % 5 __ 0:
                ans.append('FizzBuzz')
            ____ i % 3 __ 0:
                ans.append('Fizz')
            ____ i % 5 __ 0:
                ans.append('Buzz')
            ____
                ans.append(str(i))

        r_ ans


class Solution:
    ___ fizzBuzz(self, n
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        __ not n:
            r_ ans

        a = i3 = i5 = 1

        w___ a <= n:
            w___ a <= n and a < i3 * 3 and a < i5 * 5:
                ans.append(str(a))
                a += 1

            __ a <= n and a __ i3 * 3 and a __ i5 * 5:
                ans.append('fizz buzz')
                a += 1
                i3 += 1
                i5 += 1
                continue

            w___ a <= n and a __ i3 * 3:
                ans.append('fizz')
                a += 1
                i3 += 1

            w___ a <= n and a __ i5 * 5:
                ans.append('buzz')
                a += 1
                i5 += 1

        r_ ans
