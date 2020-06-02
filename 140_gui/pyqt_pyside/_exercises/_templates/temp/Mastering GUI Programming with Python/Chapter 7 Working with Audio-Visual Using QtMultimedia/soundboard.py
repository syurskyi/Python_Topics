______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc
____ ? ______ ?M.. __ qtmm


c_ PlayButton(qtw.?PB..):
    play_stylesheet _ 'background-color: lightgreen; color: black;'
    stop_stylesheet _ 'background-color: darkred; color: white;'

    ___  - 
        s_. - ('Play')
        setFont(qtg.QFont('Sans', 32, qtg.QFont.Bold))
        sSP..(
            ?.?SP...E..,
            ?.?SP...E..
        )
        setStyleSheet(play_stylesheet)

    ___ on_state_changed  state):
        __ state __ qtmm.QMediaPlayer.PlayingState:
            setStyleSheet(stop_stylesheet)
            sT..('Stop')
        ____
            setStyleSheet(play_stylesheet)
            sT..('Play')


c_ RecordButton(qtw.?PB..):

    record_stylesheet _ 'background-color: black; color: white;'
    stop_stylesheet _ 'background-color: darkred; color: white;'

    ___  - 
        s_. - ('Record')

    ___ on_state_changed  state):
        __ state __ qtmm.QAudioRecorder.RecordingState:
            setStyleSheet(stop_stylesheet)
            sT..('Stop')
        ____
            setStyleSheet(record_stylesheet)
            sT..('Record')


c_ SoundWidget ?.?W..

    ___  - 
        s_. - ()
        sL..(qtw.QGridLayout())

        # Playback
        label _ ?.?L..("No file loaded")
        la__ .aW..(label, 0, 0, 1, 2)

        play_button _ PlayButton()
        la__ .aW..(play_button, 3, 0, 1, 2)

        player _ qtmm.QMediaPlayer()
        play_button.c__.c..(on_playbutton)
        player.stateChanged.c..(play_button.on_state_changed)

        # Loading files
        file_button _ qtw.?PB..(
            'Load File', c___self.get_file)
        la__ .aW..(file_button, 4, 0)

        # Slider
        position _ qtw.QSlider(
            minimum_0, orientation_qtc.__.H..)
        la__ .aW..(position, 1, 0, 1, 2)

        player.positionChanged.c..(position.setSliderPosition)
        player.durationChanged.c..(position.setMaximum)
        position.sliderMoved.c..(player.setPosition)


        # Looping
        loop_cb _ ?.?CB..(
            'Loop',
            stateChanged_self.on_loop_cb
        )
        la__ .aW..(loop_cb, 2, 0)

        # Volume
        volume _ qtw.QSlider(
            minimum_0,
            maximum_100,
            sliderPosition_75,
            orientation_qtc.__.H..,
            sliderMoved_self.player.setVolume
        )
        la__ .aW..(volume, 2, 1)


        # Recording
        recorder _ qtmm.QAudioRecorder()

        # supported audio inputs
        print(recorder.audioInputs())
        #self.recorder.setAudioInput('default:')

        # Overriding sound recording settings
        #settings = qtmm.QAudioEncoderSettings()
        #settings.setCodec('audio/pcm')
        #settings.setSampleRate(44100)
        #settings.setQuality(qtmm.QMultimedia.HighQuality)
        #self.recorder.setEncodingSettings(settings)
        #self.recorder.setContainerFormat('audio/x-wav')
        #self.recorder.setOutputLocation(
        #    qtc.QUrl.fromLocalFile(qtc.QDir.home().filePath('sample1')))

        record_button _ RecordButton()
        recorder.stateChanged.c..(
            record_button.on_state_changed)
        la__ .aW..(record_button, 4, 1)

        record_button.c__.c..(on_recordbutton)


    ___ on_playbutton
        __ player.state() __ qtmm.QMediaPlayer.PlayingState:
            player.stop()
        ____
            player.play()

    ___ set_file  url):
        label.sT..(url.fileName())
        __ url.scheme() __ '':
            url.setScheme('file')
        content _ qtmm.QMediaContent(url)
        #self.player.setMedia(content)
        # Looping
        # must retain a reference to the playlist
        # hence self.playlist
        playlist _ qtmm.QMediaPlaylist()
        playlist.addMedia(content)
        playlist.setCurrentIndex(1)
        player.setPlaylist(playlist)
        loop_cb.sC__ F..

    ___ get_file
        fn, _ _ qtw.?FD...getOpenFileUrl(
            self,
            "Select File",
            qtc.QDir.homePath(),
            "Audio files (*.wav *.flac *.mp3 *.ogg *.aiff);; All files (*)"
        )
        __ fn:
            set_file(fn)

    ___ on_loop_cb  state):
        __ state __ qtc.__.Checked:
            playlist.setPlaybackMode(
                qtmm.QMediaPlaylist.CurrentItemInLoop)
        ____
            playlist.setPlaybackMode(
                qtmm.QMediaPlaylist.CurrentItemOnce)

    ___ on_recordbutton
        __ recorder.state() __ qtmm.QMediaRecorder.RecordingState:
            recorder.stop()
            url _ recorder.actualLocation()
            set_file(url)
        ____
            recorder.record()

c_ MainWindow(qtw.?MW..):

    ___  - 
        """MainWindow constructor.

        Code in this method should define window properties,
        create backend resources, etc.
        """
        s_. - ()
        rows _ 3
        columns _ 3
        soundboard _ qtw.?W..
        soundboard.sL..(qtw.QGridLayout())
        sCW..(soundboard)
        ___ c __ ra..(columns):
            ___ r __ ra..(rows):
                sw _ SoundWidget()
                soundboard.la__ .aW..(sw, c, r)

        # Code ends here
        s..


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
