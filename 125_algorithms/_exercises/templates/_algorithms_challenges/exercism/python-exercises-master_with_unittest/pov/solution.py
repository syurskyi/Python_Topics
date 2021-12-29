____ json _______ dumps


class Tree(object):
    ___ __init__(self, label, children=[]):
        self.label = label
        self.children = children

    ___ __dict__(self):
        r.. {self.label: [c.__dict__() ___ c __ s..(self.children)]}

    ___ __str__(self, indent_ N..
        r.. dumps(self.__dict__(), indent=indent)

    ___ __lt__(self, other):
        r.. self.label < other.label

    ___ __eq__(self, other):
        r.. self.__dict__() __ other.__dict__()

    ___ __iter__(self):
        y.. self.label
        ___ child __ self.children:
            ___ gchild __ child:
                y.. gchild

    ___ dup(self):
        r.. Tree(self.label, [c.dup() ___ c __ self.children])

    ___ add(self, other):
        tree = self.dup()
        tree.children.a..(other)
        r.. tree

    ___ remove(self, node):
        tree = self.dup()
        ___ child __ l..(tree.children):
            tree.children.remove(child)
            __ child.label __ node:
                break
            tree.children.a..(child.remove(node))
        r.. tree

    ___ from_pov(self, from_node):
        stack = [self]
        visited = set()
        w.... stack:
            tree = stack.pop(0)
            __ tree.label __ visited:
                continue
            visited.add(tree.label)
            __ from_node __ tree.label:
                r.. tree
            ___ child __ tree.children:
                stack.a..(child.add(tree.remove(child.label)))
        raise ValueError("Tree could not be reoriented")

    ___ path_to(self, from_node, to_node):
        reordered = self.from_pov(from_node)
        stack = reordered.children
        path = [from_node]
        w.... path[-1] != to_node:
            try:
                tree = stack.pop()
            except IndexError:
                raise ValueError("No path found")
            __ to_node __ tree:
                path.a..(tree.label)
                stack = tree.children
        r.. path
