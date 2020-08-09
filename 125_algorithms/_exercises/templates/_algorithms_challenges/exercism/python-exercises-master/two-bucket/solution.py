'''
    This solution implements a breadth-first search of the graph
    of possible valid states for the two buckets until it reaches a state
    in which one of the two buckets contains the goal amount
'''


___ measure(bucket_one, bucket_two, goal, start_bucket
    sizes = [bucket_one, bucket_two]
    goalIndex = 0 __ start_bucket __ 'one' else 1

    ___ empty(buckets, i
        r_ [0, buckets[1]] __ i __ 0 else [buckets[0], 0]

    ___ fill(buckets, i
        r_ [sizes[0], buckets[1]] __ i __ 0 else [buckets[0], sizes[1]]

    ___ consolidate(buckets, i
        amount = min(buckets[1 - i], sizes[i] - buckets[i])
        target = buckets[i] + amount
        src = buckets[1 - i] - amount
        r_ [target, src] __ i __ 0 else [src, target]

    ___ bucket_str(buckets
        r_ '{},{}'.format(*buckets)

    invalid = [0, 0]
    invalid[1 - goalIndex] = sizes[1 - goalIndex]
    invalidStr = bucket_str(invalid)
    buckets = [0, 0]
    buckets[goalIndex] = sizes[goalIndex]
    toVisit = []
    visited = set()
    count = 1
    w___ goal not in buckets:
        key = bucket_str(buckets)
        __ key != invalidStr and key not in visited:
            visited.add(key)
            nc = count + 1
            ___ i in range(2
                __ buckets[i] != 0:
                    toVisit.append((empty(buckets, i), nc))
                __ buckets[i] != sizes[i]:
                    toVisit.append((fill(buckets, i), nc))
                    toVisit.append((consolidate(buckets, i), nc))
        __ not any(toVisit
            raise ValueError('No more moves!')
        buckets, count = toVisit.pop(0)

    goalIndex = buckets.index(goal)
    goalBucket = ['one', 'two'][goalIndex]
    otherBucket = buckets[1 - goalIndex]
    r_ (count, goalBucket, otherBucket)
