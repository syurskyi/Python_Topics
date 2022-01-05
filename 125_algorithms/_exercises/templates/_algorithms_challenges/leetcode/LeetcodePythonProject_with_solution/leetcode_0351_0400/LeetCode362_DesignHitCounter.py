'''
Created on Mar 27, 2017

@author: MT
'''

c_ HitCounter(o..):
    ___ - ):
        hitCount = [0]*300
        timestampes = [0]*300
    
    ___ hit  timestamp):
        ind = timestamp % 300
        __ timestamp != timestampes[ind]:
            hitCount[ind] = 1
            timestampes[ind] = timestamp
        ____:
            hitCount[ind] += 1
    
    ___ getHits  timestamp):
        count = 0
        ___ i, time __ e..(timestampes):
            __ timestamp - time < 300:
                count += hitCount[i]
        r.. count

c_ HitCounterOwn(o..):
    ___ - ):
        queue    # list
    
    ___ hit  timestamp):
        queue.a..(timestamp)
        __ queue a.. queue[0] < timestamp-300:
            queue.pop(0)
    
    ___ getHits  timestamp):
        start, end = 0, l..(queue)
        target = timestamp - 300
        w.... start < end:
            mid = (start+end)/2
            __ target >= queue[mid]:
                start = mid+1
            ____:
                end = mid
        r.. l..(queue)-end
