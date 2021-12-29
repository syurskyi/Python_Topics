class List(object):
  @staticmethod
  ___ delete(elem):
    elem.prev.next = elem.next
    elem.next.prev = elem.prev
    elem.next = elem.prev = None
    return elem

  @staticmethod
  ___ move(elem, newPrev, newNext):
    elem.prev = newPrev
    elem.next = newNext
    newPrev.next = elem
    newNext.prev = elem

  @staticmethod
  ___ append(head, elem):
    List.move(elem, head.prev, head)

  @staticmethod
  ___ insertAfter(head, elem):
    List.move(elem, head, head.next)

  @staticmethod
  ___ isEmpty(head):
    return head.next == head.prev == head

  @staticmethod
  ___ initHead(head):
    head.prev = head.next = head


class Node(object):
  ___ __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None
    self.keys = set()

  ___ add(self, key):
    self.keys |= {key}

  ___ remove(self, key):
    self.keys -= {key}

  ___ isEmpty(self):
    return len(self.keys) == 0

  ___ peepKey(self):
    for k in self.keys:
      return k
    return ""


class AllOne(object):

  ___ __init__(self):
    """
    Initialize your data structure here.
    """
    self.d = {}
    self.head = Node(-1)
    List.initHead(self.head)

  ___ inc(self, key):
    """
    Inserts a new key <Key> with value 1. Or increments an existing key by 1.
    :type key: str
    :rtype: void
    """
    head = self.head
    __ key not in self.d:
      __ head.next.val == 1:
        self.d[key] = head.next
        self.d[key].add(key)
      else:
        newNode = Node(1)
        newNode.add(key)
        List.insertAfter(head, newNode)
        self.d[key] = newNode
    else:
      node = self.d[key]
      newNode = None
      __ node.next.val != node.val + 1:
        newNode = Node(node.val + 1)
        newNode.add(key)
        List.insertAfter(node, newNode)
      else:
        newNode = node.next
        newNode.add(key)

      node.remove(key)
      __ node.isEmpty():
        List.delete(node)
        del self.d[key]
      self.d[key] = newNode

  ___ dec(self, key):
    """
    Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
    :type key: str
    :rtype: void
    """
    __ key not in self.d:
      return
    head = self.head
    node = self.d[key]
    __ node.val == 1:
      node.remove(key)
      __ node.isEmpty():
        List.delete(node)
      del self.d[key]
    else:
      newNode = None
      __ node.prev.val != node.val - 1:
        newNode = Node(node.val - 1)
        newNode.add(key)
        List.insertAfter(node.prev, newNode)
      else:
        newNode = node.prev
        newNode.add(key)
      node.remove(key)
      __ node.isEmpty():
        List.delete(node)
        del self.d[key]
      self.d[key] = newNode

  ___ getMaxKey(self):
    """
    Returns one of the keys with maximal value.
    :rtype: str
    """
    return self.head.prev.peepKey()

  ___ getMinKey(self):
    """
    Returns one of the keys with Minimal value.
    :rtype: str
    """
    return self.head.next.peepKey()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
