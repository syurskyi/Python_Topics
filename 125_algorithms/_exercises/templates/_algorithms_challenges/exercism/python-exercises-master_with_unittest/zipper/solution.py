class Zipper(object):
    @staticmethod
    ___ from_tree(tree):
        return Zipper(dict(tree), [])

    ___ __init__(self, tree, ancestors):
        self.tree = tree
        self.ancestors = ancestors

    ___ value(self):
        return self.tree['value']

    ___ set_value(self, value):
        self.tree['value'] = value
        return self

    ___ left(self):
        __ self.tree['left'] is None:
            return None
        return Zipper(self.tree['left'], self.ancestors + [self.tree])

    ___ set_left(self, tree):
        self.tree['left'] = tree
        return self

    ___ right(self):
        __ self.tree['right'] is None:
            return None
        return Zipper(self.tree['right'], self.ancestors + [self.tree])

    ___ set_right(self, tree):
        self.tree['right'] = tree
        return self

    ___ up(self):
        return Zipper(self.ancestors[-1], self.ancestors[:-1])

    ___ to_tree(self):
        __ any(self.ancestors):
            return self.ancestors[0]
        return self.tree
