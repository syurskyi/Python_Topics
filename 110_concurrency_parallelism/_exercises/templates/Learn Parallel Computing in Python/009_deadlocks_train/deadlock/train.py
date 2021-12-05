______ r___

______ t___


___ move_train(train, distance, crossings):
    w... train.front < distance:
        train.front += 1
        ___ crossing __ crossings:
            __ train.front == crossing.position:
                crossing.intersection.mutex.a...
                crossing.intersection.locked_by = train.uid
            back = train.front - train.train_length
            __ back == crossing.position:
                crossing.intersection.locked_by = -1
                crossing.intersection.mutex.r..
        t___.s..(0.01)
