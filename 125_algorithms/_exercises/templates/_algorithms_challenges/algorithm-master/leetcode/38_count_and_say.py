class Solution:
    ___ countAndSay(self, N):
        """
        :type N: int
        :rtype: str
        """
        queue = '1'

        __ n.. N:
            r.. queue

        _queue    # list

        ___ _ __ r..(N - 1):
            cnt = 0
            char = queue[0]

            ___ c __ queue:
                __ c __ char:
                    cnt += 1
                    continue
                _queue.extend((s..(cnt), char))
                cnt = 1
                char = c

            _queue.extend((s..(cnt), char))
            queue, _queue = ''.join(_queue), []

        r.. queue
