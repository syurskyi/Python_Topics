_____ ___, time
_____ asyncio

____ ?.?W.. _____ ?D.., ?A..
____ quamash _____ QEventLoop
____ demoTwoProgressBarsAsync _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.pushButtonStart.c___.c..(invokeAsync)
        s..

    ___ invokeAsync
        asyncio.ensure_future(updt(0.5, ui.progressBarFileDownload))
        asyncio.ensure_future(updt(1, ui.progressBarVirusScan))
               
    @staticmethod
    async ___ updt(delay, ProgressBar
        ___ i __ range(101
            await asyncio.sleep(delay)
            ProgressBar.setValue(i)

___ stopper(loop
    loop.stop()

     
__ _ ____ __ _____
    app _ ?A..(___.argv)
    loop _ QEventLoop(app)
    asyncio.set_event_loop(loop)
    w _ MyForm()
    w.exec()
    with loop:
        loop.run_forever()
    loop.close()
    ___.e..(app.e


