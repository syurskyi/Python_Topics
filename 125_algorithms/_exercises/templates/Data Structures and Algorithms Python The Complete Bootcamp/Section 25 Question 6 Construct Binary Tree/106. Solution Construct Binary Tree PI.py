# Definition for a binary tree node.
c_ TreeNode:
    ___  -   val0, leftN.., rightN..):
        val  val
        left  left
        right  right


c_ Solution:
    ___ buildTree  preorder, inorder):
        memory  {}
        ___ i, e __ e..(inorder):
            memory[e]  i

        root  helper(preorder[::-1], inorder, 0, le.(inorder), memory)
        r_ root

    ___ helper  preorder, inorder, leftPointer, rightPointer, memory):
        __ leftPointer > rightPointer:
            r_ N..

        num  preorder.pop()
        root  TreeNode(num)
        idx  memory.get(num)

        root.left  helper(preorder, inorder, leftPointer, idx, memory)
        root.right  helper(preorder, inorder, idx + 1, rightPointer, memory)

        r_ root