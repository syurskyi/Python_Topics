class Zipper(object
    @staticmethod
    ___ from_tree(tree
        r_ Zipper(tree, tuple())

    ___ __init__(self, tree, crumbs
        self.tree = tree
        self.crumbs = crumbs

    ___ value(self
        r_ self.tree['value']

    ___ set_value(self, value
        root = {
            'left': self.tree['left'],
            'right': self.tree['right'],
            'value': value
            }
        r_ Zipper(root, self.crumbs)

    ___ left(self
        __ self.tree['left']:
            right = ('left', self.tree['value'], self.tree['right'])
            r_ Zipper(self.tree['left'], self.crumbs + (right,))

    ___ set_left(self, left
        root = {
            'left': left,
            'right': self.tree['right'],
            'value': self.tree['value']
            }
        r_ Zipper(root, self.crumbs)

    ___ right(self
        __ self.tree['right']:
            left = ('right', self.tree['value'], self.tree['left'])
            r_ Zipper(self.tree['right'], self.crumbs + (left,))

    ___ set_right(self, right
        root = {
            'left': self.tree['left'],
            'right': right,
            'value': self.tree['value']
            }
        r_ Zipper(root, self.crumbs)

    ___ up(self
        __ le.(self.crumbs) <= 0:
            r_ None
        direcion, value, tree = self.crumbs[-1]
        root = {
            'value': value,
            direcion: self.tree,
            'left' __ direcion __ 'right' else 'right': tree}
        r_ Zipper(root, self.crumbs[:-1])

    ___ to_tree(self
        stepUp = self.up()
        __ stepUp is None:
            r_ self.tree
        r_ stepUp.to_tree()
