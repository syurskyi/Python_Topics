c_ List(object):
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


c_ FreqNode(object):
  ___ - , freq):
    prev = next = N..
    freq = freq
    head = Cache(-1, -1, self)
    List.initHead(head)

  ___ popCache
    head = head
    ret = List.delete(head.next)
    __ List.isEmpty(head):
      List.delete(self)
    r.. ret


c_ Cache(object):
  ___ - , key, val, freqNode):
    prev = next = N..
    freqNode = freqNode
    val = val
    key = key

  ___ increaseFreq
    freqNode = freqNode
    newFreqNode = N..
    __ List.isEmpty(freqNode) o. freqNode.next.freq != freqNode.freq + 1:
      newFreqNode = FreqNode(freqNode.freq + 1)
      List.insertAfter(freqNode, newFreqNode)
    ____:
      newFreqNode = freqNode.next
    freqNode = newFreqNode
    List.delete(self)
    List.a..(newFreqNode.head, self)
    __ List.isEmpty(freqNode.head):
      List.delete(freqNode)


c_ LFUCache(object):
  ___ - , capacity):
    d    # dict
    cap = capacity
    head = FreqNode(-1)
    List.initHead(head)

  ___ get(self, key):
    __ key n.. __ d:
      r.. -1
    cacheNode = d[key]
    cacheNode.increaseFreq()
    r.. cacheNode.val

  ___ set(self, key, value):
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
      List.a..(newFreqNode.head, newCacheNode)
      List.insertAfter(head, newFreqNode)
      d[key] = newCacheNode
      newCacheNode.increaseFreq()

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
