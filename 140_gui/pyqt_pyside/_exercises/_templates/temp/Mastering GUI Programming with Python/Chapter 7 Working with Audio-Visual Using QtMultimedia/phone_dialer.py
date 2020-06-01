______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtCore as qtc
____ ? ______ QtMultimedia as qtmm

______ resources


class SoundButton(qtw.?PB..):

    ___ __init__(self, wav_file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wav_file _ wav_file
        self.player _ qtmm.QSoundEffect()
        self.player.setSource(qtc.QUrl.fromLocalFile(wav_file))
        self.c__.c..(self.player.play)


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        dialpad _ qtw.QWidget()
        self.setCentralWidget(dialpad)
        dialpad.setLayout(qtw.QGridLayout())

        for i, symbol in enumerate('123456789*0#'):
            button _ SoundButton(f':/dtmf/{symbol}.wav', symbol)
            row _ i // 3
            column _ i % 3
            dialpad.layout().addWidget(button, row, column)

        # End main UI code
        self.s..


if __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
