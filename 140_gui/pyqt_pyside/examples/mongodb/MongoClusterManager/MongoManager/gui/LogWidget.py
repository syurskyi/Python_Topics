from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QIcon
from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy


class LogWidget(QWidget):
    def __init__(self, parent=None):
        super(LogWidget, self).__init__(parent)

        # Base vars
        self.logLength = 0
        self.logger = logging.getLogger(__name__)

        # Palette
        logPalette = QPalette()
        logPalette.setColor(QPalette.Base, Qt.black)
        logPalette.setColor(QPalette.Text, Qt.yellow)

        # Text Panel
        self.logText = QPlainTextEdit(self)
        self.logText.setPalette(logPalette)
        self.logText.setReadOnly(True)

        # Buttons
        self.sendButton = QPushButton(QIcon('img/email.png'), 'Send Logs')
        self.sendButton.click.connect(self.sendLogs)
        self.forceButton = QPushButton(QIcon('img/refresh.png'), 'Force Refresh')
        self.forceButton.click.connect(self.forceRefresh)
        self.clearButton = QPushButton(QIcon('img/eraser.png'), 'Clear Logs')
        self.clearButton.click.connect(self.clearLogs)

        # Layouts
        layout = QVBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.addWidget(self.logText)

        buttonLayout = QHBoxLayout()
        buttonLayout.setContentsMargins(1, 0, 1, 2)
        buttonLayout.addWidget(self.sendButton)
        buttonLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        buttonLayout.addWidget(self.forceButton)
        buttonLayout.addWidget(self.clearButton)

        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        # Timer
        self.logTimer = QTimer()
        self.logTimer.setInterval(5000)
        self.logTimer.timeout.connect(self.updateLog)
        self.logTimer.start()

    def sendLogs(self):
        self.logger.info('[USER] Now sending logs...')

        try:
            smtp = smtplib.SMTP('localhost')

            with open(LOG_FILE, 'r') as file:
                content = file.read()

            smtp.sendmail('weblord@localhost.com', 'v.ducrocq@gmail.com', content)
        except SMTPException as s:
            self.logger.error('[SYSTEM] Error while sending mail : %s' % s)
            return

        self.logger.info('[USER] Mail sent!')

    def clearLogs(self):
        self.logger.info('[USER] Clear Logs requested.')
        open(LOG_FILE, 'w').close()
        self.updateLog()

    def updateLog(self):
        logs = open(LOG_FILE, 'r').read()

        if len(logs) != self.logLength:
            self.logLength = len(logs)

            self.logText.setPlainText(logs)
            self.logText.moveCursor(QTextCursor.End)

    def forceRefresh(self):
        self.logger.info('[USER] Force Log Refresh requested.')
        self.logLength = 0
        self.updateLog()


