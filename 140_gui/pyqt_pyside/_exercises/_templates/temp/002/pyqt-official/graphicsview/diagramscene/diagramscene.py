#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


______ math

____ ?.?C.. ______ (pyqtSignal, QLineF, QPointF, QRect, QRectF, QSize,
        QSizeF, __)
____ ?.?G.. ______ (QBrush, ?C.., QFont, QIcon, QIntValidator, QPainter,
        QPainterPath, QPen, QPixmap, QPolygonF)
____ ?.?W.. ______ (?A.., ?A.., QButtonGroup, QComboBox,
        QFontComboBox, QGraphicsItem, QGraphicsLineItem, QGraphicsPolygonItem,
        QGraphicsScene, QGraphicsTextItem, QGraphicsView, QGridLayout,
        QHBoxLayout, QLabel, QMainWindow, QMenu, ?MB.., QSizePolicy,
        QToolBox, QToolButton, QWidget)

______ diagramscene_rc


c_ Arrow(QGraphicsLineItem):
    ___  -   startItem, endItem, parent_None, scene_None):
        super(Arrow, self). - (parent, scene)

        arrowHead _ QPolygonF()

        myStartItem _ startItem
        myEndItem _ endItem
        setFlag(QGraphicsItem.ItemIsSelectable, True)
        myColor _ __.black
        setPen(QPen(myColor, 2, __.SolidLine, __.RoundCap,
                __.RoundJoin))

    ___ sC..  color):
        myColor _ color

    ___ startItem
        r_ myStartItem

    ___ endItem
        r_ myEndItem

    ___ boundingRect
        extra _ (pen().width() + 20) / 2.0
        p1 _ line().p1()
        p2 _ line().p2()
        r_ QRectF(p1, QSizeF(p2.x() - p1.x(), p2.y() - p1.y())).normalized().adjusted(-extra, -extra, extra, extra)

    ___ shape
        path _ super(Arrow, self).shape()
        path.addPolygon(arrowHead)
        r_ path

    ___ updatePosition
        line _ QLineF(mapFromItem(myStartItem, 0, 0), mapFromItem(myEndItem, 0, 0))
        setLine(line)

    ___ paint  painter, option, widget_None):
        __ (myStartItem.collidesWithItem(myEndItem)):
            r_

        myStartItem _ myStartItem
        myEndItem _ myEndItem
        myColor _ myColor
        myPen _ pen()
        myPen.sC..(myColor)
        arrowSize _ 20.0
        painter.setPen(myPen)
        painter.setBrush(myColor)

        centerLine _ QLineF(myStartItem.pos(), myEndItem.pos())
        endPolygon _ myEndItem.polygon()
        p1 _ endPolygon.first() + myEndItem.pos()

        intersectPoint _ QPointF()
        ___ i __ endPolygon:
            p2 _ i + myEndItem.pos()
            polyLine _ QLineF(p1, p2)
            intersectType _ polyLine.intersect(centerLine, intersectPoint)
            __ intersectType == QLineF.BoundedIntersection:
                break
            p1 _ p2

        setLine(QLineF(intersectPoint, myStartItem.pos()))
        line _ line()

        angle _ math.acos(line.dx() / line.length())
        __ line.dy() >_ 0:
            angle _ (math.pi * 2.0) - angle

        arrowP1 _ line.p1() + QPointF(math.sin(angle + math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi / 3) * arrowSize)
        arrowP2 _ line.p1() + QPointF(math.sin(angle + math.pi - math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi - math.pi / 3.0) * arrowSize)

        arrowHead.clear()
        ___ point __ [line.p1(), arrowP1, arrowP2]:
            arrowHead.ap..(point)

        painter.drawLine(line)
        painter.drawPolygon(arrowHead)
        __ isSelected
            painter.setPen(QPen(myColor, 1, __.DashLine))
            myLine _ QLineF(line)
            myLine.translate(0, 4.0)
            painter.drawLine(myLine)
            myLine.translate(0,-8.0)
            painter.drawLine(myLine)


