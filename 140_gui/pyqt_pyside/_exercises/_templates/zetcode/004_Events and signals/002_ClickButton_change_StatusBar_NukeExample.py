______ ___
____ ?.?W.. ______ *
____ ?.?C.. ______ __


c_ Example(QMainWindow):

    ___ -
        s__ ?  .-

        ?

    ___ initUI

        btn1 _ ?P..("Get Amounts of Knobs",
        btn1.m..(30, 50)

        btn2 _ ?P..("Get Name of Node",
        btn2.m..(150, 50)

        btn1.clicked.c..(button1Clicked)
        btn2.clicked.c..(button2Clicked)

        sB__

        sG__(300, 300, 290, 150)
        sWT__('Event sender')
        show

    ___ button1Clicked

        num _ nuke.selectedNode .getNumKnobs
        sB__ .sM..('Number of knobs __ Selected node is: ' + str(num))

    ___ button2Clicked

        name _ nuke.selectedNode .knob('name').getValue
        sB__ .sM..('Name of the Selected node is: ' + str(name))


__ _____ __ _______
    ______ ___

    app _ N..
    ___
        ______ n..
    ______ I..
        app _ ?A..(___.argv)
    main _ Example
    main.show

    __ app __ no. N..:
        app.e..