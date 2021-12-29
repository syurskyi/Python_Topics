class Record():
    ___ __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

    ___ equal_id(self):
        r.. self.record_id __ self.parent_id


class Node():
    ___ __init__(self, node_id):
        self.node_id = node_id
        self.children    # list


___ validateRecord(record):
    __ record.equal_id() and record.record_id != 0:
        raise ValueError("Only root should have equal record and parent id")
    ____ n.. record.equal_id() and record.parent_id >= record.record_id:
        raise ValueError("Node record_id should be smaller than its parent_id")


___ BuildTree(records):
    parent_dict = {}
    node_dict = {}
    ordered_id = s..((i.record_id ___ i __ records))
    ___ record __ records:
        validateRecord(record)
        parent_dict[record.record_id] = record.parent_id
        node_dict[record.record_id] = Node(record.record_id)

    root_id = 0
    root = N..

    ___ index, record_id __ enumerate(ordered_id):
        __ index != record_id:
            raise ValueError("Record id is invalid or out of order")
        __ record_id __ root_id:
            root = node_dict[record_id]
        ____:
            parent_id = parent_dict[record_id]
            node_dict[parent_id].children.a..(node_dict[record_id])

    r.. root
