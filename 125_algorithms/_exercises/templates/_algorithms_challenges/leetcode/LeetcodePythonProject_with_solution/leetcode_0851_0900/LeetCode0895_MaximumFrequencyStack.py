import heapq


class FreqStack(object):

    ___ __init__(self):
        self.hashmap = {}
        self.heap = []
        self.size = 0

    ___ push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.size += 1
        self.hashmap[x] = self.hashmap.get(x, 0) + 1
        heapq.heappush(self.heap, (-self.hashmap[x], -self.size, x))

    ___ pop(self):
        """
        :rtype: int
        """
        _, _, val = heapq.heappop(self.heap)
        self.hashmap[val] -= 1
        return val


class ListNode(object):
    ___ __init__(self, val):
        self.val = val
        self.freq = 0
        self.prev = None
        self.next = None
        self.indexes = []


class FreqStack_self(object):

    ___ __init__(self):
        self.idx = 0
        self.hashmap = {}
        self.head = None
        self.tail = None
        self.idx = 0

    ___ push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.idx += 1
        __ x not in self.hashmap:
            node = ListNode(x)
            self.hashmap[x] = node
        else:
            node = self.hashmap[x]
        node.freq += 1
        node.indexes.append(self.idx)
        __ not self.head:
            self.head = node
            self.tail = node
        else:
            node0 = node.next
            while node0 and node0.freq <= node.freq:
                node0 = node0.next
            __ node0:
                nextNode = node0.next
                node0.next = node
                node.next = nextNode
            else:
                self.tail.next = node

    ___ pop(self):
        """
        :rtype: int
        """
        node = self.tail
        node.freq -= 1
        node.indexes.pop()
        val = node.val
        __ node.freq == 0:
            del self.hashmap[val]
            prevNode = node.prev
            nextNode = node.next
            __ prevNode:
                prevNode.next = nextNode
                __ nextNode:
                    nextNode.prev = prevNode
                else:
                    self.tail = prevNode
            else:
                self.head = nextNode
                __ nextNode:
                    nextNode.prev = prevNode
                else:
                    self.head = None
                    self.tail = None
        else:
            node0 = node.prev
            while node0 and (node0.freq > node.freq or
                             (node0.freq == node.freq and
                              node0.indexes[-1] > node.indexes[-1])):
                node0 = node0.prev
            __ node0 and node0 != node:
                prevNode = node0.prev
                node0.prev = node
                node.prev = prevNode
            else:
                self.head.prev = node
        return val


__ __name__ == '__main__':
    freqStack = FreqStack()
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(4)
    freqStack.push(5)
    print(freqStack.pop())
    print(freqStack.pop())
    print(freqStack.pop())
    print(freqStack.pop())
