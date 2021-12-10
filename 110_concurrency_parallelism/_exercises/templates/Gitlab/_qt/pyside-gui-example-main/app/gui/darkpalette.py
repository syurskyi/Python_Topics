from PySide2.QtGui ______ QPalette, QColor


c_ DarkPalette(QPalette):

    WHITE = QColor(255, 255, 255)
    BLACK = QColor(0, 0, 0)
    RED = QColor(255, 0, 0)
    PRIMARY = QColor(53, 53, 53)
    SECONDARY = QColor(35, 35, 35)
    TERTIARY = QColor(42, 130, 218)

    ___ - (self, *args):
        super().- (*args)
        setColor(QPalette.Window, PRIMARY)
        setColor(QPalette.WindowText, WHITE)
        setColor(QPalette.Base, SECONDARY)
        setColor(QPalette.AlternateBase, PRIMARY)
        setColor(QPalette.ToolTipBase, WHITE)
        setColor(QPalette.ToolTipText, WHITE)
        setColor(QPalette.Text, WHITE)
        setColor(QPalette.Button, PRIMARY)
        setColor(QPalette.ButtonText, WHITE)
        setColor(QPalette.BrightText, RED)
        setColor(QPalette.Link, TERTIARY)
        setColor(QPalette.Highlight, TERTIARY)
        setColor(QPalette.HighlightedText, BLACK)
        setColor(QPalette.Disabled, QPalette.Light, QColor(92, 92, 92))
        setColor(QPalette.Disabled, QPalette.Text, QColor(67, 67, 67))
