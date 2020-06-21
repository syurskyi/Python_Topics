____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *
____ ?.?PS.. ______ *
____ ?.?M.. ______ *
____ ?.?MW.. ______ *

______ __
______ ___
______ t__


c_ MainWindow ?MW..

    ___  -   $ $$
        s__(MainWindow, self). - ($ $$)

        available_cameras _ ?CI__.aC..
        __ no. available_cameras:
            p.. #quit

        status _ ?SB..
        sSB..(status)


        save_path _ ""

        viewfinder _ ?CV..
        viewfinder.s..
        sCW..(viewfinder)

        # Set the default camera.
        select_camera(0)

        # Setup tools
        camera_toolbar _ QToolBar("Camera")
        camera_toolbar.setIconSize(?S..(14, 14))
        aTB..(camera_toolbar)

        photo_action _ ?A..(?I..(__.p__ .join('images', 'camera-black.png')), "Take photo...", self)
        photo_action.sST..("Take photo of current view")
        photo_action.t__.c..(take_photo)
        camera_toolbar.aA..(photo_action)

        change_folder_action _ ?A..(?I..(__.p__ .join('images', 'blue-folder-horizontal-open.png')), "Change save location...", self)
        change_folder_action.sST..("Change folder where photos are saved.")
        change_folder_action.t__.c..(change_folder)
        camera_toolbar.aA..(change_folder_action)


        camera_selector _ ?CB()
        camera_selector.aI..([c.description() ___ c __ available_cameras])
        camera_selector.currentIndexChanged.c..( select_camera )

        camera_toolbar.aW..(camera_selector)


        sWT..("NSAViewer")
        s..

    ___ select_camera  i):
        camera _ QCamera(available_cameras[i])
        camera.setViewfinder(viewfinder)
        camera.sCM..(QCamera.CaptureStillImage)
        camera.error.c..(l___: alert(camera.errorString()))
        camera.start()

        capture _ QCameraImageCapture(camera)
        capture.error.c..(l___ i, e, s: alert(s))
        capture.imageCaptured.c..(l___ d, i: status.sM..("Image %04d captured" % save_seq))

        current_camera_name _ available_cameras[i].description()
        save_seq _ 0

    ___ take_photo
        timestamp _ t__.strftime("%d-%b-%Y-%H_%M_%S")
        capture.capture(__.p__ .join(save_path, "%s-%04d-%s.jpg" % (
            current_camera_name,
            save_seq,
            timestamp
        )))
        save_seq +_ 1

    ___ change_folder
        pa__ _ ?FD...getExistingDirectory  "Snapshot save location", "")
        __ pa__:
            save_path _ pa__
            save_seq _ 0

    ___ alert  s):
        """
        Handle errors coming from QCamera dn QCameraImageCapture by displaying alerts.
        """
        err _ QErrorMessage
        err.sM..(s)


__ ______ __ ______

    app _ ?A..(___.a..
    app.sAN..("NSAViewer")

    window _ MainWindow()
    app.e..