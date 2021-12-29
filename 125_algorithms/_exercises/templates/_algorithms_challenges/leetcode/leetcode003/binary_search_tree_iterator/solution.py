# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    ___ __init__(self, root):
        self._arr = []
        self._inorder(root)
        self._cur = -1

    # @return a boolean, whether we have a next smallest number
    ___ hasNext(self):
        __ self._arr[self._cur + 1:]:
            return True
        return False

    # @return an integer, the next smallest number
    ___ next(self):
        __ self.hasNext():
            self._cur += 1
            return self._arr[self._cur]

    ___ _inorder(self, root):
        __ root is not None:
            __ root.left is not None:
                self._inorder(root.left)
            self._arr.append(root.val)
            __ root.right is not None:
                self._inorder(root.right)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
