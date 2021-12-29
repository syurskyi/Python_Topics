class List(object):
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


class FreqNode(object):
  ___ __init__(self, freq):
    self.prev = self.next = N..
    self.freq = freq
    self.head = Cache(-1, -1, self)
    List.initHead(self.head)

  ___ popCache(self):
    head = self.head
    ret = List.delete(head.next)
    __ List.isEmpty(head):
      List.delete(self)
    r.. ret


class Cache(object):
  ___ __init__(self, key, val, freqNode):
    self.prev = self.next = N..
    self.freqNode = freqNode
    self.val = val
    self.key = key

  ___ increaseFreq(self):
    freqNode = self.freqNode
    newFreqNode = N..
    __ List.isEmpty(freqNode) o. freqNode.next.freq != freqNode.freq + 1:
      newFreqNode = FreqNode(self.freqNode.freq + 1)
      List.insertAfter(freqNode, newFreqNode)
    ____:
      newFreqNode = freqNode.next
    self.freqNode = newFreqNode
    List.delete(self)
    List.a..(newFreqNode.head, self)
    __ List.isEmpty(freqNode.head):
      List.delete(freqNode)


class LFUCache(object):
  ___ __init__(self, capacity):
    self.d = {}
    self.cap = capacity
    self.head = FreqNode(-1)
    List.initHead(self.head)

  ___ get(self, key):
    __ key n.. __ self.d:
      r.. -1
    cacheNode = self.d[key]
    cacheNode.increaseFreq()
    r.. cacheNode.val

  ___ set(self, key, value):
    __ self.cap __ 0:
      r..
    __ key __ self.d:
      cacheNode = self.d[key]
      cacheNode.val = value
      cacheNode.increaseFreq()
    ____:
      __ l..(self.d) >= self.cap:
        del self.d[self.head.next.popCache().key]
      newFreqNode = FreqNode(0)
      newCacheNode = Cache(key, value, newFreqNode)
      List.a..(newFreqNode.head, newCacheNode)
      List.insertAfter(self.head, newFreqNode)
      self.d[key] = newCacheNode
      newCacheNode.increaseFreq()

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
