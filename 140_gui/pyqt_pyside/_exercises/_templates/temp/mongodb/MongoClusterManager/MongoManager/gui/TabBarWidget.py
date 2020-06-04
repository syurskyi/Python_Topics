
____ ?.?C.. ______ QSize, __
____ ?.QtWidgets ______ QStylePainter, QStyleOptionTab, QTabBar, QStyle


c_ TabBarWidget(QTabBar):
    """
    TabBarWidget
    """
    ___  - (self, parent=None):
        tabSize = QSize(100, 25)
        super(TabBarWidget, self). - (parent)

    ___ paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionTab()

        for index in range(count()):
            initStyleOption(option, index)

            tab_rect = tabRect(index)
            tab_rect.moveLeft(10)

            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            painter.drawText(tab_rect, __.AlignVCenter | __.TextDontClip, tabText(index))

        painter.end()

    ___ tabSizeHint(self, index):
        return tabSize
