c_ Solution:
    ___ lexicalOrder  n
        """
        :type n: int
        :rtype: List[int]
        """
        ans    # list

        __ n.. n:
            r.. ans

        stack = [1]

        w.... stack:
            x = stack.p.. )
            ans.a..(x)

            # considering the case no carry up if x + 1
            # that is, x in [1, 8]
            __ x < n a.. x % 10 < 9:
                stack.a..(x + 1)

            __ x * 10 <_ n:
                stack.a..(x * 10)

        r.. ans
