____ ?.?C.. ______ __, QTimer
____ ?.?G.. ______ QPalette, QIcon
____ ?.?W.. ______ ?W.., QPlainTextEdit, ?PB.., ?VBL.., QHBoxLayout, QSpacerItem, QSizePolicy


c_ LogWidget(?W..):
    ___  -   parent_None):
        s__(LogWidget, self). - (parent)

        # Base vars
        logLength _ 0
        logger _ l__.gL..(__name__)

        # Palette
        logPalette _ QPalette()
        logPalette.setColor(QPalette.Base, __.black)
        logPalette.setColor(QPalette.Text, __.yellow)

        # Text Panel
        logText _ QPlainTextEdit(self)
        logText.setPalette(logPalette)
        logText.setReadOnly T..

        # Buttons
        sendButton _ ?PB..(QIcon('img/email.png'), 'Send Logs')
        sendButton.click.c__(sendLogs)
        forceButton _ ?PB..(QIcon('img/refresh.png'), 'Force Refresh')
        forceButton.click.c__(forceRefresh)
        clearButton _ ?PB..(QIcon('img/eraser.png'), 'Clear Logs')
        clearButton.click.c__(clearLogs)

        # Layouts
        layout _ ?VBL..(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.aW..(logText)

        buttonLayout _ QHBoxLayout()
        buttonLayout.setContentsMargins(1, 0, 1, 2)
        buttonLayout.aW..(sendButton)
        buttonLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        buttonLayout.aW..(forceButton)
        buttonLayout.aW..(clearButton)

        layout.addLayout(buttonLayout)
        sL..(layout)

        # Timer
        logTimer _ QTimer()
        logTimer.setInterval(5000)
        logTimer.timeout.c__(updateLog)
        logTimer.start()

    ___ sendLogs
        logger.i..('[USER] Now sending logs...')

        ___
            smtp _ smtplib.SMTP('localhost')

            with open(LOG_FILE, 'r') __ file:
                content _ file.read()

            smtp.sendmail('weblord@localhost.com', 'v.ducrocq@gmail.com', content)
        ______ SMTPException __ s:
            logger.error('[SYSTEM] Error while sending mail : %s' % s)
            r_

        logger.i..('[USER] Mail sent!')

    ___ clearLogs
        logger.i..('[USER] Clear Logs requested.')
        open(LOG_FILE, 'w').close()
        updateLog()

    ___ updateLog
        logs _ open(LOG_FILE, 'r').read()

        __ le.(logs) !_ logLength:
            logLength _ le.(logs)

            logText.setPlainText(logs)
            logText.moveCursor(QTextCursor.End)

    ___ forceRefresh
        logger.i..('[USER] Force Log Refresh requested.')
        logLength _ 0
        updateLog()