c_ DiagramTextItem(QGraphicsTextItem):
    lostFocus _ pyqtSignal(QGraphicsTextItem)

    selectedChange _ pyqtSignal(QGraphicsItem)

    ___  -   parent_None, scene_None):
        super(DiagramTextItem, self). - (parent, scene)

        setFlag(QGraphicsItem.ItemIsMovable)
        setFlag(QGraphicsItem.ItemIsSelectable)

    ___ itemChange  change, value):
        __ change == QGraphicsItem.ItemSelectedChange:
            selectedChange.emit
        r_ value

    ___ focusOutEvent  event):
        setTextInteractionFlags(__.NoTextInteraction)
        lostFocus.emit
        super(DiagramTextItem, self).focusOutEvent(event)

    ___ mouseDoubleClickEvent  event):
        __ textInteractionFlags() == __.NoTextInteraction:
            setTextInteractionFlags(__.TextEditorInteraction)
        super(DiagramTextItem, self).mouseDoubleClickEvent(event)


c_ DiagramItem(QGraphicsPolygonItem):
    Step, Conditional, StartEnd, Io _ range(4)

    ___  -   diagramType, contextMenu, parent_None):
        super(DiagramItem, self). - (parent)

        arrows _   # list

        diagramType _ diagramType
        contextMenu _ contextMenu

        path _ QPainterPath()
        __ diagramType == StartEnd:
            path.moveTo(200, 50)
            path.arcTo(150, 0, 50, 50, 0, 90)
            path.arcTo(50, 0, 50, 50, 90, 90)
            path.arcTo(50, 50, 50, 50, 180, 90)
            path.arcTo(150, 50, 50, 50, 270, 90)
            path.lineTo(200, 25)
            myPolygon _ path.toFillPolygon()
        ____ diagramType == Conditional:
            myPolygon _ QPolygonF([
                    QPointF(-100, 0), QPointF(0, 100),
                    QPointF(100, 0), QPointF(0, -100),
                    QPointF(-100, 0)])
        ____ diagramType == Step:
            myPolygon _ QPolygonF([
                    QPointF(-100, -100), QPointF(100, -100),
                    QPointF(100, 100), QPointF(-100, 100),
                    QPointF(-100, -100)])
        ____
            myPolygon _ QPolygonF([
                    QPointF(-120, -80), QPointF(-70, 80),
                    QPointF(120, 80), QPointF(70, -80),
                    QPointF(-120, -80)])

        setPolygon(myPolygon)
        setFlag(QGraphicsItem.ItemIsMovable, True)
        setFlag(QGraphicsItem.ItemIsSelectable, True)

    ___ removeArrow  arrow):
        try:
            arrows.remove(arrow)
        except ValueError:
            pass

    ___ removeArrows
        ___ arrow __ arrows[:]:
            arrow.startItem().removeArrow(arrow)
            arrow.endItem().removeArrow(arrow)
            scene().removeItem(arrow)

    ___ addArrow  arrow):
        arrows.ap..(arrow)

    ___ image
        pixmap _ QPixmap(250, 250)
        pixmap.fill(__.transparent)
        painter _ QPainter(pixmap)
        painter.setPen(QPen(__.black, 8))
        painter.translate(125, 125)
        painter.drawPolyline(myPolygon)
        r_ pixmap

    ___ contextMenuEvent  event):
        scene().clearSelection()
        setSelected(True)
        myContextMenu.exec_(event.screenPos())

    ___ itemChange  change, value):
        __ change == QGraphicsItem.ItemPositionChange:
            ___ arrow __ arrows:
                arrow.updatePosition()

        r_ value


