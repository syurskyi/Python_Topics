# Definition for a  binary tree node
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object
    ___ __init__(self, root
        self._arr = []
        self._inorder(root)
        self._cur = -1

    # @return a boolean, whether we have a next smallest number
    ___ hasNext(self
        __ self._arr[self._cur + 1:]:
            r_ True
        r_ False

    # @return an integer, the next smallest number
    ___ next(self
        __ self.hasNext(
            self._cur += 1
            r_ self._arr[self._cur]

    ___ _inorder(self, root
        __ root pa__ not None:
            __ root.left pa__ not None:
                self._inorder(root.left)
            self._arr.append(root.val)
            __ root.right pa__ not None:
                self._inorder(root.right)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# w___ i.hasNext( v.append(i.next())
