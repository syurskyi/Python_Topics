# -*- coding: utf-8 -*-
# ! /usr/bin/env python

_____ ___
____ PyQt4 _____ ?G.., ?C..

_____ os, string
_____ math

THUMB_WIDTH _ 128
THUMB_HEIGHT _ 128
THUMB_MIN _ 64
THUMB_MAX _ 256
FILE_TYPE _ ['jpg', 'jpeg', 'tif', 'bmp', 'gif']


c_ ImageWidget(?G...?W..

    prevSelected _ None

    """
    Use this widget to display image.
    """

    ___  -  
        super(ImageWidget, self). - 
        id _ 0
        displayText _ ''
        version _ ''
        status _ 0
        path _ ''
        showStatus _ T..
        selected _ F..
        isHightlight _ F..
        thumb _ ?G...QImage
        initAttrib

    ___ initAttrib 
        name_font _ ?G...?F..
        bg_color _ ?G...?C..(50, 50, 50)
        hightlight _ ?G...?C..(255, 255, 255, 100)
        edge_size _ 5
        pen_selected _ ?G...?P..(?G...?C..(255, 255, 0))
        pen_selected.setWidth(edge_size)
        pen_selected.setJoinStyle(?C...__.MiterJoin)

    #        self.setToolTip('aaaa\nbbbb\ncccc')

    ___ assetFile 
        r_ path + "_asset_.txt"

    ___ thumbFile 
        r_ path + "_thumb_.png"

    ___ informationFile 
        r_ path + "_information_.txt"

    ___ getPublishPath 
        current_version _ version
        __ not current_version:
            current_version _ '000'
        new_version _ int(string.atof(current_version)) + 1
        r_ '%s/%03d' % (path, new_version)

    ___ getVersionPath , version
        r_ '%s/%s' % (path, version)

    ___ getCurrentVersionPath 
        r_ getVersionPath(version)

    ___ setThumb , thumb_None
        __ not thumb:
            thumb _ thumbFile
        __ os.path.isfile(thumb
            thumb.l..(?C...QString(thumb))
            repaint
            r_ T..

    ___ paintAsThumb , painter
        name_height _ max(height * 0.15, 20)
        name_ty _ height - edge_size * 2
        # draw background
        painter.fillRect(rect, bg_color)
        painter.drawImage(rect, thumb)
        # draw hightlight
        __ isHightlight an. not selected:
            painter.fillRect(rect, hightlight)
        # draw name
        painter.setPen(?G...?P..(?G...?C..(255, 255, 255)))
        name_font.setPixelSize(name_height)
        painter.sF..(name_font)
        # 脚标字符
        painter.drawText(edge_size, name_ty, st.(displayText))

        __ status:
            title_height _ edge_size + name_height
            p1 _ ?C...QPoint(0, 0)
            p2 _ ?C...QPoint(0, title_height)
            p3 _ ?C...QPoint(title_height, 0)
            painter.setPen(?C...__.NoPen)
            painter.fillRect(0, 0, width, title_height, ?G...?C..(40, 40, 40, 40))
            __ status __ 1:
                painter.setBrush(?G...QBrush(?G...?C..(255, 0, 0)))
            ____ status __ 2:
                painter.setBrush(?G...QBrush(?G...?C..(0, 255, 0)))
            ____ status __ 3:
                painter.setBrush(?G...QBrush(?G...?C..(0, 0, 255)))
            painter.drawConvexPolygon(p1, p2, p3)

        __ version:
            version_x _ width - edge_size - name_height * 1.5
            version_y _ name_height
            painter.setPen(?G...?P..(?G...?C..(255, 255, 255)))
            painter.drawText(version_x, version_y, '%s' % version)

        # draw selected
        __ selected:
            painter.setPen(pen_selected)
            painter.setBrush(?C...__.NoBrush)
            painter.drawRect(edge_size / 2, edge_size / 2, \
                             width - edge_size, height - edge_size)

    ___ paintEvent , event
        painter _ ?G...?P..
        paintAsThumb(painter)

    ___ mouseReleaseEvent , event
        __ event.button __ ?C...__.LeftButton:
            setSelected

    ___ mouseDoubleClickEvent , event
        emit(?C...SIGNAL('doubleClick'))

    ___ enterEvent , event
        isHightlight _ T..
        repaint

    ___ leaveEvent , event
        isHightlight _ F..
        repaint

    # 设定当前为选中状态
    ___ setSelected 
        # 取消其他缩略图的选择状态, 当前设为选择状态
        __ ImageWidget.prevSelected !_ None:
            ImageWidget.prevSelected.selected _ F..
            ImageWidget.prevSelected.repaint
        selected _ T..
        repaint
        ImageWidget.prevSelected _ self

        onWidgetClicked
        emit(?C...SIGNAL("click"), id)

    ___ onWidgetClicked 
        print 'on widget clicked'


c_ ImageContainer(?G...QFrame
    ___  -  , widgets_None
        super(ImageContainer, self). - 

        containerLayout _ ?G...QVBoxLayout

        # 初始化Slider
        zoomSlider _ ?G...QSlider
        zoomSlider.setOrientation(?C...__.Horizontal)
        zoomSlider.setMinimum(THUMB_MIN)
        zoomSlider.setMaximum(THUMB_MAX)
        zoomSlider.sV..(THUMB_WIDTH)
        zoomSlider.setFixedWidth(128)
        zoomSlider.setFixedHeight(10)

        # Slider设定
        ?C...QObject.c..(zoomSlider, ?C...SIGNAL('valueChanged(int)'), setItemSize)

        item_scrollarea _ ?G...QScrollArea
        item_area _ ?G...?W..
        item_scrollarea.setWidget(item_area)

        containerLayout.addWidget(zoomSlider)
        containerLayout.addWidget(item_scrollarea)

        widget_w _ THUMB_WIDTH
        widget_h _ THUMB_HEIGHT
        min_width _ THUMB_MIN
        max_height _ THUMB_MAX
        asset_space _ 2
        auto_space _ F..

        setWindowOpacity(0.0)

        setLayout(containerLayout)

        # 缩略图对象列表
        ImageWidgetList _ {}

    ___ addWidget , widget
        widget.setParent(item_area)
        widget.resize(widget_w, widget_h)
        widget.s..
        # 添加到列表
        ImageWidgetList[st.(widget.id)] _ widget

    ___ addWidgets , widgets
        ___ widget __ widgets:
            addWidget(widget)
        layout

    ___ clearAll 
        widgets _ item_area.children
        __ widgets:
            ___ widget __ widgets:
                widget.setParent(None)

        ImageWidgetList.c..

    ___ layout 
        w _ width - 20
        widgets _ item_area.children

        num_x _ max(math.ceil(w / (widget_w + asset_space)), 1)  # Can do -1
        num_y _ math.ceil(le.(widgets) / num_x)
        item_area.resize(w, num_y * (widget_h + asset_space) + 50)

        main_w _ item_area.width
        main_h _ item_area.height
        num_x _ max(math.ceil(main_w / (widget_w + asset_space)), 1)  # Can do -1

        x _ 0
        y _ 0
        ___ i __ range(le.(widgets)):
            space_x _ 0
            __ auto_space:
                space_x _ (main_w - asset_space * 2 - num_x * (widget_w + asset_space)) / num_x
            widgets[i].move(asset_space * 2 + x * (widget_w + asset_space + space_x), \
                            asset_space * 2 + y * (widget_h + asset_space))
            x +_ 1
            __ x >_ num_x:
                x _ 0
                y +_ 1

    ___ resizeEvent , event
        layout

    ___ changeItemSize , mount
        widgets _ item_area.children
        widget_w +_ mount
        __ widget_w > max_height:
            widget_w _ max_height
        ____ widget_w < min_width:
            widget_w _ min_width

        widget_h +_ mount
        __ widget_h > max_height:
            widget_h _ max_height
        ____ widget_h < min_width:
            widget_h _ min_width

        ___ a __ widgets:
            a.resize(widget_w, widget_h)

        layout

    ___ setItemSize , size
        widgets _ item_area.children

        widget_w _ size
        widget_h _ size

        ___ a __ widgets:
            a.resize(size, size)

        layout

    # 设定指定id为选中状态
    ___ setSelected , id
        print 'ImageContainer -> setSelected    ', id
        ImageWidgetList[st.(id)].setSelected


c_ MainWindow(?G...?W..
    ___  -  
        app _ ?G...?A..
        super(MainWindow, self). - 

        setWindowTitle("Image Viewer")
        resize(1280, 800)

        # 屏幕居中
        screen _ ?G...QDesktopWidget.screenGeometry
        size _ geometry
        move((screen.width - size.width()) / 2, (screen.height - size.height()) / 2)

        s..

        mainSpliter _ ?G...QSplitter(?C...__.Horizontal)

        # 文件夹列表model
        dirModel _ ?G...QDirModel

        # 只显示文件夹
        dirModel.setFilter(?C...QDir.Dirs | ?C...QDir.NoDotAndDotDot)

        # 文件夹列表view
        dirTreeView _ ?G...QTreeView

        # 绑定model
        dirTreeView.setModel(dirModel)

        dirTreeView.hideColumn(1)
        dirTreeView.hideColumn(2)
        dirTreeView.hideColumn(3)

        # DirTree事件响应
        dirTreeView.selectionModel.sC__.c..(dirTreeClicked)

        mainLayout _ ?G...QVBoxLayout
        mainSpliter.addWidget(dirTreeView)

        imageContainer _ ImageContainer(mainSpliter)
        #        self.imageContainer.setGeometry(self.imageContainer.geometry().x(), self.imageContainer.geometry().y(), 100, self.imageContainer.geometry().height())
        imageContainer.setMinimumWidth(geometry.width * 0.7)
        mainSpliter.addWidget(imageContainer)

        mainLayout.addWidget(mainSpliter)

        setLayout(mainLayout)

        ___.e.. ?.e

    ___ dirTreeClicked 
        print 'dirTreeClicked'

        imageContainer.clearAll

        # 获取选择的路径
        pathSelected _ dirModel.filePath(dirTreeView.selectedIndexes[0])
        print 'pathSelected   ', pathSelected
        # 遍历路径下的媒体文件
        ___ item __ os.listdir(pathSelected
            __ item.split('.')[-1] __ FILE_TYPE:
                print item
                # 添加widget
                ___
                    widget _ ImageWidget
                    widget.displayText _ item
                    widget.setThumb(unicode(pathSelected + '/' + item))
                    imageContainer.addWidget(widget)
                _____:
                    pass


# self.imageContainer.layout()

___ main(
    MainWindow


__ __name__ __ '__main__':
    main