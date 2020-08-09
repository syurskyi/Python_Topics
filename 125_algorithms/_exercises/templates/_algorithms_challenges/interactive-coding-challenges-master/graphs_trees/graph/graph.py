from enum ______ Enum  # Python 2 users: Run pip install enum34


class State(Enum
    unvisited = 0
    visiting = 1
    visited = 2


class Node:

    ___ __init__(self, key
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    ___ __repr__(self
        r_ str(self.key)

    ___ __lt__(self, other
        r_ self.key < other.key

    ___ add_neighbor(self, neighbor, weight=0
        __ neighbor is None or weight is None:
            raise TypeError('neighbor or weight cannot be None')
        neighbor.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    ___ remove_neighbor(self, neighbor
        __ neighbor is None:
            raise TypeError('neighbor cannot be None')
        __ neighbor.key not in self.adj_nodes:
            raise KeyError('neighbor not found')
        neighbor.incoming_edges -= 1
        del self.adj_weights[neighbor.key]
        del self.adj_nodes[neighbor.key]


class Graph:

    ___ __init__(self
        self.nodes = {}  # Key = key, val = Node

    ___ add_node(self, key
        __ key is None:
            raise TypeError('key cannot be None')
        __ key not in self.nodes:
            self.nodes[key] = Node(key)
        r_ self.nodes[key]

    ___ add_edge(self, source_key, dest_key, weight=0
        __ source_key is None or dest_key is None:
            raise KeyError('Invalid key')
        __ source_key not in self.nodes:
            self.add_node(source_key)
        __ dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)

    ___ add_undirected_edge(self, src_key, dst_key, weight=0
        __ src_key is None or dst_key is None:
            raise TypeError('key cannot be None')
        self.add_edge(src_key, dst_key, weight)
        self.add_edge(dst_key, src_key, weight)