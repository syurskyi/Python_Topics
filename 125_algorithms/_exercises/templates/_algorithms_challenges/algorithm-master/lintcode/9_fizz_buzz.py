c_ Solution:
    ___ fizzBuzz  n
        """
        :type n: int
        :rtype: List[str]
        """
        ans    # list

        __ n.. n:
            r.. ans

        ___ i __ r..(1, n + 1
            __ i % 3 __ 0 a.. i % 5 __ 0:
                ans.a..('FizzBuzz')
            ____ i % 3 __ 0:
                ans.a..('Fizz')
            ____ i % 5 __ 0:
                ans.a..('Buzz')
            ____
                ans.a..(s..(i

        r.. ans


c_ Solution:
    ___ fizzBuzz  n
        """
        :type n: int
        :rtype: List[str]
        """
        ans    # list
        __ n.. n:
            r.. ans

        a = i3 = i5 = 1

        w.... a <= n:
            w.... a <= n a.. a < i3 * 3 a.. a < i5 * 5:
                ans.a..(s..(a
                a += 1

            __ a <= n a.. a __ i3 * 3 a.. a __ i5 * 5:
                ans.a..('fizz buzz')
                a += 1
                i3 += 1
                i5 += 1
                _____

            w.... a <= n a.. a __ i3 * 3:
                ans.a..('fizz')
                a += 1
                i3 += 1

            w.... a <= n a.. a __ i5 * 5:
                ans.a..('buzz')
                a += 1
                i5 += 1

        r.. ans