c_ DiagramScene(QGraphicsScene):
    InsertItem, InsertLine, InsertText, MoveItem  _ range(4)

    itemInserted _ pyqtSignal(DiagramItem)

    textInserted _ pyqtSignal(QGraphicsTextItem)

    itemSelected _ pyqtSignal(QGraphicsItem)

    ___  -   itemMenu, parent_None):
        super(DiagramScene, self). - (parent)

        myItemMenu _ itemMenu
        myMode _ MoveItem
        myItemType _ DiagramItem.Step
        line _ N..
        textItem _ N..
        myItemColor _ __.white
        myTextColor _ __.black
        myLineColor _ __.black
        myFont _ QFont()

    ___ setLineColor  color):
        myLineColor _ color
        __ isItemChange(Arrow):
            item _ selectedItems()[0]
            item.sC..(myLineColor)
            update()

    ___ setTextColor  color):
        myTextColor _ color
        __ isItemChange(DiagramTextItem):
            item _ selectedItems()[0]
            item.setDefaultTextColor(myTextColor)

    ___ setItemColor  color):
        myItemColor _ color
        __ isItemChange(DiagramItem):
            item _ selectedItems()[0]
            item.setBrush(myItemColor)

    ___ setFont  font):
        myFont _ font
        __ isItemChange(DiagramTextItem):
            item _ selectedItems()[0]
            item.setFont(myFont)

    ___ setMode  mode):
        myMode _ mode

    ___ setItemType  type):
        myItemType _ type

    ___ editorLostFocus  item):
        cursor _ item.textCursor()
        cursor.clearSelection()
        item.setTextCursor(cursor)

        __ item.toPlainText
            removeItem(item)
            item.deleteLater()

    ___ mousePressEvent  mouseEvent):
        __ (mouseEvent.button() !_ __.LeftButton):
            r_

        __ myMode == InsertItem:
            item _ DiagramItem(myItemType, myItemMenu)
            item.setBrush(myItemColor)
            addItem(item)
            item.setPos(mouseEvent.scenePos())
            itemInserted.emit(item)
        ____ myMode == InsertLine:
            line _ QGraphicsLineItem(QLineF(mouseEvent.scenePos(),
                    mouseEvent.scenePos()))
            line.setPen(QPen(myLineColor, 2))
            addItem(line)
        ____ myMode == InsertText:
            textItem _ DiagramTextItem()
            textItem.setFont(myFont)
            textItem.setTextInteractionFlags(__.TextEditorInteraction)
            textItem.setZValue(1000.0)
            textItem.lostFocus.c..(editorLostFocus)
            textItem.selectedChange.c..(itemSelected)
            addItem(textItem)
            textItem.setDefaultTextColor(myTextColor)
            textItem.setPos(mouseEvent.scenePos())
            textInserted.emit(textItem)

        super(DiagramScene, self).mousePressEvent(mouseEvent)

    ___ mouseMoveEvent  mouseEvent):
        __ myMode == InsertLine and line:
            newLine _ QLineF(line.line().p1(), mouseEvent.scenePos())
            line.setLine(newLine)
        ____ myMode == MoveItem:
            super(DiagramScene, self).mouseMoveEvent(mouseEvent)

    ___ mouseReleaseEvent  mouseEvent):
        __ line and myMode == InsertLine:
            startItems _ items(line.line().p1())
            __ le.(startItems) and startItems[0] == line:
                startItems.p.. 0)
            endItems _ items(line.line().p2())
            __ le.(endItems) and endItems[0] == line:
                endItems.p.. 0)

            removeItem(line)
            line _ N..

            __ le.(startItems) and le.(endItems) and \
                    isinstance(startItems[0], DiagramItem) and \
                    isinstance(endItems[0], DiagramItem) and \
                    startItems[0] !_ endItems[0]:
                startItem _ startItems[0]
                endItem _ endItems[0]
                arrow _ Arrow(startItem, endItem)
                arrow.sC..(myLineColor)
                startItem.addArrow(arrow)
                endItem.addArrow(arrow)
                arrow.setZValue(-1000.0)
                addItem(arrow)
                arrow.updatePosition()

        line _ N..
        super(DiagramScene, self).mouseReleaseEvent(mouseEvent)

    ___ isItemChange  type):
        ___ item __ selectedItems
            __ isinstance(item, type):
                r_ True
        r_ False


