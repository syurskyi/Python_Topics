______ ___
____ ? ______ ?C.. __ qtc
____ ? ______ ?W.. __ qtw
____ ? ______ QtMultimedia __ qtmm
____ ? ______ QtMultimediaWidgets __ qtmmw


c_ MainWindow(qtw.?MW..):

    ___  -
        """MainWindow constructor.

        Code in this method should define window properties,
        create backend resources, etc.
        """
        s_. - ()
        # Main framework
        r..(qtc.?S..(800, 600))
        base_widget _ qtw.?W..
        base_widget.sL..(qtw.?HBL..
        notebook _ qtw.?TW..()
        base_widget.la__ .aW..(notebook)
        file_list _ ?.?LW..
        base_widget.la__ .aW..(file_list)

        sCW..(base_widget)

        # transport controls
        toolbar _ addToolBar("Transport")
        record_act _ toolbar.aA..('Rec')
        stop_act _ toolbar.aA..('Stop')
        play_act _ toolbar.aA..('Play')
        pause_act _ toolbar.aA..('Pause')

        # define the video directory
        video_dir _ qtc.QDir.home()
        __ no. video_dir.cd('captains_log'):
            qtc.QDir.home().mkdir('captains_log')
            video_dir.cd('captains_log')

        # Read the files in the directory
        refresh_video_list()

        ############
        # Playback #
        ############

        # setup the player and video widget
        player _ qtmm.QMediaPlayer()
        video_widget _ qtmmw.QVideoWidget()
        player.setVideoOutput(video_widget)
        notebook.aT..(video_widget, "Play")

        # connect the transport
        play_act.t__.c..(player.play)
        pause_act.t__.c..(player.pause)
        stop_act.t__.c..(player.stop)
        play_act.t__.c..(
            l___: notebook.setCurrentWidget(video_widget))

        # connect file list
        file_list.itemDoubleClicked.c..(
            on_file_selected)
        file_list.itemDoubleClicked.c..(
            l___: notebook.setCurrentWidget(video_widget))



        #############
        # Recording #
        #############

        # set up camera
        camera _ camera_check()
        __ no. camera:
            s..
            r_
        camera.setCaptureMode(qtmm.QCamera.CaptureVideo)

        # Create the viewfinder widget for recording
        cvf _ qtmmw.QCameraViewfinder()
        camera.setViewfinder(cvf)
        notebook.aT..(cvf, 'Record')

        # start the camera
        camera.start()

        # Configure recorder
        recorder _ qtmm.QMediaRecorder(camera)
        #settings = self.recorder.videoSettings()
        #settings.setResolution(640, 480)
        #settings.setFrameRate(24.0)
        #settings.setQuality(qtmm.QMultimedia.VeryHighQuality)
        #self.recorder.setVideoSettings(settings)

        # connect the transport
        record_act.t__.c..(record)
        record_act.t__.c..(
            l___: notebook.setCurrentWidget(cvf)
        )
        pause_act.t__.c..(recorder.pause)
        stop_act.t__.c..(recorder.stop)

        # refresh the files when the recording is made
        stop_act.t__.c..(refresh_video_list)


        s..

    ######################
    # Playback callbacks #
    ######################

    ___ refresh_video_list
        file_list.c..
        video_files _ video_dir.entryList(
            ["*.ogg", "*.avi", "*.mov", "*.mp4", "*.mkv"],
            qtc.QDir.Files | qtc.QDir.Readable
        )
        ___ fn __ sorted(video_files):
            file_list.aI..(fn)

    ___ on_file_selected  item):
        fn _ item.t__()
        url _ qtc.QUrl.fromLocalFile(video_dir.filePath(fn))
        content _ qtmm.QMediaContent(url)
        player.setMedia(content)
        player.play()

    #######################
    # Recording callbacks #
    #######################

    ___ camera_check
        cameras _ qtmm.QCameraInfo.availableCameras()
        print(cameras)
        __ no. cameras:
            qtw.?MB...c..(
                self,
                'No cameras',
                'No cameras were found, recording disabled.'
            )
        ____
            r_ qtmm.QCamera(cameras[0])

    ___ record
        # create a filename
        datestamp _ qtc.QDateTime.currentDateTime().toString()
        mediafile _ qtc.QUrl.fromLocalFile(
            video_dir.filePath('log - ' + datestamp)
        )
        recorder.setOutputLocation(mediafile)
        # start recording
        recorder.record()

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
