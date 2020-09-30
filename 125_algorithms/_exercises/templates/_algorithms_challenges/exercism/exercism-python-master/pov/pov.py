from json ______ dumps
from itertools ______ chain

class Tree(object
    ___ __init__(self, label, children=None
        self.label = label
        self.children = children or   # list

    ___ __dict__(self
        r_ {self.label: [c.__dict__() ___ c __ sorted(self.children)]}

    ___ __str__(self, indent=None
        r_ dumps(self.__dict__(), indent=indent)

    ___ __lt__(self, other
        r_ self.label < other.label

    ___ __eq__(self, other
        r_ self.__dict__() __ other.__dict__()

    ___ from_pov(self, from_node
        steps = self.find(from_node)
        ___ step __ steps[1:]:
            self.children = [c ___ c __ self.children __ c.label != step.label]
            step.label, self.label = self.label, step.label
            step.children, self.children = self.children, step.children
            self.children.append(step)
        r_ self

    ___ path_to(self, from_node, to_node
        to_path, from_path = self.find(to_node), self.find(from_node)
        r_ list(n.label ___ n __ chain(reversed(from_path), to_path[1:]))

    ___ find(self, to_node
        queue = [(self, tu..())]
        w___ queue:
            node, path = queue.p..
            path += (node,)
            __ node.label __ to_node:
                r_ path
            queue.extend((c, path) ___ c __ node.children)
        raise ValueError("No node {}".format(to_node))
