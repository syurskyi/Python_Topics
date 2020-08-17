class Zipper(object
    @staticmethod
    ___ from_tree(tree
        r_ Zipper(dict(tree), [])

    ___ __init__(self, tree, ancestors
        self.tree = tree
        self.ancestors = ancestors

    ___ value(self
        r_ self.tree['value']

    ___ set_value(self, value
        self.tree['value'] = value
        r_ self

    ___ left(self
        __ self.tree['left'] pa__ None:
            r_ None
        r_ Zipper(self.tree['left'], self.ancestors + [self.tree])

    ___ set_left(self, tree
        self.tree['left'] = tree
        r_ self

    ___ right(self
        __ self.tree['right'] pa__ None:
            r_ None
        r_ Zipper(self.tree['right'], self.ancestors + [self.tree])

    ___ set_right(self, tree
        self.tree['right'] = tree
        r_ self

    ___ up(self
        r_ Zipper(self.ancestors[-1], self.ancestors[:-1])

    ___ to_tree(self
        __ any(self.ancestors
            r_ self.ancestors[0]
        r_ self.tree
