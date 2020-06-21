
____ ?.?C.. _______ QSize, Qt
____ ?.?W.. _______ QStylePainter, QStyleOptionTab, QTabBar, QStyle


c_ TabBarWidget(QTabBar):
    """
    TabBarWidget
    """
    ___  - (self, p.._N..
        tabSize = QSize(100, 25)
        s__(TabBarWidget, self). - ?

    ___ paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionTab()

        ___ index __ ra..(count()):
            initStyleOption(option, index)

            tab_rect = tabRect(index)
            tab_rect.moveLeft(10)

            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            painter.drawText(tab_rect, Qt.AlignVCenter | Qt.TextDontClip, tabText(index))

        painter.end()

    ___ tabSizeHint(self, index):
        return tabSize
