'''
Created on Apr 15, 2017

@author: MT
'''

c_ Bucket(o..):
    ___ - , value):
        keySet = set()
        value = value
        next = N..
        prev = N..

c_ AllOne(o..):
    ___ - ):
        keyBucketMap    # dict
        head = N..
        tail = N..
    
    ___ inc  key):
        __ key __ keyBucketMap:
            bucket = keyBucketMap[key]
            nextBucket = bucket.next
            __ nextBucket a.. nextBucket.value __ bucket.value+1:
                nextBucket.keySet.add(key)
                keyBucketMap[key] = nextBucket
            ____ n.. nextBucket:
                nextBucket = Bucket(bucket.value+1)
                nextBucket.keySet.add(key)
                tail = nextBucket
                bucket.next = nextBucket
                keyBucketMap[key] = nextBucket
            ____:
                newBucket = Bucket(bucket.value+1)
                newBucket.keySet.add(key)
                nextBucket.prev = newBucket
                newBucket.next = nextBucket
                bucket.next = newBucket
                newBucket.prev = bucket
                keyBucketMap[key] = newBucket
            bucket.keySet.remove(key)
            __ n.. bucket.keySet:
                prevBucket = bucket.prev
                __ prevBucket:
                    nextBucket = bucket.next
                    prevBucket.next = bucket.next
                    nextBucket.prev = prevBucket
                ____:
                    nextBucket = bucket.next
                    nextBucket.prev = N..
                    head = nextBucket
        ____:
            __ head:
                __ head.value __ 1:
                    head.keySet.add(key)
                ____:
                    bucket = Bucket(1)
                    bucket.keySet.add(key)
                    head.prev = bucket
                    bucket.next = head
                    head = bucket
            ____:
                bucket= Bucket(1)
                bucket.keySet.add(key)
                head = bucket
                tail = bucket
            keyBucketMap[key] = head
    
    ___ dec  key):
        __ key __ keyBucketMap:
            bucket = keyBucketMap[key]
            prevBucket = bucket.prev
            __ prevBucket:
                __ prevBucket.value+1 __ bucket.value:
                    prevBucket.keySet.add(key)
                    keyBucketMap[key] = prevBucket
                ____:
                    newBucket = Bucket(bucket.value-1)
                    newBucket.keySet.add(key)
                    newBucket.prev = prevBucket
                    newBucket.next = bucket
                    prevBucket.next = newBucket
                    bucket.prev = newBucket
                    keyBucketMap[key] = newBucket
            ____:
                __ bucket.value __ 1:
                    del keyBucketMap[key]
                ____:
                    newBucket = Bucket(bucket.value-1)
                    newBucket.keySet.add(key)
                    newBucket.next = bucket
                    bucket.prev = newBucket
                    head = newBucket
                    keyBucketMap[key] = newBucket
            bucket.keySet.remove(key)
            __ n.. bucket.keySet:
                __ n.. bucket.prev a.. n.. bucket.next:
                    head = N..
                    tail = N..
                ____ bucket.prev a.. n.. bucket.next:
                    bucket.prev.next = N..
                    tail = bucket.prev
                    bucket.prev = N..
                ____ bucket.next a.. n.. bucket.prev:
                    bucket.next.prev = N..
                    head = bucket.next
                    bucket.next = N..
                ____:
                    bucket.next.prev = bucket.prev
                    bucket.prev.next = bucket.next
                    bucket.prev = N..
                    bucket.next = N..
        
    ___ getMax
        __ tail:
            val = tail.keySet.pop()
            tail.keySet.add(val)
            r.. val
        ____:
            r.. ''
    
    ___ getMin
        __ head:
            val = head.keySet.pop()
            head.keySet.add(val)
            r.. val
        ____:
            r.. ''
    