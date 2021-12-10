# #!/usr/bin/env python
# '''
# This example demonstrates a simple use of pycallgraph.
# '''
# from pycallgraph ______ PyCallGraph
# from pycallgraph.output ______ GraphvizOutput
#
#
# class Banana:
#
#     ___ eat(self):
#         pass
# py
#
# class Person:
#
#     ___ __init__(self):
#         self.no_bananas()
#
#     ___ no_bananas(self):
#         self.bananas = []
#
#     ___ add_banana(self, banana):
#         self.bananas.append(banana)
#
#     ___ eat_bananas(self):
#         [banana.eat() ___ banana __ self.bananas]
#         self.no_bananas()
#
#
# ___ main():
#     graphviz = GraphvizOutput()
#     graphviz.output_file = 'basic.png'
#
#     with PyCallGraph(output=graphviz):
#         person = Person()
#         ___ a __ xrange(10):
#             person.add_banana(Banana())
#         person.eat_bananas()
#
#
# __ _____ __ ______
#     main()