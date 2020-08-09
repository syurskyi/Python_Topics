______ sys


class PriorityQueueNode(object

    ___ __init__(self, obj, key
        self.obj = obj
        self.key = key

    ___ __repr__(self
        r_ str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object

    ___ __init__(self
        self.array = []

    ___ __len__(self
        r_ le.(self.array)

    ___ insert(self, node
        self.array.append(node)
        r_ self.array[-1]

    ___ extract_min(self
        __ not self.array:
            r_ None
        minimum = sys.maxsize
        for index, node in enumerate(self.array
            __ node.key < minimum:
                minimum = node.key
                minimum_index = index
        r_ self.array.pop(minimum_index)

    ___ decrease_key(self, obj, new_key
        for node in self.array:
            __ node.obj is obj:
                node.key = new_key
                r_ node
        r_ None