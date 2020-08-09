class Solution:
    ___ letterCombinations(self, s
        """
        :type s: str
        :rtype: List[str]
        """
        __ not s:
            r_ []

        L = {
            '2': 'abc', '3': '___',  '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        queue, _queue = [], []
        ___ d in s:
            __ d not in L:
                r_ []
            __ not queue:
                queue.extend(list(L[d]))
                continue

            ___ c in L[d]:
                ___ _c in queue:
                    _queue.append(_c + c)
            queue, _queue = _queue, []

        queue.sort()
        r_ queue
