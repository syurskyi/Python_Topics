'''
Created on Mar 27, 2017

@author: MT
'''

class HitCounter(object):
    ___ __init__(self):
        self.hitCount = [0]*300
        self.timestampes = [0]*300
    
    ___ hit(self, timestamp):
        ind = timestamp % 300
        __ timestamp != self.timestampes[ind]:
            self.hitCount[ind] = 1
            self.timestampes[ind] = timestamp
        ____:
            self.hitCount[ind] += 1
    
    ___ getHits(self, timestamp):
        count = 0
        ___ i, time __ e..(self.timestampes):
            __ timestamp - time < 300:
                count += self.hitCount[i]
        r.. count

class HitCounterOwn(object):
    ___ __init__(self):
        self.queue    # list
    
    ___ hit(self, timestamp):
        self.queue.a..(timestamp)
        __ self.queue a.. self.queue[0] < timestamp-300:
            self.queue.pop(0)
    
    ___ getHits(self, timestamp):
        start, end = 0, l..(self.queue)
        target = timestamp - 300
        w.... start < end:
            mid = (start+end)/2
            __ target >= self.queue[mid]:
                start = mid+1
            ____:
                end = mid
        r.. l..(self.queue)-end
