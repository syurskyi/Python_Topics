c_ Node:
    ___  -   value_N..
        value _ value
        next_node _ None

    ___ set_next_node  next_node
        next_node _ next_node

    ___ get_next_node
        r_ next_node


c_ NodeList:
    ___  -   values_N..
        node_head _ None
        for value in values:
            add_node(value)

    ___ add_node  value
        checked_node _ node_head
        __(checked_node is None
            node_head _ Node(value)
        else:
            while(checked_node.get_next_node() is not None
                checked_node _ checked_node.get_next_node()
            checked_node.set_next_node(Node(value))

    ___ print
        checked_node _ node_head
        while(checked_node is not None
            print(checked_node.value)
            checked_node _ checked_node.get_next_node()

    ___ remove_node  position
        checked_node _ node_head
        previous_node _ None
        found _ True
        for count in range(position
            previous_node _ checked_node
            checked_node _ checked_node.get_next_node()
            __(checked_node __ None
                found _ False
                break
        __(found and previous_node is not None
            previous_node.set_next_node(checked_node.get_next_node())

    ___ get_node_value  position
        checked_node _ node_head
        found _ True
        for count in range(position
            checked_node _ checked_node.get_next_node()
            __(checked_node __ None
                found _ False
                break
        __(found
            r_ checked_node.value
        else:
            r_ None

    ___ get_head_node
        r_ node_head
