'''
Created on Apr 15, 2017

@author: MT
'''

class Bucket(object
    ___ __init__(self, value
        self.keySet = set()
        self.value = value
        self.next = None
        self.prev = None

class AllOne(object
    ___ __init__(self
        self.keyBucketMap = {}
        self.head = None
        self.tail = None
    
    ___ inc(self, key
        __ key in self.keyBucketMap:
            bucket = self.keyBucketMap[key]
            nextBucket = bucket.next
            __ nextBucket and nextBucket.value __ bucket.value+1:
                nextBucket.keySet.add(key)
                self.keyBucketMap[key] = nextBucket
            ____ not nextBucket:
                nextBucket = Bucket(bucket.value+1)
                nextBucket.keySet.add(key)
                self.tail = nextBucket
                bucket.next = nextBucket
                self.keyBucketMap[key] = nextBucket
            ____
                newBucket = Bucket(bucket.value+1)
                newBucket.keySet.add(key)
                nextBucket.prev = newBucket
                newBucket.next = nextBucket
                bucket.next = newBucket
                newBucket.prev = bucket
                self.keyBucketMap[key] = newBucket
            bucket.keySet.remove(key)
            __ not bucket.keySet:
                prevBucket = bucket.prev
                __ prevBucket:
                    nextBucket = bucket.next
                    prevBucket.next = bucket.next
                    nextBucket.prev = prevBucket
                ____
                    nextBucket = bucket.next
                    nextBucket.prev = None
                    self.head = nextBucket
        ____
            __ self.head:
                __ self.head.value __ 1:
                    self.head.keySet.add(key)
                ____
                    bucket = Bucket(1)
                    bucket.keySet.add(key)
                    self.head.prev = bucket
                    bucket.next = self.head
                    self.head = bucket
            ____
                bucket= Bucket(1)
                bucket.keySet.add(key)
                self.head = bucket
                self.tail = bucket
            self.keyBucketMap[key] = self.head
    
    ___ dec(self, key
        __ key in self.keyBucketMap:
            bucket = self.keyBucketMap[key]
            prevBucket = bucket.prev
            __ prevBucket:
                __ prevBucket.value+1 __ bucket.value:
                    prevBucket.keySet.add(key)
                    self.keyBucketMap[key] = prevBucket
                ____
                    newBucket = Bucket(bucket.value-1)
                    newBucket.keySet.add(key)
                    newBucket.prev = prevBucket
                    newBucket.next = bucket
                    prevBucket.next = newBucket
                    bucket.prev = newBucket
                    self.keyBucketMap[key] = newBucket
            ____
                __ bucket.value __ 1:
                    del self.keyBucketMap[key]
                ____
                    newBucket = Bucket(bucket.value-1)
                    newBucket.keySet.add(key)
                    newBucket.next = bucket
                    bucket.prev = newBucket
                    self.head = newBucket
                    self.keyBucketMap[key] = newBucket
            bucket.keySet.remove(key)
            __ not bucket.keySet:
                __ not bucket.prev and not bucket.next:
                    self.head = None
                    self.tail = None
                ____ bucket.prev and not bucket.next:
                    bucket.prev.next = None
                    self.tail = bucket.prev
                    bucket.prev = None
                ____ bucket.next and not bucket.prev:
                    bucket.next.prev = None
                    self.head = bucket.next
                    bucket.next = None
                ____
                    bucket.next.prev = bucket.prev
                    bucket.prev.next = bucket.next
                    bucket.prev = None
                    bucket.next = None
        
    ___ getMax(self
        __ self.tail:
            val = self.tail.keySet.pop()
            self.tail.keySet.add(val)
            r_ val
        ____
            r_ ''
    
    ___ getMin(self
        __ self.head:
            val = self.head.keySet.pop()
            self.head.keySet.add(val)
            r_ val
        ____
            r_ ''
    