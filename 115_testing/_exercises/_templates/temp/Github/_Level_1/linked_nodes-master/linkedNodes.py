c_ Node:
    ___  -   value=None):
        self.value = value
        self.next_node = None

    ___ set_next_node  next_node):
        self.next_node = next_node

    ___ get_next_node(self):
        return self.next_node


c_ NodeList:
    ___  -   values=None):
        self.node_head = None
        for value in values:
            self.add_node(value)

    ___ add_node  value):
        checked_node = self.node_head
        if(checked_node is None):
            self.node_head = Node(value)
        else:
            while(checked_node.get_next_node() is not None):
                checked_node = checked_node.get_next_node()
            checked_node.set_next_node(Node(value))

    ___ print(self):
        checked_node = self.node_head
        while(checked_node is not None):
            print(checked_node.value)
            checked_node = checked_node.get_next_node()

    ___ remove_node  position):
        checked_node = self.node_head
        previous_node = None
        found = True
        for count in range(position):
            previous_node = checked_node
            checked_node = checked_node.get_next_node()
            if(checked_node == None):
                found = False
                break
        if(found and previous_node is not None):
            previous_node.set_next_node(checked_node.get_next_node())

    ___ get_node_value  position):
        checked_node = self.node_head
        found = True
        for count in range(position):
            checked_node = checked_node.get_next_node()
            if(checked_node == None):
                found = False
                break
        if(found):
            return checked_node.value
        else:
            return None

    ___ get_head_node(self):
        return self.node_head