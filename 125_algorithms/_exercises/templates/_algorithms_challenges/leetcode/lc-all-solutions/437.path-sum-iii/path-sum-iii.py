c_ Solution(o..
  ___ pathSum  root, target
    """
    :type root: TreeNode
    :type target: int
    :rtype: int
    """
    count = 0
    preDict = {0: 1}

    ___ dfs(p, target, pathSum, preDict
      __ p:
        pathSum += p.val
        count += preDict.g.. pathSum - target, 0)
        preDict[pathSum] = preDict.g.. pathSum, 0) + 1
        dfs(p.left, target, pathSum, preDict)
        dfs(p.right, target, pathSum, preDict)
        preDict[pathSum] -_ 1

    dfs(root, target, 0, preDict)
    r.. count
