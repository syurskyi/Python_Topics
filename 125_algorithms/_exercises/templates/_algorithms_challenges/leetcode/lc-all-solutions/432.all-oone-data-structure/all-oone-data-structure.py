c_ List(o..):
  @staticmethod
  ___ delete(elem):
    elem.prev.next = elem.next
    elem.next.prev = elem.prev
    elem.next = elem.prev = N..
    r.. elem

  @staticmethod
  ___ move(elem, newPrev, newNext):
    elem.prev = newPrev
    elem.next = newNext
    newPrev.next = elem
    newNext.prev = elem

  @staticmethod
  ___ a..(head, elem):
    List.move(elem, head.prev, head)

  @staticmethod
  ___ insertAfter(head, elem):
    List.move(elem, head, head.next)

  @staticmethod
  ___ isEmpty(head):
    r.. head.next __ head.prev __ head

  @staticmethod
  ___ initHead(head):
    head.prev = head.next = head


c_ Node(o..):
  ___ - , val):
    val = val
    prev = N..
    next = N..
    keys = s..()

  ___ add  key):
    keys |= {key}

  ___ remove  key):
    keys -= {key}

  ___ isEmpty
    r.. l..(keys) __ 0

  ___ peepKey
    ___ k __ keys:
      r.. k
    r.. ""


c_ AllOne(o..):

  ___ - ):
    """
    Initialize your data structure here.
    """
    d    # dict
    head = Node(-1)
    List.initHead(head)

  ___ inc  key):
    """
    Inserts a new key <Key> with value 1. Or increments an existing key by 1.
    :type key: str
    :rtype: void
    """
    head = head
    __ key n.. __ d:
      __ head.next.val __ 1:
        d[key] = head.next
        d[key].add(key)
      ____:
        newNode = Node(1)
        newNode.add(key)
        List.insertAfter(head, newNode)
        d[key] = newNode
    ____:
      node = d[key]
      newNode = N..
      __ node.next.val != node.val + 1:
        newNode = Node(node.val + 1)
        newNode.add(key)
        List.insertAfter(node, newNode)
      ____:
        newNode = node.next
        newNode.add(key)

      node.remove(key)
      __ node.isEmpty
        List.delete(node)
        del d[key]
      d[key] = newNode

  ___ dec  key):
    """
    Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
    :type key: str
    :rtype: void
    """
    __ key n.. __ d:
      r..
    head = head
    node = d[key]
    __ node.val __ 1:
      node.remove(key)
      __ node.isEmpty
        List.delete(node)
      del d[key]
    ____:
      newNode = N..
      __ node.prev.val != node.val - 1:
        newNode = Node(node.val - 1)
        newNode.add(key)
        List.insertAfter(node.prev, newNode)
      ____:
        newNode = node.prev
        newNode.add(key)
      node.remove(key)
      __ node.isEmpty
        List.delete(node)
        del d[key]
      d[key] = newNode

  ___ getMaxKey
    """
    Returns one of the keys with maximal value.
    :rtype: str
    """
    r.. head.prev.peepKey()

  ___ getMinKey
    """
    Returns one of the keys with Minimal value.
    :rtype: str
    """
    r.. head.next.peepKey()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
