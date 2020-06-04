____ ?.?C.. ______ __, QTimer
____ ?.QtGui ______ QPalette, QIcon
____ ?.QtWidgets ______ QWidget, QPlainTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy


c_ LogWidget(QWidget):
    ___  - (self, parent=None):
        super(LogWidget, self). - (parent)

        # Base vars
        logLength = 0
        logger = l__.gL..(__name__)

        # Palette
        logPalette = QPalette()
        logPalette.setColor(QPalette.Base, __.black)
        logPalette.setColor(QPalette.Text, __.yellow)

        # Text Panel
        logText = QPlainTextEdit(self)
        logText.setPalette(logPalette)
        logText.setReadOnly T..

        # Buttons
        sendButton = QPushButton(QIcon('img/email.png'), 'Send Logs')
        sendButton.click.c__(sendLogs)
        forceButton = QPushButton(QIcon('img/refresh.png'), 'Force Refresh')
        forceButton.click.c__(forceRefresh)
        clearButton = QPushButton(QIcon('img/eraser.png'), 'Clear Logs')
        clearButton.click.c__(clearLogs)

        # Layouts
        layout = QVBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.addWidget(logText)

        buttonLayout = QHBoxLayout()
        buttonLayout.setContentsMargins(1, 0, 1, 2)
        buttonLayout.addWidget(sendButton)
        buttonLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        buttonLayout.addWidget(forceButton)
        buttonLayout.addWidget(clearButton)

        layout.addLayout(buttonLayout)
        setLayout(layout)

        # Timer
        logTimer = QTimer()
        logTimer.setInterval(5000)
        logTimer.timeout.c__(updateLog)
        logTimer.start()

    ___ sendLogs
        logger.info('[USER] Now sending logs...')

        try:
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
        open(LOG_FILE, 'w').close()
        updateLog()

    ___ updateLog
        logs = open(LOG_FILE, 'r').read()

        if len(logs) != logLength:
            logLength = len(logs)

            logText.setPlainText(logs)
            logText.moveCursor(QTextCursor.End)

    ___ forceRefresh
        logger.info('[USER] Force Log Refresh requested.')
        logLength = 0
        updateLog()


