_______ heapq


c_ FreqStack(o..

    ___ -
        hashmap    # dict
        heap    # list
        size = 0

    ___ push  x
        """
        :type x: int
        :rtype: None
        """
        size += 1
        hashmap[x] = hashmap.get(x, 0) + 1
        heapq.heappush(heap, (-hashmap[x], -size, x))

    ___ pop
        """
        :rtype: int
        """
        _, _, val = heapq.heappop(heap)
        hashmap[val] -= 1
        r.. val


c_ ListNode(o..
    ___ - , val
        val = val
        freq = 0
        prev = N..
        next = N..
        indexes    # list


c_ FreqStack_self(o..

    ___ -
        idx = 0
        hashmap    # dict
        head = N..
        tail = N..
        idx = 0

    ___ push  x
        """
        :type x: int
        :rtype: None
        """
        idx += 1
        __ x n.. __ hashmap:
            node = ListNode(x)
            hashmap[x] = node
        ____:
            node = hashmap[x]
        node.freq += 1
        node.indexes.a..(idx)
        __ n.. head:
            head = node
            tail = node
        ____:
            node0 = node.next
            w.... node0 a.. node0.freq <= node.freq:
                node0 = node0.next
            __ node0:
                nextNode = node0.next
                node0.next = node
                node.next = nextNode
            ____:
                tail.next = node

    ___ pop
        """
        :rtype: int
        """
        node = tail
        node.freq -= 1
        node.indexes.pop()
        val = node.val
        __ node.freq __ 0:
            del hashmap[val]
            prevNode = node.prev
            nextNode = node.next
            __ prevNode:
                prevNode.next = nextNode
                __ nextNode:
                    nextNode.prev = prevNode
                ____:
                    tail = prevNode
            ____:
                head = nextNode
                __ nextNode:
                    nextNode.prev = prevNode
                ____:
                    head = N..
                    tail = N..
        ____:
            node0 = node.prev
            w.... node0 a.. (node0.freq > node.freq o.
                             (node0.freq __ node.freq a..
                              node0.indexes[-1] > node.indexes[-1])):
                node0 = node0.prev
            __ node0 a.. node0 != node:
                prevNode = node0.prev
                node0.prev = node
                node.prev = prevNode
            ____:
                head.prev = node
        r.. val


__ _____ __ _____
    freqStack = FreqStack()
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(4)
    freqStack.push(5)
    print(freqStack.pop
    print(freqStack.pop
    print(freqStack.pop
    print(freqStack.pop
