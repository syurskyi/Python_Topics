_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ ?.?C.. _____ QRect, QPropertyAnimation

____ demoAnimation3 _____ _

c_ MyForm(?D..
    ___  -  
        s__. - 
        ui _ ?
        ?.sU..
        ?.pushButtonBounce.c___.c..(startAnimation)
        s..

    ___ startAnimation 
        anim _ QPropertyAnimation(?.labelPic, b"geometry")
        anim.setDuration(10000)
        anim.setKeyValueAt(0, QRect(0, 0, 100, 80));
        anim.setKeyValueAt(0.8, QRect(160, 160, 200, 180));
        anim.setKeyValueAt(1, QRect(400, 0, 100, 80));
        anim.s..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
