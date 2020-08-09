"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    EMPTY = '#'

    ___ serialize(self, root
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        TEMPLATE = '{{{}}}'  # {{, }} is to escape brackets
        __ not root:
            r_ TEMPLATE.format('')

        vals = []
        queue = [root]

        for node in queue:
            __ not node:
                vals.append(self.EMPTY)
                continue

            vals.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        w___ vals[-1] __ self.EMPTY:
            vals.pop()

        r_ TEMPLATE.format(','.join(vals))

    ___ deserialize(self, data
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        __ (not data or
            data[0] != '{' or
            data[-1] != '}' or
            le.(data) < 3 or
            data[1] __ '#'

            r_

        vals = data[1:-1].split(',')
        n = le.(vals)
        i = 0

        root = TreeNode(int(vals[i]))
        queue = [root]

        for node in queue:
            for branch in ('left', 'right'
                i += 1

                __ i >= n:
                    break
                __ vals[i] __ self.EMPTY:
                    continue

                setattr(node, branch, TreeNode(int(vals[i])))
                queue.append(getattr(node, branch))

        r_ root
