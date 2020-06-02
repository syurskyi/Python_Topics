____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc
____ ? ______ QtMultimedia __ qtmm
____ ? ______ QtMultimediaWidgets __ qtmmw


c_ MainWindow ?.?W..

    ___  -  
        s_. - ()
        sL.. ?.?VBL..

        # camera
        camera _ qtmm.QCamera()

        # viewfinder
        cvf _ qtmmw.QCameraViewfinder()
        camera.setViewfinder(cvf)
        la__ .aW..(cvf)

        # Form
        form _ qtw.?FL..
        la__ .aL..(form)

        # zoom
        zoomslider _ qtw.QSlider(
            minimum_1,
            maximum_10,
            sliderMoved_self.on_slider_moved,
            orientation_qtc.__.H..
        )
        form.aR..('Zoom', zoomslider)

        camera.start()
        s..

    ___ on_slider_moved  value):

        focus _ camera.focus()
        focus.zoomTo(1, value)


__ ______ __ ______
    app _ qtw.?
    mw _ MainWindow()
    app.exec()
