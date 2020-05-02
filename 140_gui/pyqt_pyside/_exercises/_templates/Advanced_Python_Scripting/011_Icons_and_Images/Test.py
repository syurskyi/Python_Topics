# -*- coding: utf-8 -*-
# ! /usr/bin/env python

_____ ___
____ PyQt4 _____ QtGui, ?C..

_____ os, string
_____ math

THUMB_WIDTH = 128
THUMB_HEIGHT = 128
THUMB_MIN = 64
THUMB_MAX = 256
FILE_TYPE = ['jpg', 'jpeg', 'tif', 'bmp', 'gif']


c_ ImageWidget(QtGui.?W..

    prevSelected = None

    """
    Use this widget to display image.
    """

    ___  -  
        super(ImageWidget, self). - ()
        id = 0
        displayText = ''
        version = ''
        status = 0
        path = ''
        showStatus = T..
        selected = False
        isHightlight = False
        thumb = QtGui.QImage()
        initAttrib()

    ___ initAttrib 
        name_font = QtGui.QFont()
        bg_color = QtGui.QColor(50, 50, 50)
        hightlight = QtGui.QColor(255, 255, 255, 100)
        edge_size = 5
        pen_selected = QtGui.QPen(QtGui.QColor(255, 255, 0))
        pen_selected.setWidth(edge_size)
        pen_selected.setJoinStyle(?C...Qt.MiterJoin)

    #        self.setToolTip('aaaa\nbbbb\ncccc')

    ___ assetFile 
        return path + "_asset_.txt"

    ___ thumbFile 
        return path + "_thumb_.png"

    ___ informationFile 
        return path + "_information_.txt"

    ___ getPublishPath 
        current_version = version
        __ not current_version:
            current_version = '000'
        new_version = int(string.atof(current_version)) + 1
        return '%s/%03d' % (path, new_version)

    ___ getVersionPath , version
        return '%s/%s' % (path, version)

    ___ getCurrentVersionPath 
        return getVersionPath(version)

    ___ setThumb , thumb=None
        __ not thumb:
            thumb = thumbFile()
        __ os.path.isfile(thumb
            thumb.load(?C...QString(thumb))
            repaint()
            return T..

    ___ paintAsThumb , painter
        name_height = max(height() * 0.15, 20)
        name_ty = height() - edge_size * 2
        # draw background
        painter.fillRect(rect(), bg_color)
        painter.drawImage(rect(), thumb)
        # draw hightlight
        __ isHightlight and not selected:
            painter.fillRect(rect(), hightlight)
        # draw name
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255)))
        name_font.setPixelSize(name_height)
        painter.setFont(name_font)
        # 脚标字符
        painter.drawText(edge_size, name_ty, st.(displayText))

        __ status:
            title_height = edge_size + name_height
            p1 = ?C...QPoint(0, 0)
            p2 = ?C...QPoint(0, title_height)
            p3 = ?C...QPoint(title_height, 0)
            painter.setPen(?C...Qt.NoPen)
            painter.fillRect(0, 0, width(), title_height, QtGui.QColor(40, 40, 40, 40))
            __ status __ 1:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
            elif status __ 2:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
            elif status __ 3:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 0, 255)))
            painter.drawConvexPolygon(p1, p2, p3)

        __ version:
            version_x = width() - edge_size - name_height * 1.5
            version_y = name_height
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255)))
            painter.drawText(version_x, version_y, '%s' % version)

        # draw selected
        __ selected:
            painter.setPen(pen_selected)
            painter.setBrush(?C...Qt.NoBrush)
            painter.drawRect(edge_size / 2, edge_size / 2, \
                             width() - edge_size, height() - edge_size)

    ___ paintEvent , event
        painter = QtGui.QPainter
        paintAsThumb(painter)

    ___ mouseReleaseEvent , event
        __ event.button() __ ?C...Qt.LeftButton:
            setSelected()

    ___ mouseDoubleClickEvent , event
        emit(?C...SIGNAL('doubleClick'))

    ___ enterEvent , event
        isHightlight = T..
        repaint()

    ___ leaveEvent , event
        isHightlight = False
        repaint()

    # 设定当前为选中状态
    ___ setSelected 
        # 取消其他缩略图的选择状态, 当前设为选择状态
        __ ImageWidget.prevSelected != None:
            ImageWidget.prevSelected.selected = False
            ImageWidget.prevSelected.repaint()
        selected = T..
        repaint()
        ImageWidget.prevSelected = self

        onWidgetClicked()
        emit(?C...SIGNAL("click"), id)

    ___ onWidgetClicked 
        print 'on widget clicked'


