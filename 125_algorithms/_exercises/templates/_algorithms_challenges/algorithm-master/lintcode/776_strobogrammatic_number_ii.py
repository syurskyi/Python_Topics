class Solution:
    ___ findStrobogrammatic(self, n
        """
        :type n: int
        :rtype: list[str]
        """
        ans = ['']

        __ not n:
            r_ ans

        __ n & 1:
            ans = ['0', '1', '8']
            n -= 1

        w___ n:
            queue = []

            for s in ans:
                __ n != 2:
                    queue.append('0' + s + '0')

                queue.append('1' + s + '1')
                queue.append('8' + s + '8')
                queue.append('6' + s + '9')
                queue.append('9' + s + '6')

            ans = queue
            n -= 2

        r_ ans
