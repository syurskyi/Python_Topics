c_ Solution:
    ___ kthSmallest root: TreeNode, k: in.)  in.:
        .k _ k
        .res _ N..
        .helper(root)
        r_ .res

    ___ helper root
        __ no. root:
            r_
        .helper(root.left)
        
        .k -_ 1
        __ .k __ 0:
            .res _ root.val
            r_
        .helper(root.right)
