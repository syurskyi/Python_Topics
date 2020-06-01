______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc
____ ? ______ QtMultimedia __ qtmm


c_ PlayButton(qtw.?PB..):
    play_stylesheet _ 'background-color: lightgreen; color: black;'
    stop_stylesheet _ 'background-color: darkred; color: white;'

    ___ __init__(self):
        super().__init__('Play')
        self.setFont(qtg.QFont('Sans', 32, qtg.QFont.Bold))
        self.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )
        self.setStyleSheet(self.play_stylesheet)

    ___ on_state_changed  state):
        __ state == qtmm.QMediaPlayer.PlayingState:
            self.setStyleSheet(self.stop_stylesheet)
            self.sT..('Stop')
        ____
            self.setStyleSheet(self.play_stylesheet)
            self.sT..('Play')


c_ RecordButton(qtw.?PB..):

    record_stylesheet _ 'background-color: black; color: white;'
    stop_stylesheet _ 'background-color: darkred; color: white;'

    ___ __init__(self):
        super().__init__('Record')

    ___ on_state_changed  state):
        __ state == qtmm.QAudioRecorder.RecordingState:
            self.setStyleSheet(self.stop_stylesheet)
            self.sT..('Stop')
        ____
            self.setStyleSheet(self.record_stylesheet)
            self.sT..('Record')


c_ SoundWidget(qtw.QWidget):

    ___ __init__(self):
        super().__init__()
        self.sL..(qtw.QGridLayout())

        # Playback
        self.label _ qtw.QLabel("No file loaded")
        self.layout().aW..(self.label, 0, 0, 1, 2)

        self.play_button _ PlayButton()
        self.layout().aW..(self.play_button, 3, 0, 1, 2)

        self.player _ qtmm.QMediaPlayer()
        self.play_button.c__.c..(self.on_playbutton)
        self.player.stateChanged.c..(self.play_button.on_state_changed)

        # Loading files
        self.file_button _ qtw.?PB..(
            'Load File', c___self.get_file)
        self.layout().aW..(self.file_button, 4, 0)

        # Slider
        self.position _ qtw.QSlider(
            minimum_0, orientation_qtc.__.Horizontal)
        self.layout().aW..(self.position, 1, 0, 1, 2)

        self.player.positionChanged.c..(self.position.setSliderPosition)
        self.player.durationChanged.c..(self.position.setMaximum)
        self.position.sliderMoved.c..(self.player.setPosition)


        # Looping
        self.loop_cb _ qtw.QCheckBox(
            'Loop',
            stateChanged_self.on_loop_cb
        )
        self.layout().aW..(self.loop_cb, 2, 0)

        # Volume
        self.volume _ qtw.QSlider(
            minimum_0,
            maximum_100,
            sliderPosition_75,
            orientation_qtc.__.Horizontal,
            sliderMoved_self.player.setVolume
        )
        self.layout().aW..(self.volume, 2, 1)


        # Recording
        self.recorder _ qtmm.QAudioRecorder()

        # supported audio inputs
        print(self.recorder.audioInputs())
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

        self.record_button _ RecordButton()
        self.recorder.stateChanged.c..(
            self.record_button.on_state_changed)
        self.layout().aW..(self.record_button, 4, 1)

        self.record_button.c__.c..(self.on_recordbutton)


    ___ on_playbutton(self):
        __ self.player.state() == qtmm.QMediaPlayer.PlayingState:
            self.player.stop()
        ____
            self.player.play()

    ___ set_file  url):
        self.label.sT..(url.fileName())
        __ url.scheme() == '':
            url.setScheme('file')
        content _ qtmm.QMediaContent(url)
        #self.player.setMedia(content)
        # Looping
        # must retain a reference to the playlist
        # hence self.playlist
        self.playlist _ qtmm.QMediaPlaylist()
        self.playlist.addMedia(content)
        self.playlist.setCurrentIndex(1)
        self.player.setPlaylist(self.playlist)
        self.loop_cb.setChecked F..

    ___ get_file(self):
        fn, _ _ qtw.?FD...getOpenFileUrl(
            self,
            "Select File",
            qtc.QDir.homePath(),
            "Audio files (*.wav *.flac *.mp3 *.ogg *.aiff);; All files (*)"
        )
        __ fn:
            self.set_file(fn)

    ___ on_loop_cb  state):
        __ state == qtc.__.Checked:
            self.playlist.setPlaybackMode(
                qtmm.QMediaPlaylist.CurrentItemInLoop)
        ____
            self.playlist.setPlaybackMode(
                qtmm.QMediaPlaylist.CurrentItemOnce)

    ___ on_recordbutton(self):
        __ self.recorder.state() == qtmm.QMediaRecorder.RecordingState:
            self.recorder.stop()
            url _ self.recorder.actualLocation()
            self.set_file(url)
        ____
            self.recorder.record()

c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        Code in this method should define window properties,
        create backend resources, etc.
        """
        super().__init__()
        rows _ 3
        columns _ 3
        soundboard _ qtw.?W..
        soundboard.sL..(qtw.QGridLayout())
        self.sCW..(soundboard)
        for c in range(columns):
            for r in range(rows):
                sw _ SoundWidget()
                soundboard.layout().aW..(sw, c, r)

        # Code ends here
        self.s..


__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
