____ graphics ______ *


c_ TrainAnim:
    ___  -   win, train_length):
        colours = [color_rgb(233, 33, 40), color_rgb(78, 151, 210),
                        color_rgb(251, 170, 26), color_rgb(11, 132, 54)]
        train_length = train_length
        track0 = Line(Point(10, 330), Point(790, 330))
        track1 = Line(Point(10, 470), Point(790, 470))
        track2 = Line(Point(330, 10), Point(330, 790))
        track3 = Line(Point(470, 10), Point(470, 790))
        draw_track(win, track0)
        draw_track(win, track1)
        draw_track(win, track2)
        draw_track(win, track3)
        train0 = Line(Point(10, 330), Point(10 - train_length, 330))
        train1 = Line(Point(470, 10), Point(470, 10 - train_length))
        train2 = Line(Point(790, 470), Point(790 + train_length, 470))
        train3 = Line(Point(330, 790), Point(330, 790 + train_length))
        draw_train(win, train0, colours[0])
        draw_train(win, train1, colours[1])
        draw_train(win, train2, colours[2])
        draw_train(win, train3, colours[3])
        boxes = [Rectangle(Point(350, 350), Point(360, 360)),
                      Rectangle(Point(450, 350), Point(440, 360)),
                      Rectangle(Point(450, 450), Point(440, 440)),
                      Rectangle(Point(350, 450), Point(360, 440))]
        ___ box __ boxes:
            draw_crossing(win, box)

    ___ update_trains  trains, intersections):
        current_x = train0.getP2().getX() - 10 + train_length
        train0.move(trains[0].front - current_x, 0)
        current_x = 790 - train2.getP2().getX() + train_length
        train2.move(current_x - trains[2].front, 0)
        current_y = train1.getP2().getY() - 10 + train_length
        train1.move(0, trains[1].front - current_y)
        current_y = 790 - train3.getP2().getY() + train_length
        train3.move(0, current_y - trains[3].front)
        ___ i __ r...(4):
            __ intersections[i].locked_by < 0:
                boxes[i].setFill(color_rgb(185, 185, 185))
            else:
                boxes[i].setFill(colours[intersections[i].locked_by])

    ___ draw_crossing  win, box):
        box.setFill(color_rgb(185, 185, 185))
        box.draw(win)

    ___ draw_track  win, line):
        line.setFill(color_rgb(185, 185, 185))
        line.setWidth(4)
        line.draw(win)

    ___ draw_train  win, line, colour):
        line.setFill(colour)
        line.setWidth(14)
        line.draw(win)
