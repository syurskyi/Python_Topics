
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QStylePainter, QStyleOptionTab, QTabBar, QStyle


class TabBarWidget(QTabBar):
    """
    TabBarWidget
    """
    def __init__(self, parent=None):
        self.tabSize = QSize(100, 25)
        super(TabBarWidget, self).__init__(parent)

    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionTab()

        for index in range(self.count()):
            self.initStyleOption(option, index)

            tab_rect = self.tabRect(index)
            tab_rect.moveLeft(10)

            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            painter.drawText(tab_rect, Qt.AlignVCenter | Qt.TextDontClip, self.tabText(index))

        painter.end()

    def tabSizeHint(self, index):
        return self.tabSize
