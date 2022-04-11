c_ L..(o..
  $
  ___ delete(elem
    elem.prev.next elem.next
    elem.next.prev elem.prev
    r.. elem

  $
  ___ move(elem, newPrev, newNext
    elem.prev newPrev
    elem.next newNext
    newPrev.next elem
    newNext.prev elem

  $
  ___ a..(head, elem
    L...move(elem, head.prev, head)

  $
  ___ isEmpty(head
    r.. head.next __ head.prev __ head

  $
  ___ initHead(head
    head.prev head.next head


c_ Node(o..
  ___ - , key, value, head
    key key
    value value
    head head
    prev next N..

  ___ hit
    L...delete(self)
    L...a..(head, self)


c_ LRUCache(o..
  ___ - , capacity
    """
    :type capacity: int
    """
    d    # dict
    cap capacity
    head Node(-1, -1, N..)
    L...initHead(head)

  ___ get  key
    """
    :rtype: int
    """
    __ key n.. __ d:
      r.. -1
    d[key].hit()
    r.. d[key].value

  ___ s..  key, value
    """
    :type key: int
    :type value: int
    :rtype: nothing
    """
    __ cap __ 0:
      r..

    __ key __ d:
      d[key].hit()
      d[key].value value
    ____
      __ l..(d) >_ cap:
        oldNode L...delete(head.next)
        del d[oldNode.key]

      newNode Node(key, value, head)
      L...a..(head, newNode)
      d[key] newNode
