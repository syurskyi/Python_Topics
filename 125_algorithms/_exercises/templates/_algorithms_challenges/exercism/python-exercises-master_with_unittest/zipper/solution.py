class Zipper(object):
    @staticmethod
    ___ from_tree(tree):
        r.. Zipper(d..(tree), [])

    ___ __init__(self, tree, ancestors):
        self.tree = tree
        self.ancestors = ancestors

    ___ value(self):
        r.. self.tree['value']

    ___ set_value(self, value):
        self.tree['value'] = value
        r.. self

    ___ left(self):
        __ self.tree['left'] __ N..
            r.. N..
        r.. Zipper(self.tree['left'], self.ancestors + [self.tree])

    ___ set_left(self, tree):
        self.tree['left'] = tree
        r.. self

    ___ right(self):
        __ self.tree['right'] __ N..
            r.. N..
        r.. Zipper(self.tree['right'], self.ancestors + [self.tree])

    ___ set_right(self, tree):
        self.tree['right'] = tree
        r.. self

    ___ up(self):
        r.. Zipper(self.ancestors[-1], self.ancestors[:-1])

    ___ to_tree(self):
        __ any(self.ancestors):
            r.. self.ancestors[0]
        r.. self.tree
