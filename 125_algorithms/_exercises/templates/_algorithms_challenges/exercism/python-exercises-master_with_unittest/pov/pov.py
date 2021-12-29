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

    ___ from_pov(self, from_node):
        pass

    ___ path_to(self, from_node, to_node):
        pass
