#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. LRUCache o..
    ___ __init__  capacity
        self.capacity = capacity
        self.cache _ # dict
        self.doubleLinkedList = DoubleLinkedList()
        self.l.. = 0

    ___ get  key
        # Get operator will also update the linked list(Don't forget)
        __ key __ self.cache:
            node = self.cache[key]
            self.doubleLinkedList.delete(node)
            self.doubleLinkedList.append(node)
            r_ self.cache[key].value
        ____
            r_ -1

    ___ s..  key, value
        # update the (key,value) pair in both hash and linked list.
        __ key __ self.cache:
            node = self.cache[key]
            self.doubleLinkedList.delete(node)
            new_node = Node(key, value)
            self.doubleLinkedList.append(new_node)
            self.cache[key] = new_node

        ____
            node = Node(key, value)
            # Add the new node to cache
            __ self.l.. < self.capacity:
                self.doubleLinkedList.append(node)
                self.cache[key] = node
                self.l.. += 1
            # Remove the head of linked list and append the new node
            ____
                replaced_node = self.doubleLinkedList.del_head()
                del self.cache[replaced_node.key]
                self.doubleLinkedList.append(node)
                self.cache[key] = node


c.. Node:
    ___ __init__  key=None, value=None, next_node=None, pre_node=None
        self.key = key
        self.value = value
        self.next = next_node
        self.pre = pre_node


# Double linked list
c.. DoubleLinkedList:
    ___ __init__(self
        self.head = None
        self.tail = None

    ___ append  node
        __ n.. self.head:
            self.head = node
            self.tail = self.head
        ____
            self.tail.next = node
            node.pre = self.tail
            self.tail = node

    ___ delete  node
        __ self.head __ self.tail:
            self.head, self.tail = None, None
        ____ node __ self.head:
            node.next.pre = None
            self.head = node.next
        ____ node __ self.tail:
            node.pre.next = None
            self.tail = node.pre
        ____
            node.pre.next = node.next
            node.next.pre = node.pre

    ___ del_head(self
        del_head = self.head
        self.delete(self.head)
        r_ del_head

"""
if __name__ == '__main__':
    ca = LRUCache(2)
    ca.set(2, 1)
    print "AA", ca.get(2)
    ca.set(2, 2)
    print "BB",  ca.get(2)
    ca.set(3, 3)
    print "CC", ca.get(3)
    # what if: print "CC", ca.get(2)
    ca.set(4, 1)
    print "CC", ca.get(2)
"""
