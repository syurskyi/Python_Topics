class Solution:
    ___ generate(self, num_rows
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        ans = []
        __ not num_rows:
            r_ ans

        ans.append([1])

        ___ i in range(1, num_rows
            path = [ans[i - 1][0]]

            ___ j in range(1, le.(ans[i - 1])):
                path.append(ans[i - 1][j] + ans[i - 1][j - 1])

            path.append(ans[i - 1][-1])
            ans.append(path)

        r_ ans


class Solution:
    ___ generate(self, num_rows
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        ans = []
        __ not num_rows:
            r_ ans

        ans.append([1])

        ___ i in range(1, num_rows
            ans.append([
                (ans[i - 1] + [0])[j] + ([0] + ans[i - 1])[j]
                ___ j in range(le.(ans[i - 1]) + 1)
            ])

        r_ ans
