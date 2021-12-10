____ _ ______ L..., T..

____ deadlocks_train.deadlock.train ______ *
____ deadlocks_train.draw_trains ______ *
____ deadlocks_train.model ______ *

train_length = 200


___ main
    win = GraphWin('Trains in a box', 800, 800)  # give title and dimensions
    win.setBackground('black')
    train_anim = TrainAnim(win, train_length)

    trains   # list
    intersections   # list
    ___ i __ r...(4):
        trains.a..(Train(i, train_length, 0))

    ___ i __ r...(4):
        intersections.a..(Intersection(i, L...(), -1))

    t1 = T..(t.._move_train,
                a.._(trains[0], 780, [Crossing(320, intersections[0]), Crossing(460, intersections[1])]))
    t2 = T..(t.._move_train,
                a.._(trains[1], 780, [Crossing(320, intersections[1]), Crossing(460, intersections[2])]))
    t3 = T..(t.._move_train,
                a.._(trains[2], 780, [Crossing(320, intersections[2]), Crossing(460, intersections[3])]))
    t4 = T..(t.._move_train,
                a.._(trains[3], 780, [Crossing(320, intersections[3]), Crossing(460, intersections[0])]))
    t1.s..
    t2.s..
    t3.s..
    t4.s..
    w... T..
        train_anim.update_trains(trains, intersections)
        t___.s..(0.01)


main()
