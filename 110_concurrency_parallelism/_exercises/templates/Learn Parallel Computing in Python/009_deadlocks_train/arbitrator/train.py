______ _
______ t___

controller = _.Condition()


___ all_free(intersections_to_lock):
    ___ it __ intersections_to_lock:
        if it.locked_by >= 0:
            return False
    return True


___ lock_intersections_in_distance(id, reserve_start, reserve_end, crossings):
    intersections_to_lock = []
    ___ crossing __ crossings:
        if reserve_end >= crossing.position >= reserve_start and crossing.intersection.locked_by != id:
            intersections_to_lock.append(crossing.intersection)

    controller.acquire()
    while not all_free(intersections_to_lock):
        controller.wait()

    ___ intersection __ intersections_to_lock:
        intersection.locked_by = id
        t___.s..(0.01)
    controller.release()


___ move_train(train, distance, crossings):
    while train.front < distance:
        train.front += 1
        ___ crossing __ crossings:
            if train.front == crossing.position:
                lock_intersections_in_distance(train.uid, crossing.position,
                                               crossing.position + train.train_length, crossings)
            back = train.front - train.train_length
            if back == crossing.position:
                controller.acquire()
                crossing.intersection.locked_by = -1
                controller.notify_all()
                controller.release()
        t___.s..(0.01)
