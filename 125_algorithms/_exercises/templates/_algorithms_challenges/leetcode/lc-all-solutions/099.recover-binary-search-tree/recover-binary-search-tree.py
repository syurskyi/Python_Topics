c_ Solution:
  ___ -
    n1 N..
    n2 N..
    pre N..

  ___ findBadNode  root
    __ root __ N.. r..
    findBadNode(root.left)
    __ pre __ n.. N..
      __ root.val < pre.val:
        __ n1 __ N..
          n1 pre
          n2 root
        ____
          n2 root
    pre root
    findBadNode(root.right)

  ___ recoverTree  root
    findBadNode(root)
    __ n1 __ n.. N.. a.. n2 __ n.. N..
      n1.val, n2.val n2.val, n1.val
