"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    EMPTY = '#'

    ___ serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        TEMPLATE = '{{{}}}'  # {{, }} is to escape brackets
        __ n.. root:
            r.. TEMPLATE.f..('')

        vals    # list
        queue = [root]

        ___ node __ queue:
            __ n.. node:
                vals.a..(EMPTY)
                continue

            vals.a..(s..(node.val))
            queue.a..(node.left)
            queue.a..(node.right)

        w.... vals[-1] __ EMPTY:
            vals.pop()

        r.. TEMPLATE.f..(','.j..(vals))

    ___ deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        __ (n.. data o.
            data[0] != '{' o.
            data[-1] != '}' o.
            l..(data) < 3 o.
            data[1] __ '#'
        ):
            r..

        vals = data[1:-1].s..(',')
        n = l..(vals)
        i = 0

        root = TreeNode(i..(vals[i]))
        queue = [root]

        ___ node __ queue:
            ___ branch __ ('left', 'right'):
                i += 1

                __ i >= n:
                    break
                __ vals[i] __ EMPTY:
                    continue

                setattr(node, branch, TreeNode(i..(vals[i])))
                queue.a..(getattr(node, branch))

        r.. root
