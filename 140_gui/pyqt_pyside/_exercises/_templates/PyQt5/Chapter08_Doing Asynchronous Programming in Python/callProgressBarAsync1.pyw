_____ ___, time
_____ asyncio

____ ?.?W.. _____ ?D.., ?A..
____ quamash _____ QEventLoop
____ demoTwoProgressBarsAsync _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonStart.clicked.c..(invokeAsync)
        s..

    ___ invokeAsync
        asyncio.ensure_future(updt(0.5, ui.progressBarFileDownload))
        asyncio.ensure_future(updt(1, ui.progressBarVirusScan))
               
    @staticmethod
    async ___ updt(delay, ProgressBar
        for i in range(101
            await asyncio.sleep(delay)
            ProgressBar.setValue(i)

___ stopper(loop
    loop.stop()

     
__ __name____"__main__":    
    app = ?A..(___.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    w = MyForm()
    w.exec()
    with loop:
        loop.run_forever()
    loop.close()
    ___.e..(app.exec_())


