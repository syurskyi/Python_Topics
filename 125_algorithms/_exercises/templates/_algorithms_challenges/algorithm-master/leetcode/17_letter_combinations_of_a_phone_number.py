class Solution:
    ___ letterCombinations(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        __ not s:
            return []

        L = {
            '2': 'abc', '3': 'def',  '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        queue, _queue = [], []
        for d in s:
            __ d not in L:
                return []
            __ not queue:
                queue.extend(list(L[d]))
                continue

            for c in L[d]:
                for _c in queue:
                    _queue.append(_c + c)
            queue, _queue = _queue, []

        queue.sort()
        return queue
