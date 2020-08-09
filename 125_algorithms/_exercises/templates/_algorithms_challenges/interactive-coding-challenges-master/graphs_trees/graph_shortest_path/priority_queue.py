______ sys


class PriorityQueueNode(object

    ___ __init__(self, obj, key
        self.obj = obj
        self.key = key

    ___ __repr__(self
        r_ str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object

    ___ __init__(self
        self.queue = []

    ___ insert(self, node
        __ node is not None:
            self.queue.append(node)
            r_ self.queue[-1]
        r_ None

    ___ extract_min(self
        __ not self.queue:
            r_ None
        minimum = sys.maxsize
        for index, node in enumerate(self.queue
            __ node.key < minimum:
                minimum = node.key
                minimum_index = index
        node = self.queue.pop(minimum_index)
        r_ node.obj

    ___ decrease_key(self, obj, new_key
        for node in self.queue:
            __ node.obj is obj:
                node.key = new_key
                r_ node
        r_ None