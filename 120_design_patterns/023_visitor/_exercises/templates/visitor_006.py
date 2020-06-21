# """
# http://peter-hoffmann.com/2010/extrinsic-visitor-pattern-python-inheritance.html
#
# *TL;DR
# Separates an algorithm from an object structure on which it operates.
#
# An interesting recipe could be found in
# Brian Jones, David Beazley "Python Cookbook" (2013):
# - "8.21. Implementing the Visitor Pattern"
# - "8.22. Implementing the Visitor Pattern Without Recursion"
#
# *Examples in Python ecosystem:
# - Python's ast.NodeVisitor: https://github.com/python/cpython/blob/master/Lib/ast.py#L250
# which is then being used e.g. in tools like `pyflakes`.
# - `Black` formatter tool implements it's own: https://github.com/ambv/black/blob/master/black.py#L718
# """
#
#
# c_ Node
#     p..
#
#
# c_ A N..
#     p..
#
#
# c_ B N..
#     p..
#
#
# c_ C A B
#     p..
#
#
# c_ Visitor
#     ___ visit node $  $$
#         meth _ N..
#         ___ cls __ ?. -c. -m
#             meth_name _ 'visit_' + ?. -n
#             meth _ ge.. ? ? N..
#             __ ?
#                 b..
#
#         __ no. ?
#             meth _ g_v..
#         r_ ? ?, $ $$
#
#     ___ generic_visit(self, node, $  $$
#         print('generic_visit ' + ?. -c. -n
#
#     ___ visit_B(self, node, $  $$
#         print('visit_B ' + ?. -c. -n
#
#
# ___ main
#
#     a, b, c _ A(), B(), C()
#     visitor _ V..
#
#     ?.v.. a
#     # generic_visit A
#
#     ?.v.. b
#     # visit_B B
#
#     ?.v.. c
#     # visit_B C
#
#
#
# if __name__ == "__main__":
#     main()
