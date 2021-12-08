from PySide2.QtGui import QPalette, QColor


class DarkPalette(QPalette):

    WHITE = QColor(255, 255, 255)
    BLACK = QColor(0, 0, 0)
    RED = QColor(255, 0, 0)
    PRIMARY = QColor(53, 53, 53)
    SECONDARY = QColor(35, 35, 35)
    TERTIARY = QColor(42, 130, 218)

    def __init__(self, *args):
        super().__init__(*args)
        self.setColor(QPalette.Window, self.PRIMARY)
        self.setColor(QPalette.WindowText, self.WHITE)
        self.setColor(QPalette.Base, self.SECONDARY)
        self.setColor(QPalette.AlternateBase, self.PRIMARY)
        self.setColor(QPalette.ToolTipBase, self.WHITE)
        self.setColor(QPalette.ToolTipText, self.WHITE)
        self.setColor(QPalette.Text, self.WHITE)
        self.setColor(QPalette.Button, self.PRIMARY)
        self.setColor(QPalette.ButtonText, self.WHITE)
        self.setColor(QPalette.BrightText, self.RED)
        self.setColor(QPalette.Link, self.TERTIARY)
        self.setColor(QPalette.Highlight, self.TERTIARY)
        self.setColor(QPalette.HighlightedText, self.BLACK)
        self.setColor(QPalette.Disabled, QPalette.Light, QColor(92, 92, 92))
        self.setColor(QPalette.Disabled, QPalette.Text, QColor(67, 67, 67))
