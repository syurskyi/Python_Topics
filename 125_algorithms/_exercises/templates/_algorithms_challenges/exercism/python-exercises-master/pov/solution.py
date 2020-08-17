from json ______ dumps


class Tree(object
    ___ __init__(self, label, children=[]
        self.label = label
        self.children = children

    ___ __dict__(self
        r_ {self.label: [c.__dict__() ___ c in sorted(self.children)]}

    ___ __str__(self, indent=None
        r_ dumps(self.__dict__(), indent=indent)

    ___ __lt__(self, other
        r_ self.label < other.label

    ___ __eq__(self, other
        r_ self.__dict__() __ other.__dict__()

    ___ __iter__(self
        yield self.label
        ___ child in self.children:
            ___ gchild in child:
                yield gchild

    ___ dup(self
        r_ Tree(self.label, [c.dup() ___ c in self.children])

    ___ add(self, other
        tree = self.dup()
        tree.children.append(other)
        r_ tree

    ___ remove(self, node
        tree = self.dup()
        ___ child in list(tree.children
            tree.children.remove(child)
            __ child.label __ node:
                break
            tree.children.append(child.remove(node))
        r_ tree

    ___ from_pov(self, from_node
        stack = [self]
        visited = set()
        w___ stack:
            tree = stack.pop(0)
            __ tree.label in visited:
                continue
            visited.add(tree.label)
            __ from_node __ tree.label:
                r_ tree
            ___ child in tree.children:
                stack.append(child.add(tree.remove(child.label)))
        raise ValueError("Tree could not be reoriented")

    ___ path_to(self, from_node, to_node
        reordered = self.from_pov(from_node)
        stack = reordered.children
        path = [from_node]
        w___ path[-1] != to_node:
            try:
                tree = stack.p..
            except IndexError:
                raise ValueError("No path found")
            __ to_node in tree:
                path.append(tree.label)
                stack = tree.children
        r_ path
