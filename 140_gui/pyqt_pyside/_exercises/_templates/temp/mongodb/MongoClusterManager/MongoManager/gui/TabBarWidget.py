
____ ?.?C.. ______ QSize, __
____ ?.QtWidgets ______ QStylePainter, QStyleOptionTab, QTabBar, QStyle


c_ TabBarWidget(QTabBar):
    """
    TabBarWidget
    """
    ___  -   parent_None):
        tabSize _ QSize(100, 25)
        super(TabBarWidget, self). - (parent)

    ___ paintEvent  event):
        painter _ QStylePainter(self)
        option _ QStyleOptionTab()

        ___ index in range(count()):
            initStyleOption(option, index)

            tab_rect _ tabRect(index)
            tab_rect.moveLeft(10)

            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            painter.drawText(tab_rect, __.AlignVCenter | __.TextDontClip, tabText(index))

        painter.end()

    ___ tabSizeHint  index):
        r_ tabSize
