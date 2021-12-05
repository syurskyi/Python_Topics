______ _
______ t___

controller = _.C...()


___ all_free(intersections_to_lock):
    ___ it __ intersections_to_lock:
        __ it.locked_by >= 0:
            return False
    return True


___ lock_intersections_in_distance(id, reserve_start, reserve_end, crossings):
    intersections_to_lock = []
    ___ crossing __ crossings:
        __ reserve_end >= crossing.position >= reserve_start and crossing.intersection.locked_by != id:
            intersections_to_lock.a..(crossing.intersection)

    controller.a...
    w... not all_free(intersections_to_lock):
        controller.w..

    ___ intersection __ intersections_to_lock:
        intersection.locked_by = id
        t___.s..(0.01)
    controller.r..


___ move_train(train, distance, crossings):
    w... train.front < distance:
        train.front += 1
        ___ crossing __ crossings:
            __ train.front == crossing.position:
                lock_intersections_in_distance(train.uid, crossing.position,
                                               crossing.position + train.train_length, crossings)
            back = train.front - train.train_length
            __ back == crossing.position:
                controller.a...
                crossing.intersection.locked_by = -1
                controller.notify_all()
                controller.r..
        t___.s..(0.01)
