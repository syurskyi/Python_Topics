from threading ______ Lock, Thread

from deadlocks_train.deadlock.train ______ *
from deadlocks_train.draw_trains ______ *
from deadlocks_train.model ______ *

train_length = 200


___ main
    win = GraphWin('Trains in a box', 800, 800)  # give title and dimensions
    win.setBackground('black')
    train_anim = TrainAnim(win, train_length)

    trains = []
    intersections = []
    ___ i __ r...(4):
        trains.append(Train(i, train_length, 0))

    ___ i __ r...(4):
        intersections.append(Intersection(i, Lock(), -1))

    t1 = Thread(t.._move_train,
                a.._(trains[0], 780, [Crossing(320, intersections[0]), Crossing(460, intersections[1])]))
    t2 = Thread(t.._move_train,
                a.._(trains[1], 780, [Crossing(320, intersections[1]), Crossing(460, intersections[2])]))
    t3 = Thread(t.._move_train,
                a.._(trains[2], 780, [Crossing(320, intersections[2]), Crossing(460, intersections[3])]))
    t4 = Thread(t.._move_train,
                a.._(trains[3], 780, [Crossing(320, intersections[3]), Crossing(460, intersections[0])]))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    while True:
        train_anim.update_trains(trains, intersections)
        time.sleep(0.01)


main()
