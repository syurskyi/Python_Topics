c_ CodeGeneratorVisitor o..
    ?d__.o. 'n..'
    ___ visit  node
        """This is the generic method"""

    @visit.when(ASTNode)
    ___ visit(self, node):
        map(self.visit, node.children)

    @visit.when(EchoStatement)
    ___ visit(self, node):
        self.visit(node.children)
        print "print"

    @visit.when(BinaryExpression)
    ___ visit(self, node):
        map(self.visit, node.children)
        print node.props['operator']

    @visit.when(Constant)
    ___ visit(self, node):
        print "push %d" % node.props['value']

sometree = None
CodeGeneratorVisitor().visit(sometree)
# Output:
# push 1
# print
# push 2
# push 4
# push 3
# multiply
# plus
# print
