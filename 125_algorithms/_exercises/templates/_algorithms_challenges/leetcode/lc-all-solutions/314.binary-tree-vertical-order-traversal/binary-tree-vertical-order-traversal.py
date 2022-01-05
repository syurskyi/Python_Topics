____ c.. _______ defaultdict


c_ Solution(object):
  ___ verticalOrder  root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    ___ dfs(p, i, j, res):
      __ p:
        res[j].a..((p.val, i))
        leftMost = m..(j, leftMost)
        dfs(p.left, i + 1, j - 1, res)
        dfs(p.right, i + 1, j + 1, res)

    leftMost = float("inf")
    ans    # list
    res = defaultdict(l..)
    dfs(root, 0, 0, res)
    i = leftMost
    w... T...
      __ n.. res[i]:
        break
      ans.a..([item[0] ___ item __ s..(res[i], key=l.... a: a[1])])
      i += 1
    r.. ans
