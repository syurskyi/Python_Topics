from collections ______ defaultdict

class Record(
    ___ __init__(self, record_id, parent_id
        self.record_id = record_id
        self.parent_id = parent_id


class Node(
    ___ __init__(self, node_id
        self.node_id = node_id
        self.children = []


___ BuildTree(records
    nodes = {}
    parents = defaultdict(list)
    max_id = 0
    ___ n_nodes, record in enumerate(records
        __ (record.record_id __ record.parent_id != 0) or \
            record.record_id < record.parent_id:
            raise ValueError("Invalid record {}".format(record))
        node = Node(record.record_id)
        nodes[record.record_id] = node
        max_id = max(max_id, node.node_id)
        node.children = parents[node.node_id]
        __ node.node_id != 0:
            parents[record.parent_id].append(node)
            parents[record.parent_id].sort(key=lambda n: n.node_id)

    __ nodes __ {}:
        r_ None
    ____ 0 not in nodes:
        raise ValueError("No root node")
    ____ n_nodes != max(nodes.keys()):
        raise ValueError("To many nodes")

    r_ nodes[0]
