____ ?.QtGui ______ *
____ ?.?W.. ______ *
____ ?.QtCore ______ *
____ ?.QtPrintSupport ______ *
____ ?.QtMultimedia ______ *
____ ?.QtMultimediaWidgets ______ *

______ os
______ sys
______ time


class MainWindow(QMainWindow):

    ___ __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.available_cameras _ QCameraInfo.availableCameras()
        if not self.available_cameras:
            pass #quit

        self.status _ QStatusBar()
        self.setStatusBar(self.status)


        self.save_path _ ""

        self.viewfinder _ QCameraViewfinder()
        self.viewfinder.s..
        self.setCentralWidget(self.viewfinder)

        # Set the default camera.
        self.select_camera(0)

        # Setup tools
        camera_toolbar _ QToolBar("Camera")
        camera_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(camera_toolbar)

        photo_action _ QAction(QIcon(os.path.join('images', 'camera-black.png')), "Take photo...", self)
        photo_action.setStatusTip("Take photo of current view")
        photo_action.triggered.c..(self.take_photo)
        camera_toolbar.addAction(photo_action)

        change_folder_action _ QAction(QIcon(os.path.join('images', 'blue-folder-horizontal-open.png')), "Change save location...", self)
        change_folder_action.setStatusTip("Change folder where photos are saved.")
        change_folder_action.triggered.c..(self.change_folder)
        camera_toolbar.addAction(change_folder_action)


        camera_selector _ QComboBox()
        camera_selector.addItems([c.description() for c in self.available_cameras])
        camera_selector.currentIndexChanged.c..( self.select_camera )

        camera_toolbar.addWidget(camera_selector)


        self.setWindowTitle("NSAViewer")
        self.s..

    ___ select_camera(self, i):
        self.camera _ QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.c..(lambda: self.alert(self.camera.errorString()))
        self.camera.start()

        self.capture _ QCameraImageCapture(self.camera)
        self.capture.error.c..(lambda i, e, s: self.alert(s))
        self.capture.imageCaptured.c..(lambda d, i: self.status.showMessage("Image %04d captured" % self.save_seq))

        self.current_camera_name _ self.available_cameras[i].description()
        self.save_seq _ 0

    ___ take_photo(self):
        timestamp _ time.strftime("%d-%b-%Y-%H_%M_%S")
        self.capture.capture(os.path.join(self.save_path, "%s-%04d-%s.jpg" % (
            self.current_camera_name,
            self.save_seq,
            timestamp
        )))
        self.save_seq +_ 1

    ___ change_folder(self):
        path _ QFileDialog.getExistingDirectory(self, "Snapshot save location", "")
        if path:
            self.save_path _ path
            self.save_seq _ 0

    ___ alert(self, s):
        """
        Handle errors coming from QCamera dn QCameraImageCapture by displaying alerts.
        """
        err _ QErrorMessage(self)
        err.showMessage(s)


if __name__ == '__main__':

    app _ QApplication(sys.argv)
    app.setApplicationName("NSAViewer")

    window _ MainWindow()
    app.e..