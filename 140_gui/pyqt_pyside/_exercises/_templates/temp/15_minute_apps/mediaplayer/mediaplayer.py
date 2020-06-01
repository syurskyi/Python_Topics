____ ?.QtGui ______ *
____ ?.?W.. ______ *
____ ?.QtCore ______ *
____ ?.QtMultimedia ______ *
____ ?.QtMultimediaWidgets ______ *

____ MainWindow ______ Ui_MainWindow

___ hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 360000
    h, r _ divmod(ms, 36000)
    m, r _ divmod(r, 60000)
    s, _ _ divmod(r, 1000)
    return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))

class ViewerWindow(QMainWindow):
    state _ pyqtSignal(bool)

    ___ closeEvent(self, e):
        # Emit the window state, to update the viewer toggle button.
        self.state.emit(False)


class PlaylistModel(QAbstractListModel):
    ___ __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist _ playlist

    ___ data(self, index, role):
        if role == Qt.DisplayRole:
            media _ self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    ___ rowCount(self, index):
        return self.playlist.mediaCount()


class MainWindow(QMainWindow, Ui_MainWindow):
    ___ __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.player _ QMediaPlayer()

        self.player.error.c..(self.erroralert)
        self.player.play()

        # Setup the playlist.
        self.playlist _ QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        # Add viewer for video playback, separate floating window.
        self.viewer _ ViewerWindow(self)
        self.viewer.setWindowFlags(self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(QSize(480,360))

        videoWidget _ QVideoWidget()
        self.viewer.setCentralWidget(videoWidget)
        self.player.setVideoOutput(videoWidget)

        # Connect control buttons/slides for media player.
        self.playButton.pressed.c..(self.player.play)
        self.pauseButton.pressed.c..(self.player.pause)
        self.stopButton.pressed.c..(self.player.stop)
        self.volumeSlider.valueChanged.c..(self.player.setVolume)

        self.viewButton.toggled.c..(self.toggle_viewer)
        self.viewer.state.c..(self.viewButton.setChecked)

        self.previousButton.pressed.c..(self.playlist.previous)
        self.nextButton.pressed.c..(self.playlist.next)

        self.model _ PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlist.currentIndexChanged.c..(self.playlist_position_changed)
        selection_model _ self.playlistView.selectionModel()
        selection_model.selectionChanged.c..(self.playlist_selection_changed)

        self.player.durationChanged.c..(self.update_duration)
        self.player.positionChanged.c..(self.update_position)
        self.timeSlider.valueChanged.c..(self.player.setPosition)

        self.open_file_action.triggered.c..(self.open_file)

        self.setAcceptDrops(True)

        self.s..

    ___ dragEnterEvent(self, e):
        if e.mimeData().hasUrls
            e.acceptProposedAction()

    ___ dropEvent(self, e):
        for url in e.mimeData().urls
            self.playlist.addMedia(
                QMediaContent(url)
            )

        self.model.layoutChanged.emit()

        # If not playing, seeking to first of newly added + play.
        if self.player.state() !_ QMediaPlayer.PlayingState:
            i _ self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()

    ___ open_file(self):
        path, _ _ QFileDialog.getOpenFileName(self, "Open file", "", "mp3 Audio (*.mp3);mp4 Video (*.mp4);Movie files (*.mov);All files (*.*)")

        if path:
            self.playlist.addMedia(
                QMediaContent(
                    QUrl.fromLocalFile(path)
                )
            )

        self.model.layoutChanged.emit()

    ___ update_duration(self, duration):
        print("!", duration)
        print("?", self.player.duration())
        
        self.timeSlider.setMaximum(duration)

        if duration >_ 0:
            self.totalTimeLabel.sT..(hhmmss(duration))

    ___ update_position(self, position):
        if position >_ 0:
            self.currentTimeLabel.sT..(hhmmss(position))

        # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    ___ playlist_selection_changed(self, ix):
        # We receive a QItemSelection from selectionChanged.
        i _ ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    ___ playlist_position_changed(self, i):
        if i > -1:
            ix _ self.model.index(i)
            self.playlistView.setCurrentIndex(ix)

    ___ toggle_viewer(self, state):
        if state:
            self.viewer.s..
        else:
            self.viewer.hide()

    ___ erroralert(self, *args):
        print(args)




if __name__ == '__main__':
    app _ ?
    app.setApplicationName("Failamp")
    app.setStyle("Fusion")

    # Fusion dark palette from https://gist.github.com/QuantumCD/6245215.
    palette _ QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    window _ MainWindow()
    app.e..
