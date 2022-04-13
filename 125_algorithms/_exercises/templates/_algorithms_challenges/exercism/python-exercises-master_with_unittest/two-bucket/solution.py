'''
    This solution implements a breadth-first search of the graph
    of possible valid states for the two buckets until it reaches a state
    in which one of the two buckets contains the goal amount
'''


___ measure(bucket_one, bucket_two, goal, start_bucket
    sizes [bucket_one, bucket_two]
    goalIndex 0 __ start_bucket __ 'one' ____ 1

    ___ empty(buckets, i
        r.. [0, buckets[1]] __ i __ 0 ____ [buckets[0], 0]

    ___ fill(buckets, i
        r.. [sizes[0], buckets[1]] __ i __ 0 ____ [buckets[0], sizes[1]]

    ___ consolidate(buckets, i
        amount m..(buckets[1 - i], sizes[i] - buckets[i])
        target buckets[i] + amount
        src buckets[1 - i] - amount
        r.. [target, src] __ i __ 0 ____ [src, target]

    ___ bucket_str(buckets
        r.. '{},{}'.f..(*buckets)

    invalid [0, 0]
    invalid[1 - goalIndex] sizes[1 - goalIndex]
    invalidStr bucket_str(invalid)
    buckets [0, 0]
    buckets[goalIndex] sizes[goalIndex]
    toVisit    # list
    visited s..()
    count 1
    w.... goal n.. __ buckets:
        key bucket_str(buckets)
        __ key !_ invalidStr a.. key n.. __ visited:
            visited.add(key)
            nc count + 1
            ___ i __ r..(2
                __ buckets[i] !_ 0:
                    toVisit.a..((empty(buckets, i), nc
                __ buckets[i] !_ sizes[i]:
                    toVisit.a..((fill(buckets, i), nc
                    toVisit.a..((consolidate(buckets, i), nc
        __ n.. a__(toVisit
            r.. V...('No more moves!')
        buckets, count toVisit.p.. 0)

    goalIndex buckets.i.. goal)
    goalBucket =  'one', 'two' [goalIndex]
    otherBucket buckets[1 - goalIndex]
    r.. (count, goalBucket, otherBucket)
