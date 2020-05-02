_____ ___
____ pytube _____ YouTube
____ math _____ *
____ PySide.?C.. _____ *
____ PySide.QtGui _____ *


c_ Form(?D..
    ___  -  , parent=None
        super(Form, self). - (parent)

        intext = QTextEdit()
        outtext = QTextBrowser()
        bt1 = ?PB..()
        output = ""

        bt1.sT..("Download")

        grid = QGridLayout()
        grid.addWidget(intext, 1, 0)
        grid.addWidget(outtext, 2, 0)
        grid.addWidget(bt1, 1, 1)
        setLayout(grid)

        c..(bt1, SIGNAL("clicked()"), updateUi)
        setWindowTitle("PyTube : Download Videos From Youtube")
        pass

    ___ updateUi 
        outtext.append("Download has started!!")
        yt = YouTube()
        yt.from_url(intext.toPlainText())
        yt.set_filename("Temp")
        video = yt.videos[0]
        video.download()
        outtext.append("Download Finished!!")
        pass


app = ?A..(___.argv)
form = Form()
form.s..
app.exec_()