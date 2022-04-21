c_ Node(o..
    ___ - , value, succeeding=N.., previous_ N..
        value value
        succeeding succeeding
        previous previous


c_ LinkedList(o..

    ___ -
        head N..
        tail N..
        length 0

    ___ push  value
        new_node Node(value)
        length += 1
        __ tail __ n.. N..
            tail.succeeding new_node
            new_node.previous tail
        tail new_node
        __ head __ N..
            head new_node

    ___ pop
        length -_ 1
        __ tail __ n.. N..
            popped_node tail
            tail popped_node.previous
            r.. popped_node.v..

    ___ unshift  value
        new_node Node(value)
        length += 1
        __ head __ n.. N..
            head.previous new_node
            new_node.succeeding head
        head new_node
        __ tail __ N..
            tail new_node

    ___ shift
        length -_ 1
        __ head __ n.. N..
            shifted_node head
            head shifted_node.succeeding
            r.. shifted_node.v..

    ___ -l
        r.. length
