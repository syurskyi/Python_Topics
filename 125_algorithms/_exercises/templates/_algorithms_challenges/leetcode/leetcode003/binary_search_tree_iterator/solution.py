# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ BSTIterator(object):
    ___ - , root):
        _arr    # list
        _inorder(root)
        _cur = -1

    # @return a boolean, whether we have a next smallest number
    ___ hasNext
        __ _arr[_cur + 1:]:
            r.. T..
        r.. F..

    # @return an integer, the next smallest number
    ___ next
        __ hasNext
            _cur += 1
            r.. _arr[_cur]

    ___ _inorder  root):
        __ root __ n.. N..
            __ root.left __ n.. N..
                _inorder(root.left)
            _arr.a..(root.val)
            __ root.right __ n.. N..
                _inorder(root.right)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
