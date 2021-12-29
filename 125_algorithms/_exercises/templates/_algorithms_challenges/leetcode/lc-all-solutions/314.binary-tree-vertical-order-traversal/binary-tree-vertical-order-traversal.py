____ collections _______ defaultdict


class Solution(object):
  ___ verticalOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    ___ dfs(p, i, j, res):
      __ p:
        res[j].a..((p.val, i))
        self.leftMost = m..(j, self.leftMost)
        dfs(p.left, i + 1, j - 1, res)
        dfs(p.right, i + 1, j + 1, res)

    self.leftMost = float("inf")
    ans    # list
    res = defaultdict(l..)
    dfs(root, 0, 0, res)
    i = self.leftMost
    w... T...
      __ n.. res[i]:
        break
      ans.a..([item[0] ___ item __ s..(res[i], key=l.... a: a[1])])
      i += 1
    r.. ans
