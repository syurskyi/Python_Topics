from collections ______ defaultdict


class Solution(object
  ___ verticalOrder(self, root
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    ___ dfs(p, i, j, res
      __ p:
        res[j].append((p.val, i))
        self.leftMost = min(j, self.leftMost)
        dfs(p.left, i + 1, j - 1, res)
        dfs(p.right, i + 1, j + 1, res)

    self.leftMost = float("inf")
    ans = []
    res = defaultdict(list)
    dfs(root, 0, 0, res)
    i = self.leftMost
    w___ True:
      __ not res[i]:
        break
      ans.append([item[0] for item in sorted(res[i], key=lambda a: a[1])])
      i += 1
    r_ ans
