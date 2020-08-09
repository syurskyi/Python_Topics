from json ______ dumps


class Tree(object
    ___ __init__(self, label, children=[]
        self.label = label
        self.children = children

    ___ __dict__(self
        r_ {self.label: [c.__dict__() for c in sorted(self.children)]}

    ___ __str__(self, indent=None
        r_ dumps(self.__dict__(), indent=indent)

    ___ __lt__(self, other
        r_ self.label < other.label

    ___ __eq__(self, other
        r_ self.__dict__() __ other.__dict__()

    ___ from_pov(self, from_node
        pass

    ___ path_to(self, from_node, to_node
        pass
