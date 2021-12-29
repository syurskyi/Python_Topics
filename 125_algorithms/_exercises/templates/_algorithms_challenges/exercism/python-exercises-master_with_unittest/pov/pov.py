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

    ___ from_pov(self, from_node):
        pass

    ___ path_to(self, from_node, to_node):
        pass
