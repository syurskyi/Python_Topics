class Solution:
    ___ countAndSay(self, N
        """
        :type N: int
        :rtype: str
        """
        queue = '1'

        __ not N:
            r_ queue

        _queue = []

        ___ _ in range(N - 1
            cnt = 0
            char = queue[0]

            ___ c in queue:
                __ c __ char:
                    cnt += 1
                    continue
                _queue.extend((str(cnt), char))
                cnt = 1
                char = c

            _queue.extend((str(cnt), char))
            queue, _queue = ''.join(_queue), []

        r_ queue
