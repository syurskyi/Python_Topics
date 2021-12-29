from json import dumps


class Tree(object):
    ___ __init__(self, label, children=[]):
        self.label = label
        self.children = children

    ___ __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    ___ __str__(self, indent_ N..
        return dumps(self.__dict__(), indent=indent)

    ___ __lt__(self, other):
        return self.label < other.label

    ___ __eq__(self, other):
        return self.__dict__() == other.__dict__()

    ___ __iter__(self):
        yield self.label
        for child in self.children:
            for gchild in child:
                yield gchild

    ___ dup(self):
        return Tree(self.label, [c.dup() for c in self.children])

    ___ add(self, other):
        tree = self.dup()
        tree.children.append(other)
        return tree

    ___ remove(self, node):
        tree = self.dup()
        for child in list(tree.children):
            tree.children.remove(child)
            __ child.label == node:
                break
            tree.children.append(child.remove(node))
        return tree

    ___ from_pov(self, from_node):
        stack = [self]
        visited = set()
        while stack:
            tree = stack.pop(0)
            __ tree.label in visited:
                continue
            visited.add(tree.label)
            __ from_node == tree.label:
                return tree
            for child in tree.children:
                stack.append(child.add(tree.remove(child.label)))
        raise ValueError("Tree could not be reoriented")

    ___ path_to(self, from_node, to_node):
        reordered = self.from_pov(from_node)
        stack = reordered.children
        path = [from_node]
        while path[-1] != to_node:
            try:
                tree = stack.pop()
            except IndexError:
                raise ValueError("No path found")
            __ to_node in tree:
                path.append(tree.label)
                stack = tree.children
        return path
