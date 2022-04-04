c_ Solution:
    ___ letterCombinations  s
        """
        :type s: str
        :rtype: List[str]
        """
        __ n.. s:
            r.. []

        L = {
            '2': 'abc', '3': 'def',  '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        queue, _queue    # list, []
        ___ d __ s:
            __ d n.. __ L:
                r.. []
            __ n.. queue:
                queue.e.. l..(L[d]
                _____

            ___ c __ L[d]:
                ___ _c __ queue:
                    _queue.a..(_c + c)
            queue, _queue = _queue, []

        queue.s..()
        r.. queue
