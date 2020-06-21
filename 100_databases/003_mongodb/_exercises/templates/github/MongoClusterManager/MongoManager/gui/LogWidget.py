____ ?.?C.. _______ Qt, QTimer
____ ?.?G.. _______ QPalette, QIcon
____ ?.?W.. _______ QWidget, QPlainTextEdit, ?PB.., QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy


c_ LogWidget(QWidget):
    ___  - (self, p.._N..
        s__(LogWidget, self). - ?

        # Base vars
        logLength = 0
        logger = logging.getLogger(__name__)

        # Palette
        logPalette = QPalette()
        logPalette.setColor(QPalette.Base, Qt.black)
        logPalette.setColor(QPalette.Text, Qt.yellow)

        # Text Panel
        logText = QPlainTextEdit(self)
        logText.setPalette(logPalette)
        logText.setReadOnly(True)

        # Buttons
        sendButton = ?PB..(QIcon('img/email.png'), 'Send Logs')
        sendButton.click.c..(sendLogs)
        forceButton = ?PB..(QIcon('img/refresh.png'), 'Force Refresh')
        forceButton.click.c..(forceRefresh)
        clearButton = ?PB..(QIcon('img/eraser.png'), 'Clear Logs')
        clearButton.click.c..(clearLogs)

        # Layouts
        layout = QVBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.aW..(logText)

        buttonLayout = QHBoxLayout()
        buttonLayout.setContentsMargins(1, 0, 1, 2)
        buttonLayout.aW..(sendButton)
        buttonLayout.aI..(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        buttonLayout.aW..(forceButton)
        buttonLayout.aW..(clearButton)

        layout.addLayout(buttonLayout)
        sL..(layout)

        # Timer
        logTimer = QTimer()
        logTimer.setInterval(5000)
        logTimer.timeout.c..(updateLog)
        logTimer.start()

    ___ sendLogs
        logger.info('[USER] Now sending logs...')

        ___
            smtp = smtplib.SMTP('localhost')

            with open(LOG_FILE, 'r') as file:
                content = file.read()

            smtp.sendmail('weblord@localhost.com', 'v.ducrocq@gmail.com', content)
        except SMTPException as s:
            logger.error('[SYSTEM] Error while sending mail : %s' % s)
            return

        logger.info('[USER] Mail sent!')

    ___ clearLogs
        logger.info('[USER] Clear Logs requested.')
        open(LOG_FILE, 'w').c..
        updateLog()

    ___ updateLog
        logs = open(LOG_FILE, 'r').read()

        __ le.(logs) != logLength:
            logLength = le.(logs)

            logText.setPlainText(logs)
            logText.moveCursor(QTextCursor.End)

    ___ forceRefresh
        logger.info('[USER] Force Log Refresh requested.')
        logLength = 0
        updateLog()


