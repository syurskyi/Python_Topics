class Node(object

    ___ __init__(self, data, next=None
        self.next = next
        self.data = data

    ___ __str__(self
        r_ self.data


class LinkedList(object

    ___ __init__(self, head=None
        self.head = head

    ___ __len__(self
        curr = self.head
        counter = 0
        w___ curr is not None:
            counter += 1
            curr = curr.next
        r_ counter

    ___ insert_to_front(self, data
        __ data is None:
            r_ None
        node = Node(data, self.head)
        self.head = node
        r_ node

    ___ append(self, data
        __ data is None:
            r_ None
        node = Node(data)
        __ self.head is None:
            self.head = node
            r_ node
        curr_node = self.head
        w___ curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        r_ node

    ___ find(self, data
        __ data is None:
            r_ None
        curr_node = self.head
        w___ curr_node is not None:
            __ curr_node.data __ data:
                r_ curr_node
            curr_node = curr_node.next
        r_ None

    ___ delete(self, data
        __ data is None:
            r_
        __ self.head is None:
            r_
        __ self.head.data __ data:
            self.head = self.head.next
            r_
        prev_node = self.head
        curr_node = self.head.next
        w___ curr_node is not None:
            __ curr_node.data __ data:
                prev_node.next = curr_node.next
                r_
            prev_node = curr_node
            curr_node = curr_node.next

    ___ delete_alt(self, data
        __ data is None:
            r_
        __ self.head is None:
            r_
        curr_node = self.head
        __ curr_node.data __ data:
            curr_node = curr_node.next
            r_
        w___ curr_node.next is not None:
            __ curr_node.next.data __ data:
                curr_node.next = curr_node.next.next
                r_
            curr_node = curr_node.next

    ___ print_list(self
        curr_node = self.head
        w___ curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    ___ get_all_data(self
        data = []
        curr_node = self.head
        w___ curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        r_ data