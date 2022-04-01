c_ List(o..):
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


c_ Node(o..):
  ___ - , key, value, head):
    key = key
    value = value
    head = head
    prev = next = N..

  ___ hit
    List.delete(self)
    List.a..(head, self)


c_ LRUCache(o..):
  ___ - , capacity):
    """
    :type capacity: int
    """
    d    # dict
    cap = capacity
    head = Node(-1, -1, N..)
    List.initHead(head)

  ___ get  key):
    """
    :rtype: int
    """
    __ key n.. __ d:
      r.. -1
    d[key].hit()
    r.. d[key].value

  ___ s..  key, value):
    """
    :type key: int
    :type value: int
    :rtype: nothing
    """
    __ cap __ 0:
      r..

    __ key __ d:
      d[key].hit()
      d[key].value = value
    ____:
      __ l..(d) >= cap:
        oldNode = List.delete(head.next)
        del d[oldNode.key]

      newNode = Node(key, value, head)
      List.a..(head, newNode)
      d[key] = newNode
