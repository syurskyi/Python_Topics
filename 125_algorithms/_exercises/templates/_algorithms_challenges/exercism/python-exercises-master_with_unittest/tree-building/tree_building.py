c_ Record
    ___ - , record_id, parent_id
        record_id record_id
        parent_id parent_id


c_ Node
    ___ - , node_id
        node_id node_id
        children    # list


___ BuildTree(records
    root N..
    records.s..(key=l.... x: x.record_id)
    ordered_id [i.record_id ___ i __ records]
    __ records:
        __ ordered_id[-1] !_ l..(ordered_id) - 1:
            r.. V...
        __ ordered_id[0] !_ 0:
            r.. V...
    trees    # list
    parent    # dict
    ___ i __ r..(l..(ordered_id:
        ___ j __ records:
            __ ordered_id[i] __ j.record_id:
                __ j.record_id __ 0:
                    __ j.parent_id !_ 0:
                        r.. V...
                __ j.record_id < j.parent_id:
                    r.. V...
                __ j.record_id __ j.parent_id:
                    __ j.record_id !_ 0:
                        r.. V...
                trees.a..(Node(ordered_id[i]
    ___ i __ r..(l..(ordered_id:
        ___ j __ trees:
            __ i __ j.node_id:
                parent j
        ___ j __ records:
            __ j.parent_id __ i:
                ___ k __ trees:
                    __ k.node_id __ 0:
                        _____
                    __ j.record_id __ k.node_id:
                        child k
                        parent.children.a..(child)
    __ l..(trees) > 0:
        root trees[0]
    r.. root