c_ MainWindow ?MW..
    InsertTextButton _ 10

    ___  -
        super(MainWindow, self). - ()

        createActions()
        createMenus()
        createToolBox()

        scene _ DiagramScene(itemMenu)
        scene.setSceneRect(QRectF(0, 0, 5000, 5000))
        scene.itemInserted.c..(itemInserted)
        scene.textInserted.c..(textInserted)
        scene.itemSelected.c..(itemSelected)

        createToolbars()

        layout _ QHBoxLayout()
        layout.aW..(toolBox)
        view _ QGraphicsView(scene)
        layout.aW..(view)

        widget _ ?W..
        widget.sL..(layout)

        sCW..(widget)
        setWindowTitle("Diagramscene")

    ___ backgroundButtonGroupClicked  button):
        buttons _ backgroundButtonGroup.buttons()
        ___ myButton __ buttons:
            __ myButton !_ button:
                button.setChecked F..

        t__ _ button.t__()
        __ t__ == "Blue Grid":
            scene.setBackgroundBrush(QBrush(QPixmap(':/images/background1.png')))
        ____ t__ == "White Grid":
            scene.setBackgroundBrush(QBrush(QPixmap(':/images/background2.png')))
        ____ t__ == "Gray Grid":
            scene.setBackgroundBrush(QBrush(QPixmap(':/images/background3.png')))
        ____
            scene.setBackgroundBrush(QBrush(QPixmap(':/images/background4.png')))

        scene.update()
        view.update()

    ___ buttonGroupClicked  id):
        buttons _ buttonGroup.buttons()
        ___ button __ buttons:
            __ buttonGroup.button(id) !_ button:
                button.setChecked F..

        __ id == InsertTextButton:
            scene.setMode(DiagramScene.InsertText)
        ____
            scene.setItemType(id)
            scene.setMode(DiagramScene.InsertItem)

    ___ deleteItem
        ___ item __ scene.selectedItems
            __ isinstance(item, DiagramItem):
                item.removeArrows()
            scene.removeItem(item)

    ___ pointerGroupClicked  i):
        scene.setMode(pointerTypeGroup.checkedId())

    ___ bringToFront
        __ no. scene.selectedItems
            r_

        selectedItem _ scene.selectedItems()[0]
        overlapItems _ selectedItem.collidingItems()

        zValue _ 0
        ___ item __ overlapItems:
            __ (item.zValue() >_ zValue and isinstance(item, DiagramItem)):
                zValue _ item.zValue() + 0.1
        selectedItem.setZValue(zValue)

    ___ sendToBack
        __ no. scene.selectedItems
            r_

        selectedItem _ scene.selectedItems()[0]
        overlapItems _ selectedItem.collidingItems()

        zValue _ 0
        ___ item __ overlapItems:
            __ (item.zValue() <_ zValue and isinstance(item, DiagramItem)):
                zValue _ item.zValue() - 0.1
        selectedItem.setZValue(zValue)

    ___ itemInserted  item):
        pointerTypeGroup.button(DiagramScene.MoveItem).setChecked(True)
        scene.setMode(pointerTypeGroup.checkedId())
        buttonGroup.button(item.diagramType).setChecked F..

    ___ textInserted  item):
        buttonGroup.button(InsertTextButton).setChecked F..
        scene.setMode(pointerTypeGroup.checkedId())

    ___ currentFontChanged  font):
        handleFontChange()

    ___ fontSizeChanged  font):
        handleFontChange()

    ___ sceneScaleChanged  scale):
        newScale _ scale.left(scale.indexOf("%")).toDouble()[0] / 100.0
        oldMatrix _ view.matrix()
        view.resetMatrix()
        view.translate(oldMatrix.dx(), oldMatrix.dy())
        view.scale(newScale, newScale)

    ___ textColorChanged
        textAction _ sender()
        fontColorToolButton.setIcon(
                createColorToolButtonIcon(':/images/textpointer.png',
                        ?C..(textAction.data())))
        textButtonTriggered()

    ___ itemColorChanged
        fillAction _ sender()
        fillColorToolButton.setIcon(
                createColorToolButtonIcon( ':/images/floodfill.png',
                        ?C..(fillAction.data())))
        fillButtonTriggered()

    ___ lineColorChanged
        lineAction _ sender()
        lineColorToolButton.setIcon(
                createColorToolButtonIcon(':/images/linecolor.png',
                        ?C..(lineAction.data())))
        lineButtonTriggered()

    ___ textButtonTriggered
        scene.setTextColor(?C..(textAction.data()))

    ___ fillButtonTriggered
        scene.setItemColor(?C..(fillAction.data()))

    ___ lineButtonTriggered
        scene.setLineColor(?C..(lineAction.data()))

    ___ handleFontChange
        font _ fontCombo.currentFont()
        font.setPointSize(fontSizeCombo.currentText().toInt()[0])
        __ boldAction.isChecked
            font.setWeight(QFont.Bold)
        ____
            font.setWeight(QFont.Normal)
        font.setItalic(italicAction.isChecked())
        font.setUnderline(underlineAction.isChecked())

        scene.setFont(font)

    ___ itemSelected  item):
        font _ item.font()
        color _ item.defaultTextColor()
        fontCombo.setCurrentFont(font)
        fontSizeCombo.setEditText(str(font.pointSize()))
        boldAction.setChecked(font.weight() == QFont.Bold)
        italicAction.setChecked(font.italic())
        underlineAction.setChecked(font.underline())

    ___ about
        ?MB...about  "About Diagram Scene",
                "The <b>Diagram Scene</b> example shows use of the graphics framework.")

    ___ createToolBox
        buttonGroup _ QButtonGroup()
        buttonGroup.setExclusive F..
        buttonGroup.buttonClicked[int].c..(buttonGroupClicked)

        layout _ QGridLayout()
        layout.aW..(createCellWidget("Conditional", DiagramItem.Conditional),
                0, 0)
        layout.aW..(createCellWidget("Process", DiagramItem.Step), 0,
                1)
        layout.aW..(createCellWidget("Input/Output", DiagramItem.Io),
                1, 0)

        textButton _ QToolButton()
        textButton.setCheckable(True)
        buttonGroup.addButton(textButton, InsertTextButton)
        textButton.setIcon(QIcon(QPixmap(':/images/textpointer.png').scaled(30, 30)))
        textButton.setIconSize(QSize(50, 50))

        textLayout _ QGridLayout()
        textLayout.aW..(textButton, 0, 0, __.AlignHCenter)
        textLayout.aW..(QLabel("Text"), 1, 0, __.AlignCenter)
        textWidget _ ?W..
        textWidget.sL..(textLayout)
        layout.aW..(textWidget, 1, 1)

        layout.setRowStretch(3, 10)
        layout.setColumnStretch(2, 10)

        itemWidget _ ?W..
        itemWidget.sL..(layout)

        backgroundButtonGroup _ QButtonGroup()
        backgroundButtonGroup.buttonClicked.c..(backgroundButtonGroupClicked)

        backgroundLayout _ QGridLayout()
        backgroundLayout.aW..(createBackgroundCellWidget("Blue Grid",
                ':/images/background1.png'), 0, 0)
        backgroundLayout.aW..(createBackgroundCellWidget("White Grid",
                ':/images/background2.png'), 0, 1)
        backgroundLayout.aW..(createBackgroundCellWidget("Gray Grid",
                ':/images/background3.png'), 1, 0)
        backgroundLayout.aW..(createBackgroundCellWidget("No Grid",
                ':/images/background4.png'), 1, 1)

        backgroundLayout.setRowStretch(2, 10)
        backgroundLayout.setColumnStretch(2, 10)

        backgroundWidget _ ?W..
        backgroundWidget.sL..(backgroundLayout)

        toolBox _ QToolBox()
        toolBox.sSP..(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored))
        toolBox.setMinimumWidth(itemWidget.sizeHint().width())
        toolBox.addItem(itemWidget, "Basic Flowchart Shapes")
        toolBox.addItem(backgroundWidget, "Backgrounds")

    ___ createActions
        toFrontAction _ ?A..(
                QIcon(':/images/bringtofront.png'), "Bring to &Front",
                self, shortcut_"Ctrl+F", statusTip_"Bring item to front",
                triggered_self.bringToFront)

        sendBackAction _ ?A..(
                QIcon(':/images/sendtoback.png'), "Send to &Back", self,
                shortcut_"Ctrl+B", statusTip_"Send item to back",
                triggered_self.sendToBack)

        deleteAction _ ?A..(QIcon(':/images/delete.png'),
                "&Delete", self, shortcut_"Delete",
                statusTip_"Delete item from diagram",
                triggered_self.deleteItem)

        exitAction _ ?A..("E&xit", self, shortcut_"Ctrl+X",
                statusTip_"Quit Scenediagram example", triggered_self.close)

        boldAction _ ?A..(QIcon(':/images/bold.png'),
                "Bold", self, checkable_True, shortcut_"Ctrl+B",
                triggered_self.handleFontChange)

        italicAction _ ?A..(QIcon(':/images/italic.png'),
                "Italic", self, checkable_True, shortcut_"Ctrl+I",
                triggered_self.handleFontChange)

        underlineAction _ ?A..(
                QIcon(':/images/underline.png'), "Underline", self,
                checkable_True, shortcut_"Ctrl+U",
                triggered_self.handleFontChange)

        aboutAction _ ?A..("A&bout", self, shortcut_"Ctrl+B",
                triggered_self.about)

    ___ createMenus
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(exitAction)

        itemMenu _ mB.. .aM..("&Item")
        itemMenu.aA..(deleteAction)
        itemMenu.addSeparator()
        itemMenu.aA..(toFrontAction)
        itemMenu.aA..(sendBackAction)

        aboutMenu _ mB.. .aM..("&Help")
        aboutMenu.aA..(aboutAction)

    ___ createToolbars
        editToolBar _ addToolBar("Edit")
        editToolBar.aA..(deleteAction)
        editToolBar.aA..(toFrontAction)
        editToolBar.aA..(sendBackAction)

        fontCombo _ QFontComboBox()
        fontCombo.currentFontChanged.c..(currentFontChanged)

        fontSizeCombo _ QComboBox()
        fontSizeCombo.setEditable(True)
        ___ i __ range(8, 30, 2):
            fontSizeCombo.addItem(str(i))
        validator _ QIntValidator(2, 64, self)
        fontSizeCombo.setValidator(validator)
        fontSizeCombo.currentIndexChanged.c..(fontSizeChanged)

        fontColorToolButton _ QToolButton()
        fontColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        fontColorToolButton.setMenu(
                createColorMenu(textColorChanged, __.black))
        textAction _ fontColorToolButton.menu().defaultAction()
        fontColorToolButton.setIcon(
                createColorToolButtonIcon(':/images/textpointer.png',
                        __.black))
        fontColorToolButton.setAutoFillBackground(True)
        fontColorToolButton.c__.c..(textButtonTriggered)

        fillColorToolButton _ QToolButton()
        fillColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        fillColorToolButton.setMenu(
                createColorMenu(itemColorChanged, __.white))
        fillAction _ fillColorToolButton.menu().defaultAction()
        fillColorToolButton.setIcon(
                createColorToolButtonIcon(':/images/floodfill.png',
                        __.white))
        fillColorToolButton.c__.c..(fillButtonTriggered)

        lineColorToolButton _ QToolButton()
        lineColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        lineColorToolButton.setMenu(
                createColorMenu(lineColorChanged, __.black))
        lineAction _ lineColorToolButton.menu().defaultAction()
        lineColorToolButton.setIcon(
                createColorToolButtonIcon(':/images/linecolor.png',
                        __.black))
        lineColorToolButton.c__.c..(lineButtonTriggered)

        textToolBar _ addToolBar("Font")
        textToolBar.aW..(fontCombo)
        textToolBar.aW..(fontSizeCombo)
        textToolBar.aA..(boldAction)
        textToolBar.aA..(italicAction)
        textToolBar.aA..(underlineAction)

        colorToolBar _ addToolBar("Color")
        colorToolBar.aW..(fontColorToolButton)
        colorToolBar.aW..(fillColorToolButton)
        colorToolBar.aW..(lineColorToolButton)

        pointerButton _ QToolButton()
        pointerButton.setCheckable(True)
        pointerButton.setChecked(True)
        pointerButton.setIcon(QIcon(':/images/pointer.png'))
        linePointerButton _ QToolButton()
        linePointerButton.setCheckable(True)
        linePointerButton.setIcon(QIcon(':/images/linepointer.png'))

        pointerTypeGroup _ QButtonGroup()
        pointerTypeGroup.addButton(pointerButton, DiagramScene.MoveItem)
        pointerTypeGroup.addButton(linePointerButton,
                DiagramScene.InsertLine)
        pointerTypeGroup.buttonClicked[int].c..(pointerGroupClicked)

        sceneScaleCombo _ QComboBox()
        sceneScaleCombo.addItems(["50%", "75%", "100%", "125%", "150%"])
        sceneScaleCombo.setCurrentIndex(2)
        sceneScaleCombo.currentIndexChanged[str].c..(sceneScaleChanged)

        pointerToolbar _ addToolBar("Pointer type")
        pointerToolbar.aW..(pointerButton)
        pointerToolbar.aW..(linePointerButton)
        pointerToolbar.aW..(sceneScaleCombo)

    ___ createBackgroundCellWidget  t__, image):
        button _ QToolButton()
        button.sT..(t__)
        button.setIcon(QIcon(image))
        button.setIconSize(QSize(50, 50))
        button.setCheckable(True)
        backgroundButtonGroup.addButton(button)

        layout _ QGridLayout()
        layout.aW..(button, 0, 0, __.AlignHCenter)
        layout.aW..(QLabel(t__), 1, 0, __.AlignCenter)

        widget _ ?W..
        widget.sL..(layout)

        r_ widget

    ___ createCellWidget  t__, diagramType):
        item _ DiagramItem(diagramType, itemMenu)
        icon _ QIcon(item.image())

        button _ QToolButton()
        button.setIcon(icon)
        button.setIconSize(QSize(50, 50))
        button.setCheckable(True)
        buttonGroup.addButton(button, diagramType)

        layout _ QGridLayout()
        layout.aW..(button, 0, 0, __.AlignHCenter)
        layout.aW..(QLabel(t__), 1, 0, __.AlignCenter)

        widget _ ?W..
        widget.sL..(layout)

        r_ widget

    ___ createColorMenu  slot, defaultColor):
        colors _ [__.black, __.white, __.red, __.blue, __.yellow]
        names _ ["black", "white", "red", "blue", "yellow"]

        colorMenu _ QMenu
        ___ color, name __ zip(colors, names):
            action _ ?A..(createColorIcon(color), name, self,
                    triggered_slot)
            action.setData(?C..(color))
            colorMenu.aA..(action)
            __ color == defaultColor:
                colorMenu.setDefaultAction(action)
        r_ colorMenu

    ___ createColorToolButtonIcon  imageFile, color):
        pixmap _ QPixmap(50, 80)
        pixmap.fill(__.transparent)
        painter _ QPainter(pixmap)
        image _ QPixmap(imageFile)
        target _ QRect(0, 0, 50, 60)
        source _ QRect(0, 0, 42, 42)
        painter.fillRect(QRect(0, 60, 50, 80), color)
        painter.drawPixmap(target, image, source)
        painter.end()

        r_ QIcon(pixmap)

    ___ createColorIcon  color):
        pixmap _ QPixmap(20, 20)
        painter _ QPainter(pixmap)
        painter.setPen(__.NoPen)
        painter.fillRect(QRect(0, 0, 20, 20), color)
        painter.end()

        r_ QIcon(pixmap)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    mainWindow _ MainWindow()
    mainWindow.setGeometry(100, 100, 800, 500)
    mainWindow.s..

    ___.exit(app.exec_())
