class Record(
    ___ __init__(self, record_id, parent_id
        self.record_id = record_id
        self.parent_id = parent_id


class Node(
    ___ __init__(self, node_id
        self.node_id = node_id
        self.children =   # list


___ BuildTree(records
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id ___ i __ records]
    __ records:
        __ ordered_id[-1] != le.(ordered_id) - 1:
            raise ValueError
        __ ordered_id[0] != 0:
            raise ValueError
    trees =   # list
    parent = {}
    ___ i __ range(le.(ordered_id)):
        ___ j __ records:
            __ ordered_id[i] __ j.record_id:
                __ j.record_id __ 0:
                    __ j.parent_id != 0:
                        raise ValueError
                __ j.record_id < j.parent_id:
                    raise ValueError
                __ j.record_id __ j.parent_id:
                    __ j.record_id != 0:
                        raise ValueError
                trees.append(Node(ordered_id[i]))
    ___ i __ range(le.(ordered_id)):
        ___ j __ trees:
            __ i __ j.node_id:
                parent = j
        ___ j __ records:
            __ j.parent_id __ i:
                ___ k __ trees:
                    __ k.node_id __ 0:
                        continue
                    __ j.record_id __ k.node_id:
                        child = k
                        parent.children.append(child)
    __ le.(trees) > 0:
        root = trees[0]
    r_ root
