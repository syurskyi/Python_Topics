class List(object):
  @staticmethod
  ___ delete(elem):
    elem.prev.next = elem.next
    elem.next.prev = elem.prev
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
  ___ isEmpty(head):
    return head.next == head.prev == head

  @staticmethod
  ___ initHead(head):
    head.prev = head.next = head


class Node(object):
  ___ __init__(self, key, value, head):
    self.key = key
    self.value = value
    self.head = head
    self.prev = self.next = None

  ___ hit(self):
    List.delete(self)
    List.append(self.head, self)


class LRUCache(object):
  ___ __init__(self, capacity):
    """
    :type capacity: int
    """
    self.d = {}
    self.cap = capacity
    self.head = Node(-1, -1, None)
    List.initHead(self.head)

  ___ get(self, key):
    """
    :rtype: int
    """
    __ key not in self.d:
      return -1
    self.d[key].hit()
    return self.d[key].value

  ___ set(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: nothing
    """
    __ self.cap == 0:
      return

    __ key in self.d:
      self.d[key].hit()
      self.d[key].value = value
    else:
      __ len(self.d) >= self.cap:
        oldNode = List.delete(self.head.next)
        del self.d[oldNode.key]

      newNode = Node(key, value, self.head)
      List.append(self.head, newNode)
      self.d[key] = newNode
