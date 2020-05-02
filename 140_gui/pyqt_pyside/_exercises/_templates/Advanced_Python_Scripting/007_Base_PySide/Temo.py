_____ ___
____ pytube _____ YouTube
____ math _____ *
____ PySide.?C.. _____ *
____ PySide.QtGui _____ *


c_ Form(?D..
    ___  -  , parent_None
        super(Form, self). - (parent)

        intext _ QTextEdit()
        outtext _ QTextBrowser()
        bt1 _ ?PB..()
        output _ ""

        bt1.sT..("Download")

        grid _ QGridLayout()
        grid.addWidget(intext, 1, 0)
        grid.addWidget(outtext, 2, 0)
        grid.addWidget(bt1, 1, 1)
        setLayout(grid)

        c..(bt1, SIGNAL("clicked()"), updateUi)
        setWindowTitle("PyTube : Download Videos From Youtube")
        pass

    ___ updateUi 
        outtext.append("Download has started!!")
        yt _ YouTube()
        yt.from_url(intext.toPlainText())
        yt.set_filename("Temp")
        video _ yt.videos[0]
        video.download()
        outtext.append("Download Finished!!")
        pass


app _ ?A..(___.argv)
form _ Form()
form.s..
app.exec_()