c_ ImageContainer(QtGui.QFrame
    ___  -  , widgets=None
        super(ImageContainer, self). - ()

        containerLayout = QtGui.QVBoxLayout()

        # 初始化Slider
        zoomSlider = QtGui.QSlider()
        zoomSlider.setOrientation(?C...Qt.Horizontal)
        zoomSlider.setMinimum(THUMB_MIN)
        zoomSlider.setMaximum(THUMB_MAX)
        zoomSlider.setValue(THUMB_WIDTH)
        zoomSlider.setFixedWidth(128)
        zoomSlider.setFixedHeight(10)

        # Slider设定
        ?C...QObject.c..(zoomSlider, ?C...SIGNAL('valueChanged(int)'), setItemSize)

        item_scrollarea = QtGui.QScrollArea()
        item_area = QtGui.?W..()
        item_scrollarea.setWidget(item_area)

        containerLayout.addWidget(zoomSlider)
        containerLayout.addWidget(item_scrollarea)

        widget_w = THUMB_WIDTH
        widget_h = THUMB_HEIGHT
        min_width = THUMB_MIN
        max_height = THUMB_MAX
        asset_space = 2
        auto_space = False

        setWindowOpacity(0.0)

        setLayout(containerLayout)

        # 缩略图对象列表
        ImageWidgetList = {}

    ___ addWidget , widget
        widget.setParent(item_area)
        widget.resize(widget_w, widget_h)
        widget.s..
        # 添加到列表
        ImageWidgetList[st.(widget.id)] = widget

    ___ addWidgets , widgets
        for widget in widgets:
            addWidget(widget)
        layout()

    ___ clearAll 
        widgets = item_area.children()
        __ widgets:
            for widget in widgets:
                widget.setParent(None)

        ImageWidgetList.clear()

    ___ layout 
        w = width() - 20
        widgets = item_area.children()

        num_x = max(math.ceil(w / (widget_w + asset_space)), 1)  # Can do -1
        num_y = math.ceil(len(widgets) / num_x)
        item_area.resize(w, num_y * (widget_h + asset_space) + 50)

        main_w = item_area.width()
        main_h = item_area.height()
        num_x = max(math.ceil(main_w / (widget_w + asset_space)), 1)  # Can do -1

        x = 0
        y = 0
        for i in range(len(widgets)):
            space_x = 0
            __ auto_space:
                space_x = (main_w - asset_space * 2 - num_x * (widget_w + asset_space)) / num_x
            widgets[i].move(asset_space * 2 + x * (widget_w + asset_space + space_x), \
                            asset_space * 2 + y * (widget_h + asset_space))
            x += 1
            __ x >= num_x:
                x = 0
                y += 1

    ___ resizeEvent , event
        layout()

    ___ changeItemSize , mount
        widgets = item_area.children()
        widget_w += mount
        __ widget_w > max_height:
            widget_w = max_height
        elif widget_w < min_width:
            widget_w = min_width

        widget_h += mount
        __ widget_h > max_height:
            widget_h = max_height
        elif widget_h < min_width:
            widget_h = min_width

        for a in widgets:
            a.resize(widget_w, widget_h)

        layout()

    ___ setItemSize , size
        widgets = item_area.children()

        widget_w = size
        widget_h = size

        for a in widgets:
            a.resize(size, size)

        layout()

    # 设定指定id为选中状态
    ___ setSelected , id
        print 'ImageContainer -> setSelected    ', id
        ImageWidgetList[st.(id)].setSelected()


c_ MainWindow(QtGui.?W..
    ___  -  
        app = QtGui.?A..(___.argv)
        super(MainWindow, self). - ()

        setWindowTitle("Image Viewer")
        resize(1280, 800)

        # 屏幕居中
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = geometry()
        move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

        s..

        mainSpliter = QtGui.QSplitter(?C...Qt.Horizontal)

        # 文件夹列表model
        dirModel = QtGui.QDirModel

        # 只显示文件夹
        dirModel.setFilter(?C...QDir.Dirs | ?C...QDir.NoDotAndDotDot)

        # 文件夹列表view
        dirTreeView = QtGui.QTreeView()

        # 绑定model
        dirTreeView.setModel(dirModel)

        dirTreeView.hideColumn(1)
        dirTreeView.hideColumn(2)
        dirTreeView.hideColumn(3)

        # DirTree事件响应
        dirTreeView.selectionModel().selectionChanged.c..(dirTreeClicked)

        mainLayout = QtGui.QVBoxLayout()
        mainSpliter.addWidget(dirTreeView)

        imageContainer = ImageContainer(mainSpliter)
        #        self.imageContainer.setGeometry(self.imageContainer.geometry().x(), self.imageContainer.geometry().y(), 100, self.imageContainer.geometry().height())
        imageContainer.setMinimumWidth(geometry().width() * 0.7)
        mainSpliter.addWidget(imageContainer)

        mainLayout.addWidget(mainSpliter)

        setLayout(mainLayout)

        ___.e..(app.exec_())

    ___ dirTreeClicked 
        print 'dirTreeClicked'

        imageContainer.clearAll()

        # 获取选择的路径
        pathSelected = dirModel.filePath(dirTreeView.selectedIndexes()[0])
        print 'pathSelected   ', pathSelected
        # 遍历路径下的媒体文件
        for item in os.listdir(pathSelected
            __ item.split('.')[-1] in FILE_TYPE:
                print item
                # 添加widget
                try:
                    widget = ImageWidget()
                    widget.displayText = item
                    widget.setThumb(unicode(pathSelected + '/' + item))
                    imageContainer.addWidget(widget)
                except:
                    pass


# self.imageContainer.layout()

___ main(
    MainWindow()


__ __name__ __ '__main__':
    main()