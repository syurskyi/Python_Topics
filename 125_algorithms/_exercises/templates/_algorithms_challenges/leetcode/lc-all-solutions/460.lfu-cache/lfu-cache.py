c_ L..(o..
  $
  ___ delete(elem
    elem.prev.next = elem.next
    elem.next.prev = elem.prev
    elem.next = elem.prev = N..
    r.. elem

  $
  ___ move(elem, newPrev, newNext
    elem.prev = newPrev
    elem.next = newNext
    newPrev.next = elem
    newNext.prev = elem

  $
  ___ a..(head, elem
    L...move(elem, head.prev, head)

  $
  ___ insertAfter(head, elem
    L...move(elem, head, head.next)

  $
  ___ isEmpty(head
    r.. head.next __ head.prev __ head

  $
  ___ initHead(head
    head.prev = head.next = head


c_ FreqNode(o..
  ___ - , freq
    prev = next = N..
    freq = freq
    head = Cache(-1, -1, self)
    L...initHead(head)

  ___ popCache
    head = head
    ret = L...delete(head.next)
    __ L...isEmpty(head
      L...delete(self)
    r.. ret


c_ Cache(o..
  ___ - , key, val, freqNode
    prev = next = N..
    freqNode = freqNode
    val = val
    key = key

  ___ increaseFreq
    freqNode = freqNode
    newFreqNode = N..
    __ L...isEmpty(freqNode) o. freqNode.next.freq != freqNode.freq + 1:
      newFreqNode = FreqNode(freqNode.freq + 1)
      L...insertAfter(freqNode, newFreqNode)
    ____:
      newFreqNode = freqNode.next
    freqNode = newFreqNode
    L...delete(self)
    L...a..(newFreqNode.head, self)
    __ L...isEmpty(freqNode.head
      L...delete(freqNode)


c_ LFUCache(o..
  ___ - , capacity
    d    # dict
    cap = capacity
    head = FreqNode(-1)
    L...initHead(head)

  ___ get  key
    __ key n.. __ d:
      r.. -1
    cacheNode = d[key]
    cacheNode.increaseFreq()
    r.. cacheNode.val

  ___ s..  key, value
    __ cap __ 0:
      r..
    __ key __ d:
      cacheNode = d[key]
      cacheNode.val = value
      cacheNode.increaseFreq()
    ____:
      __ l..(d) >= cap:
        del d[head.next.popCache().key]
      newFreqNode = FreqNode(0)
      newCacheNode = Cache(key, value, newFreqNode)
      L...a..(newFreqNode.head, newCacheNode)
      L...insertAfter(head, newFreqNode)
      d[key] = newCacheNode
      newCacheNode.increaseFreq()

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
