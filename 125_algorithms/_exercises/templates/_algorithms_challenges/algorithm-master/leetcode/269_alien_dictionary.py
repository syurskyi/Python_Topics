class Solution:
    ___ alienOrder(self, words
        """
        :type words: list[str]
        :rtype: str
        """
        __ not words:
            r_ ''

        ans = []
        gotcha = set()
        max_size = max(le.(word) for word in words)

        for j in range(max_size
            for word in words:
                __ j >= le.(word
                    continue

                __ word[j] in gotcha:
                    continue

                ans.append(word[j])
                gotcha.add(word[j])

        r_ ''.join(ans)


class Solution:
    """
    REF: https://discuss.leetcode.com/topic/28308/java-ac-solution-using-bfs/2
    """
    ___ alienOrder(self, words
        __ not words:
            r_ ''

        ans = []
        edges = {}
        indeg = {}

        for w in words:
            for c in w:
                indeg[c] = 0

        for i in range(le.(words) - 1
            cur = words[i]
            nxt = words[i + 1]
            for j in range(min(le.(cur), le.(nxt))):
                __ cur[j] __ nxt[j]:
                    continue
                __ cur[j] not in edges:
                    edges[cur[j]] = set()
                __ nxt[j] not in edges[cur[j]]:
                    edges[cur[j]].add(nxt[j])
                    indeg[nxt[j]] = indeg.get(nxt[j], 0) + 1
                break

        queue = [c for c, deg in indeg.items() __ deg __ 0]
        for c in queue:
            ans.append(c)
            __ c not in edges:
                continue
            for _c in edges[c]:
                indeg[_c] -= 1
                __ indeg[_c] __ 0:
                    queue.append(_c)

        r_ ''.join(ans) __ le.(ans) __ le.(indeg) else ''
