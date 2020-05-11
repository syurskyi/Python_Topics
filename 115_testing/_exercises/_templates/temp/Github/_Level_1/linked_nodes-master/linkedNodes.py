c_ Node
    ___  -   value_N..
        value _ value
        next_node _ N..

    ___ set_next_node  next_node
        next_node _ next_node

    ___ get_next_node
        r_ next_node


c_ NodeList
    ___  -   values_N..
        node_head _ N..
        ___ value __ values:
            add_node(value)

    ___ add_node  value
        checked_node _ node_head
        __(checked_node __ N..
            node_head _ Node(value)
        ____:
            w__(checked_node.get_next_node() __ no. N..
                checked_node _ checked_node.get_next_node()
            checked_node.set_next_node(Node(value))

    ___ print
        checked_node _ node_head
        w__(checked_node __ no. N..
            print(checked_node.value)
            checked_node _ checked_node.get_next_node()

    ___ remove_node  position
        checked_node _ node_head
        previous_node _ N..
        found _ T..
        ___ count __ ra..(position
            previous_node _ checked_node
            checked_node _ checked_node.get_next_node()
            __(checked_node __ N..
                found _ F..
                break
        __(found an. previous_node __ no. N..
            previous_node.set_next_node(checked_node.get_next_node())

    ___ get_node_value  position
        checked_node _ node_head
        found _ T..
        ___ count __ ra..(position
            checked_node _ checked_node.get_next_node()
            __(checked_node __ N..
                found _ F..
                break
        __(found
            r_ checked_node.value
        ____:
            r_ N..

    ___ get_head_node
        r_ node_head
