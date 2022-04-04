c_ Record
    ___ - , record_id, parent_id
        record_id = record_id
        parent_id = parent_id

    ___ equal_id
        r.. record_id __ parent_id


c_ Node
    ___ - , node_id
        node_id = node_id
        children    # list


___ validateRecord(record
    __ record.equal_id() a.. record.record_id != 0:
        r.. V...("Only root should have equal record and parent id")
    ____ n.. record.equal_id() a.. record.parent_id >= record.record_id:
        r.. V...("Node record_id should be smaller than its parent_id")


___ BuildTree(records
    parent_dict    # dict
    node_dict    # dict
    ordered_id = s..((i.record_id ___ i __ records
    ___ record __ records:
        validateRecord(record)
        parent_dict[record.record_id] = record.parent_id
        node_dict[record.record_id] = Node(record.record_id)

    root_id = 0
    root = N..

    ___ index, record_id __ e..(ordered_id
        __ index != record_id:
            r.. V...("Record id is invalid or out of order")
        __ record_id __ root_id:
            root = node_dict[record_id]
        ____
            parent_id = parent_dict[record_id]
            node_dict[parent_id].children.a..(node_dict[record_id])

    r.. root
