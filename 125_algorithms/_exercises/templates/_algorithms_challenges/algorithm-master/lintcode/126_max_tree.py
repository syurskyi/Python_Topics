"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    """
    Assuming A = [2,5,6,0,3,1]
    step1/ val: 2, stack: [2]
    step2/ val: 5, stack: [5{2,}]
    step3/ val: 6, stack: [6{5{2,},}]
    step4/ val: 0, stack: [6{5{2,},0}, 0]
    step5/ val: 3, stack: [6{5{2,},3{0,}}, 3{0,}]
    step6/ val: 1, stack: [6{5{2,},3{0,1}}, 3{0,1}, 1]
    """
    ___ maxTree  A):
        stack    # list
        ___ val __ A:
            node = TreeNode(val)
            w.... stack a.. val > stack[-1].val:
                node.left = stack.pop()

            # current val less than the last node in stack
            __ stack:
                stack[-1].right = node

            stack.a..(node)
        r.. stack[0]
