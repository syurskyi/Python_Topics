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


class FreqNode(object):
  ___ __init__(self, freq):
    self.prev = self.next = None
    self.freq = freq
    self.head = Cache(-1, -1, self)
    List.initHead(self.head)

  ___ popCache(self):
    head = self.head
    ret = List.delete(head.next)
    __ List.isEmpty(head):
      List.delete(self)
    return ret


class Cache(object):
  ___ __init__(self, key, val, freqNode):
    self.prev = self.next = None
    self.freqNode = freqNode
    self.val = val
    self.key = key

  ___ increaseFreq(self):
    freqNode = self.freqNode
    newFreqNode = None
    __ List.isEmpty(freqNode) or freqNode.next.freq != freqNode.freq + 1:
      newFreqNode = FreqNode(self.freqNode.freq + 1)
      List.insertAfter(freqNode, newFreqNode)
    else:
      newFreqNode = freqNode.next
    self.freqNode = newFreqNode
    List.delete(self)
    List.append(newFreqNode.head, self)
    __ List.isEmpty(freqNode.head):
      List.delete(freqNode)


class LFUCache(object):
  ___ __init__(self, capacity):
    self.d = {}
    self.cap = capacity
    self.head = FreqNode(-1)
    List.initHead(self.head)

  ___ get(self, key):
    __ key not in self.d:
      return -1
    cacheNode = self.d[key]
    cacheNode.increaseFreq()
    return cacheNode.val

  ___ set(self, key, value):
    __ self.cap == 0:
      return
    __ key in self.d:
      cacheNode = self.d[key]
      cacheNode.val = value
      cacheNode.increaseFreq()
    else:
      __ len(self.d) >= self.cap:
        del self.d[self.head.next.popCache().key]
      newFreqNode = FreqNode(0)
      newCacheNode = Cache(key, value, newFreqNode)
      List.append(newFreqNode.head, newCacheNode)
      List.insertAfter(self.head, newFreqNode)
      self.d[key] = newCacheNode
      newCacheNode.increaseFreq()

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
