c_ Solution:
    ___ findStrobogrammatic  n):
        """
        :type n: int
        :rtype: list[str]
        """
        ans = ['']

        __ n.. n:
            r.. ans

        __ n & 1:
            ans = ['0', '1', '8']
            n -= 1

        w.... n:
            queue    # list

            ___ s __ ans:
                __ n != 2:
                    queue.a..('0' + s + '0')

                queue.a..('1' + s + '1')
                queue.a..('8' + s + '8')
                queue.a..('6' + s + '9')
                queue.a..('9' + s + '6')

            ans = queue
            n -= 2

        r.. ans
