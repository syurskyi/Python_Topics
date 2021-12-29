class List(object):
  @staticmethod
  ___ delete(elem):
    elem.prev.next = elem.next
    elem.next.prev = elem.prev
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
  ___ isEmpty(head):
    r.. head.next __ head.prev __ head

  @staticmethod
  ___ initHead(head):
    head.prev = head.next = head


class Node(object):
  ___ __init__(self, key, value, head):
    self.key = key
    self.value = value
    self.head = head
    self.prev = self.next = N..

  ___ hit(self):
    List.delete(self)
    List.a..(self.head, self)


class LRUCache(object):
  ___ __init__(self, capacity):
    """
    :type capacity: int
    """
    self.d = {}
    self.cap = capacity
    self.head = Node(-1, -1, N..)
    List.initHead(self.head)

  ___ get(self, key):
    """
    :rtype: int
    """
    __ key n.. __ self.d:
      r.. -1
    self.d[key].hit()
    r.. self.d[key].value

  ___ set(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: nothing
    """
    __ self.cap __ 0:
      r..

    __ key __ self.d:
      self.d[key].hit()
      self.d[key].value = value
    ____:
      __ l..(self.d) >= self.cap:
        oldNode = List.delete(self.head.next)
        del self.d[oldNode.key]

      newNode = Node(key, value, self.head)
      List.a..(self.head, newNode)
      self.d[key] = newNode
