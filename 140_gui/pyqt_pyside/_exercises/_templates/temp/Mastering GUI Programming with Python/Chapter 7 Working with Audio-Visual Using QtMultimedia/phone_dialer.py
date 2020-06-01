______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc
____ ? ______ QtMultimedia __ qtmm

______ resources


c_ SoundButton(qtw.?PB..):

    ___  -   wav_file, *args, **kwargs):
        s_. - (*args, **kwargs)
        wav_file _ wav_file
        player _ qtmm.QSoundEffect()
        player.setSource(qtc.QUrl.fromLocalFile(wav_file))
        c__.c..(player.play)


c_ MainWindow(qtw.QMainWindow):

    ___  -
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here
        dialpad _ qtw.?W..
        sCW..(dialpad)
        dialpad.sL..(qtw.QGridLayout())

        ___ i, symbol __ en..('123456789*0#'):
            button _ SoundButton(f':/dtmf/{symbol}.wav', symbol)
            row _ i // 3
            column _ i % 3
            dialpad.layout().aW..(button, row, column)

        # End main UI code
        s..


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
