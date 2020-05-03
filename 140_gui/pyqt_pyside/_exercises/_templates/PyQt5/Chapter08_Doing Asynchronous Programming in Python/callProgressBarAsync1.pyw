_____ ___, time
_____ asyncio

____ ?.?W.. _____ ?D.., ?A..
____ quamash _____ QEventLoop
____ demoTwoProgressBarsAsync _____ _

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ ?
        ?.sU..
        ?.pushButtonStart.c___.c..(invokeAsync)
        s..

    ___ invokeAsync
        asyncio.ensure_future(updt(0.5, ?.progressBarFileDownload))
        asyncio.ensure_future(updt(1, ?.progressBarVirusScan))
               
    @staticmethod
    async ___ updt(delay, ProgressBar
        ___ i __ range(101
            await asyncio.sleep(delay)
            ProgressBar.sV..(i)

___ stopper(loop
    loop.stop()

     
__ _ ____ __ _____
    app _ ?A..
    loop _ QEventLoop(app)
    asyncio.set_event_loop(loop)
    w _ ?
    w.exec()
    w__ loop:
        loop.run_forever()
    loop.c..
    ___.e.. ?.e


