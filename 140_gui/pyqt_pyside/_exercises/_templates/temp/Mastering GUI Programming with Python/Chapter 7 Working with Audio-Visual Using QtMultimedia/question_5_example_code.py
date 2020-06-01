____ ? ______ ?W.. as qtw
____ ? ______ QtCore as qtc
____ ? ______ QtMultimedia as qtmm
____ ? ______ QtMultimediaWidgets as qtmmw


class MainWindow(qtw.QWidget):

    ___ __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        # camera
        self.camera _ qtmm.QCamera()

        # viewfinder
        cvf _ qtmmw.QCameraViewfinder()
        self.camera.setViewfinder(cvf)
        self.layout().addWidget(cvf)

        # Form
        form _ qtw.QFormLayout()
        self.layout().addLayout(form)

        # zoom
        zoomslider _ qtw.QSlider(
            minimum_1,
            maximum_10,
            sliderMoved_self.on_slider_moved,
            orientation_qtc.Qt.Horizontal
        )
        form.addRow('Zoom', zoomslider)

        self.camera.start()
        self.s..

    ___ on_slider_moved(self, value):

        focus _ self.camera.focus()
        focus.zoomTo(1, value)


if __name__ == '__main__':
    app _ qtw.?
    mw _ MainWindow()
    app.exec()
