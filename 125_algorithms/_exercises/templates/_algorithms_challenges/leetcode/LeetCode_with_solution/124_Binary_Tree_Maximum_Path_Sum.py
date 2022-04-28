# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution o..
    ___ -(self):
        result = -2147483647

    ___ maxPathSum  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return (root.val,left+root.val,right+root.val,left+right+root);
        getNodeMaxValue(root)
        r_ result

    ___ getNodeMaxValue  node):
        __ node is N..:
            r_ 0
        lresult = getNodeMaxValue(node.left)
        rresult = getNodeMaxValue(node.right)
        result = max(lresult + rresult + node.val, result)
        ret = node.val + max(lresult, rresult)
        # if max left or right < 0 then return 0
        __ ret > 0:
            r_ ret
        r_ 0
