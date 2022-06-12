c_ MyHashMap o..

    # https://leetcode.com/problems/design-hashmap/discuss/152746/Java-Solution
    ___ - ____:
        """
        Initialize your data structure here.
        """
        size = 10000
        nodes = [N..] * size

    ___ put  key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = hash(key) % size
        __ nodes[index] is N..:
            nodes[index] = ListNode(-1, -1)
        prev = find(nodes[index], key)
        __ prev.next is N..:
            prev.next = ListNode(key, value)
        ____
            prev.next.val = value

    ___ get  key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = hash(key) % size
        __ nodes[index] is N..:
            r_ -1
        prev = find(nodes[index], key)
        __ prev.next is N..:
            r_ -1
        ____
            r_ prev.next.val

    ___ remove  key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = hash(key) % size
        __ nodes[index] is N..:
            r_
        prev = find(nodes[index], key)
        __ prev.next is N..:
            r_
        prev.next = prev.next.next


___ find(bucket, key):
    # find prev node of this key
    node = bucket
    prev = N..
    w.. node is not N.. and node.key != key:
        prev = node
        node = node.next
    r_ prev


# Basic node in hash map
c_ ListNode():

    ___ -  key, val):
        key = key
        val = val
        next = N..


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)