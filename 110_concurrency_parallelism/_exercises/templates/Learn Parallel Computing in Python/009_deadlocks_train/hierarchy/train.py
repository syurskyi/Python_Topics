______ t___


___ lock_intersections_in_distance(id, reserve_start, reserve_end, crossings):
    intersections_to_lock = []
    ___ crossing __ crossings:
        __ reserve_end >= crossing.position >= reserve_start and crossing.intersection.locked_by != id:
            intersections_to_lock.a..(crossing.intersection)

    intersections_to_lock = sorted(intersections_to_lock, key=lambda it: it.uid)

    ___ intersection __ intersections_to_lock:
        intersection.mutex.a...
        intersection.locked_by = id
        t___.s..(0.01)

___ move_train(train, distance, crossings):
    w... train.front < distance:
        train.front += 1
        ___ crossing __ crossings:
            __ train.front == crossing.position:
                lock_intersections_in_distance(train.uid, crossing.position,
                                               crossing.position + train.train_length, crossings)
            back = train.front - train.train_length
            __ back == crossing.position:
                crossing.intersection.locked_by = -1
                crossing.intersection.mutex.r..
        t___.s..(0.01)