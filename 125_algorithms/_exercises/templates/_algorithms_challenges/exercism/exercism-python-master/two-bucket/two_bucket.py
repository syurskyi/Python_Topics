___ measure(bucket_one, bucket_two, goal, start_bucket
    seen = set()
    __ start_bucket __ 'one':
        seen.add((0, bucket_two))
        vol_one, vol_two = bucket_one, 0
    ____ start_bucket __ 'two':
        seen.add((bucket_one, 0))
        vol_one, vol_two = 0, bucket_two
    ____
        raise ValueError('Only two buckets: {}'.format(start_bucket))

    queue = [(1, vol_one, vol_two)]

    w___ queue:
        steps, one, two = queue.pop(0)
        __ (one, two) __ seen:
            continue
        seen.add((one, two))

        __ one __ goal:
            r_ (steps, "one", two)
        ____ two __ goal:
            r_ (steps, "two", one)

        # Fill
        queue.append((steps + 1, one, bucket_two))
        queue.append((steps + 1, bucket_one, two))

        # Empty
        queue.append((steps + 1, one, 0))
        queue.append((steps + 1, 0, two))

        # Transfer
        __ one + two < bucket_two:
            queue.append((steps + 1, 0, one+two))
        ____
            queue.append((steps + 1, one+two-bucket_two, bucket_two))

        __ one + two < bucket_one:
            queue.append((steps + 1, one+two, 0))
        ____
            queue.append((steps + 1, bucket_one, one+two-bucket_one))

    raise ValueError('No solution')
