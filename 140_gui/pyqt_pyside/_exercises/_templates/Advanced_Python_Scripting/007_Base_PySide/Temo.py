_____ ___
____ pytube _____ YouTube
____ math _____ _
____ ?.?C.. _____ _
____ ?.?G.. _____ _


c_ Form(?D..
    ___  -  , parent_None
        s__(Form, self). - (parent)

        intext _ QTextEdit
        outtext _ QTextBrowser
        bt1 _ ?PB..
        output _ ""

        bt1.sT..("Download")

        grid _ QGridLayout
        grid.addWidget(intext, 1, 0)
        grid.addWidget(outtext, 2, 0)
        grid.addWidget(bt1, 1, 1)
        setLayout(grid)

        c..(bt1, SIGNAL("clicked()"), updateUi)
        setWindowTitle("PyTube : Download Videos From Youtube")
        p..

    ___ updateUi 
        outtext.ap..("Download has started!!")
        yt _ YouTube
        yt.from_url(intext.tPT..())
        yt.set_filename("Temp")
        video _ yt.videos[0]
        video.download
        outtext.ap..("Download Finished!!")
        p..


app _ ?A..
form _ Form
form.s..
app.e..