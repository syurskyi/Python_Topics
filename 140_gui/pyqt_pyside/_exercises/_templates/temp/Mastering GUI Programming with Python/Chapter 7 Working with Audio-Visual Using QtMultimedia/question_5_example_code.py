____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc
____ ? ______ QtMultimedia __ qtmm
____ ? ______ QtMultimediaWidgets __ qtmmw


c_ MainWindow(qtw.QWidget):

    ___ __init__(self):
        super().__init__()
        self.sL..(qtw.QVBoxLayout())

        # camera
        self.camera _ qtmm.QCamera()

        # viewfinder
        cvf _ qtmmw.QCameraViewfinder()
        self.camera.setViewfinder(cvf)
        self.layout().aW..(cvf)

        # Form
        form _ qtw.QFormLayout()
        self.layout().addLayout(form)

        # zoom
        zoomslider _ qtw.QSlider(
            minimum_1,
            maximum_10,
            sliderMoved_self.on_slider_moved,
            orientation_qtc.__.Horizontal
        )
        form.addRow('Zoom', zoomslider)

        self.camera.start()
        self.s..

    ___ on_slider_moved  value):

        focus _ self.camera.focus()
        focus.zoomTo(1, value)


__ __name__ == '__main__':
    app _ qtw.?
    mw _ MainWindow()
    app.exec()
