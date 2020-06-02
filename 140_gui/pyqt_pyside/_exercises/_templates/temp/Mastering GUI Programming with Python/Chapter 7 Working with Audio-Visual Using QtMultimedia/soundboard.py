______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc
____ ? ______ ?M.. __ qtmm


c_ PlayButton ?.?PB..
    play_stylesheet _ 'background-color: lightgreen; color: black;'
    stop_stylesheet _ 'background-color: darkred; color: white;'

    ___  - 
        s_. - Play
        sF..?.?F.. 'Sans' 32 ?.?F...B..
        sSP..
            ?.?SP...E..,
            ?.?SP...E..

        sSS.. p_s_

    ___ on_state_changed  state
        __ state __ ?.?MP__.PS..
            sSS.. s_s..
            sT.. Stop
        ____
            sSS.. p_s_
            sT.. Play


c_ RecordButton ?.?PB.

    record_stylesheet _ 'background-color: black; color: white;'
    stop_stylesheet _ 'background-color: darkred; color: white;'

    ___  - 
        s_. - Record

    ___ on_state_changed  state
        __ state __ ?.?AR...RS..
            sSS.. s_s..
            sT.. Stop
        ____
            sSS.. r_s..
            sT.. Record


c_ SoundWidget ?.?W..

    ___  - 
        s_. -
        sL.. ?.?GL..

        # Playback
        label _ ?.?L.. No file loaded
        la__ .aW.. ? 0, 0, 1, 2

        play_button _ ?
        la__ .aW.. ? 3, 0, 1, 2

        player _ ?.?MP..
        p_b_.c__.c.. o_p..
        ?.sC__.c.. p_b_.o_s_c..

        # Loading files
        file_button _ ?.?PB..
            'Load File' c___s.g_f..
        la__ .aW.. f_b.. 4, 0

        # Slider
        position _ ?.?S..
            m.._0 o.._?.__.H..
        la__ .aW.. p.. 1, 0, 1, 2

        p_.pC...c.. p__.sSP..
        p_.dC...c.. p__.sM..
        p__.sM__.c.. p_.sP..


        # Looping
        loop_cb _ ?.?CB..
            'Loop'
            sC.._s.o_l_c

        la__ .aW.. ? 2, 0

        # Volume
        volume _ ?.?S..
            mi.._0
            ma.._100
            sP.._75
            or.._?.__.H..
            sM.._s...p_.sV..
        )
        la__ .aW.. ? 2, 1


        # Recording
        recorder _ ?.?AR..

        # supported audio inputs
        print r__.aI..
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

        record_button _ ?
        r__.sC__.c..
            ?.o___
        la__ .aW.. r_b.. 4, 1

        ?.c__.c.. o_r..


    ___ on_playbutton
        __ p_.s.. __ ?.?MP...PS..
            p_.s..
        ____
            p_.p..

    ___ set_file  url
        la__.sT.. ?.fN..
        __ ?.s.. __ ''
            ?.sS.. f..
        content _ ?.?MC.. ?
        #self.p_.setMedia(content)
        # Looping
        # must retain a reference to the playlist
        # hence self.playlist
        playlist _ ?.?MP..
        ?.aM.. c..
        ?.sCI.. 1
        p_.sPl.. ?
        l_c_.sC__ F..

    ___ get_file
        fn _ _ qtw.?FD...gOFU..

            Select File
            ?.?D...hP..
            "Audio files (*.wav *.flac *.mp3 *.ogg *.aiff);; All files (*)"

        __ fn
            s_f.. ?

    ___ on_loop_cb  state
        __ state __ qtc.__.Ch..
            ?.sPk..
                ?.?MPl...CIIL..
        ____
            ?.setPlaybackMode
                ?.?MPl...CIO..

    ___ on_recordbutton
        __ r__.s.. __ ?.?MR...RS..
            r__.s..
            url _ r__.aL..
            s_f.. ?
        ____
            r__.r..

c_ MainWindow ?.?MW..

    ___  - 
        """MainWindow constructor.

        Code in this method should define window properties,
        create backend resources, etc.
        """
        s_. -
        rows _ 3
        columns _ 3
        soundboard _ ?.?W..
        ?.sL.. ?.?GL..
        sCW.. ?
        ___ c __ ra.. c..
            ___ r __ ra.. r..
                sw _ ?
                s__.la__ .aW.. sw, c, r)

        # Code ends here
        s..


__ ______ __ ______
    app _ qtw.?A.. ___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ ?
    ___.e.. ?.e..
