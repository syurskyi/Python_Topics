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
    ___ __init__  startItem, endItem, parent_None, scene_None):
        super(Arrow, self).__init__(parent, scene)

        self.arrowHead _ QPolygonF()

        self.myStartItem _ startItem
        self.myEndItem _ endItem
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.myColor _ __.black
        self.setPen(QPen(self.myColor, 2, __.SolidLine, __.RoundCap,
                __.RoundJoin))

    ___ sC..  color):
        self.myColor _ color

    ___ startItem(self):
        r_ self.myStartItem

    ___ endItem(self):
        r_ self.myEndItem

    ___ boundingRect(self):
        extra _ (self.pen().width() + 20) / 2.0
        p1 _ self.line().p1()
        p2 _ self.line().p2()
        r_ QRectF(p1, QSizeF(p2.x() - p1.x(), p2.y() - p1.y())).normalized().adjusted(-extra, -extra, extra, extra)

    ___ shape(self):
        path _ super(Arrow, self).shape()
        path.addPolygon(self.arrowHead)
        r_ path

    ___ updatePosition(self):
        line _ QLineF(self.mapFromItem(self.myStartItem, 0, 0), self.mapFromItem(self.myEndItem, 0, 0))
        self.setLine(line)

    ___ paint  painter, option, widget_None):
        __ (self.myStartItem.collidesWithItem(self.myEndItem)):
            r_

        myStartItem _ self.myStartItem
        myEndItem _ self.myEndItem
        myColor _ self.myColor
        myPen _ self.pen()
        myPen.sC..(self.myColor)
        arrowSize _ 20.0
        painter.setPen(myPen)
        painter.setBrush(self.myColor)

        centerLine _ QLineF(myStartItem.pos(), myEndItem.pos())
        endPolygon _ myEndItem.polygon()
        p1 _ endPolygon.first() + myEndItem.pos()

        intersectPoint _ QPointF()
        for i in endPolygon:
            p2 _ i + myEndItem.pos()
            polyLine _ QLineF(p1, p2)
            intersectType _ polyLine.intersect(centerLine, intersectPoint)
            __ intersectType == QLineF.BoundedIntersection:
                break
            p1 _ p2

        self.setLine(QLineF(intersectPoint, myStartItem.pos()))
        line _ self.line()

        angle _ math.acos(line.dx() / line.length())
        __ line.dy() >_ 0:
            angle _ (math.pi * 2.0) - angle

        arrowP1 _ line.p1() + QPointF(math.sin(angle + math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi / 3) * arrowSize)
        arrowP2 _ line.p1() + QPointF(math.sin(angle + math.pi - math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi - math.pi / 3.0) * arrowSize)

        self.arrowHead.clear()
        for point in [line.p1(), arrowP1, arrowP2]:
            self.arrowHead.ap..(point)

        painter.drawLine(line)
        painter.drawPolygon(self.arrowHead)
        __ self.isSelected
            painter.setPen(QPen(myColor, 1, __.DashLine))
            myLine _ QLineF(line)
            myLine.translate(0, 4.0)
            painter.drawLine(myLine)
            myLine.translate(0,-8.0)
            painter.drawLine(myLine)


c_ DiagramTextItem(QGraphicsTextItem):
    lostFocus _ pyqtSignal(QGraphicsTextItem)

    selectedChange _ pyqtSignal(QGraphicsItem)

    ___ __init__  parent_None, scene_None):
        super(DiagramTextItem, self).__init__(parent, scene)

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    ___ itemChange  change, value):
        __ change == QGraphicsItem.ItemSelectedChange:
            self.selectedChange.emit(self)
        r_ value

    ___ focusOutEvent  event):
        self.setTextInteractionFlags(__.NoTextInteraction)
        self.lostFocus.emit(self)
        super(DiagramTextItem, self).focusOutEvent(event)

    ___ mouseDoubleClickEvent  event):
        __ self.textInteractionFlags() == __.NoTextInteraction:
            self.setTextInteractionFlags(__.TextEditorInteraction)
        super(DiagramTextItem, self).mouseDoubleClickEvent(event)


c_ DiagramItem(QGraphicsPolygonItem):
    Step, Conditional, StartEnd, Io _ range(4)

    ___ __init__  diagramType, contextMenu, parent_None):
        super(DiagramItem, self).__init__(parent)

        self.arrows _   # list

        self.diagramType _ diagramType
        self.contextMenu _ contextMenu

        path _ QPainterPath()
        __ self.diagramType == self.StartEnd:
            path.moveTo(200, 50)
            path.arcTo(150, 0, 50, 50, 0, 90)
            path.arcTo(50, 0, 50, 50, 90, 90)
            path.arcTo(50, 50, 50, 50, 180, 90)
            path.arcTo(150, 50, 50, 50, 270, 90)
            path.lineTo(200, 25)
            self.myPolygon _ path.toFillPolygon()
        ____ self.diagramType == self.Conditional:
            self.myPolygon _ QPolygonF([
                    QPointF(-100, 0), QPointF(0, 100),
                    QPointF(100, 0), QPointF(0, -100),
                    QPointF(-100, 0)])
        ____ self.diagramType == self.Step:
            self.myPolygon _ QPolygonF([
                    QPointF(-100, -100), QPointF(100, -100),
                    QPointF(100, 100), QPointF(-100, 100),
                    QPointF(-100, -100)])
        ____
            self.myPolygon _ QPolygonF([
                    QPointF(-120, -80), QPointF(-70, 80),
                    QPointF(120, 80), QPointF(70, -80),
                    QPointF(-120, -80)])

        self.setPolygon(self.myPolygon)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

    ___ removeArrow  arrow):
        try:
            self.arrows.remove(arrow)
        except ValueError:
            pass

    ___ removeArrows(self):
        for arrow in self.arrows[:]:
            arrow.startItem().removeArrow(arrow)
            arrow.endItem().removeArrow(arrow)
            self.scene().removeItem(arrow)

    ___ addArrow  arrow):
        self.arrows.ap..(arrow)

    ___ image(self):
        pixmap _ QPixmap(250, 250)
        pixmap.fill(__.transparent)
        painter _ QPainter(pixmap)
        painter.setPen(QPen(__.black, 8))
        painter.translate(125, 125)
        painter.drawPolyline(self.myPolygon)
        r_ pixmap

    ___ contextMenuEvent  event):
        self.scene().clearSelection()
        self.setSelected(True)
        self.myContextMenu.exec_(event.screenPos())

    ___ itemChange  change, value):
        __ change == QGraphicsItem.ItemPositionChange:
            for arrow in self.arrows:
                arrow.updatePosition()

        r_ value


c_ DiagramScene(QGraphicsScene):
    InsertItem, InsertLine, InsertText, MoveItem  _ range(4)

    itemInserted _ pyqtSignal(DiagramItem)

    textInserted _ pyqtSignal(QGraphicsTextItem)

    itemSelected _ pyqtSignal(QGraphicsItem)

    ___ __init__  itemMenu, parent_None):
        super(DiagramScene, self).__init__(parent)

        self.myItemMenu _ itemMenu
        self.myMode _ self.MoveItem
        self.myItemType _ DiagramItem.Step
        self.line _ N..
        self.textItem _ N..
        self.myItemColor _ __.white
        self.myTextColor _ __.black
        self.myLineColor _ __.black
        self.myFont _ QFont()

    ___ setLineColor  color):
        self.myLineColor _ color
        __ self.isItemChange(Arrow):
            item _ self.selectedItems()[0]
            item.sC..(self.myLineColor)
            self.update()

    ___ setTextColor  color):
        self.myTextColor _ color
        __ self.isItemChange(DiagramTextItem):
            item _ self.selectedItems()[0]
            item.setDefaultTextColor(self.myTextColor)

    ___ setItemColor  color):
        self.myItemColor _ color
        __ self.isItemChange(DiagramItem):
            item _ self.selectedItems()[0]
            item.setBrush(self.myItemColor)

    ___ setFont  font):
        self.myFont _ font
        __ self.isItemChange(DiagramTextItem):
            item _ self.selectedItems()[0]
            item.setFont(self.myFont)

    ___ setMode  mode):
        self.myMode _ mode

    ___ setItemType  type):
        self.myItemType _ type

    ___ editorLostFocus  item):
        cursor _ item.textCursor()
        cursor.clearSelection()
        item.setTextCursor(cursor)

        __ item.toPlainText
            self.removeItem(item)
            item.deleteLater()

    ___ mousePressEvent  mouseEvent):
        __ (mouseEvent.button() !_ __.LeftButton):
            r_

        __ self.myMode == self.InsertItem:
            item _ DiagramItem(self.myItemType, self.myItemMenu)
            item.setBrush(self.myItemColor)
            self.addItem(item)
            item.setPos(mouseEvent.scenePos())
            self.itemInserted.emit(item)
        ____ self.myMode == self.InsertLine:
            self.line _ QGraphicsLineItem(QLineF(mouseEvent.scenePos(),
                    mouseEvent.scenePos()))
            self.line.setPen(QPen(self.myLineColor, 2))
            self.addItem(self.line)
        ____ self.myMode == self.InsertText:
            textItem _ DiagramTextItem()
            textItem.setFont(self.myFont)
            textItem.setTextInteractionFlags(__.TextEditorInteraction)
            textItem.setZValue(1000.0)
            textItem.lostFocus.c..(self.editorLostFocus)
            textItem.selectedChange.c..(self.itemSelected)
            self.addItem(textItem)
            textItem.setDefaultTextColor(self.myTextColor)
            textItem.setPos(mouseEvent.scenePos())
            self.textInserted.emit(textItem)

        super(DiagramScene, self).mousePressEvent(mouseEvent)

    ___ mouseMoveEvent  mouseEvent):
        __ self.myMode == self.InsertLine and self.line:
            newLine _ QLineF(self.line.line().p1(), mouseEvent.scenePos())
            self.line.setLine(newLine)
        ____ self.myMode == self.MoveItem:
            super(DiagramScene, self).mouseMoveEvent(mouseEvent)

    ___ mouseReleaseEvent  mouseEvent):
        __ self.line and self.myMode == self.InsertLine:
            startItems _ self.items(self.line.line().p1())
            __ le.(startItems) and startItems[0] == self.line:
                startItems.p.. 0)
            endItems _ self.items(self.line.line().p2())
            __ le.(endItems) and endItems[0] == self.line:
                endItems.p.. 0)

            self.removeItem(self.line)
            self.line _ N..

            __ le.(startItems) and le.(endItems) and \
                    isinstance(startItems[0], DiagramItem) and \
                    isinstance(endItems[0], DiagramItem) and \
                    startItems[0] !_ endItems[0]:
                startItem _ startItems[0]
                endItem _ endItems[0]
                arrow _ Arrow(startItem, endItem)
                arrow.sC..(self.myLineColor)
                startItem.addArrow(arrow)
                endItem.addArrow(arrow)
                arrow.setZValue(-1000.0)
                self.addItem(arrow)
                arrow.updatePosition()

        self.line _ N..
        super(DiagramScene, self).mouseReleaseEvent(mouseEvent)

    ___ isItemChange  type):
        for item in self.selectedItems
            __ isinstance(item, type):
                r_ True
        r_ False


c_ MainWindow ?MW..
    InsertTextButton _ 10

    ___ __init__(self):
        super(MainWindow, self).__init__()

        self.createActions()
        self.createMenus()
        self.createToolBox()

        self.scene _ DiagramScene(self.itemMenu)
        self.scene.setSceneRect(QRectF(0, 0, 5000, 5000))
        self.scene.itemInserted.c..(self.itemInserted)
        self.scene.textInserted.c..(self.textInserted)
        self.scene.itemSelected.c..(self.itemSelected)

        self.createToolbars()

        layout _ QHBoxLayout()
        layout.aW..(self.toolBox)
        self.view _ QGraphicsView(self.scene)
        layout.aW..(self.view)

        self.widget _ ?W..
        self.widget.sL..(layout)

        self.sCW..(self.widget)
        self.setWindowTitle("Diagramscene")

    ___ backgroundButtonGroupClicked  button):
        buttons _ self.backgroundButtonGroup.buttons()
        for myButton in buttons:
            __ myButton !_ button:
                button.setChecked F..

        t__ _ button.t__()
        __ t__ == "Blue Grid":
            self.scene.setBackgroundBrush(QBrush(QPixmap(':/images/background1.png')))
        ____ t__ == "White Grid":
            self.scene.setBackgroundBrush(QBrush(QPixmap(':/images/background2.png')))
        ____ t__ == "Gray Grid":
            self.scene.setBackgroundBrush(QBrush(QPixmap(':/images/background3.png')))
        ____
            self.scene.setBackgroundBrush(QBrush(QPixmap(':/images/background4.png')))

        self.scene.update()
        self.view.update()

    ___ buttonGroupClicked  id):
        buttons _ self.buttonGroup.buttons()
        for button in buttons:
            __ self.buttonGroup.button(id) !_ button:
                button.setChecked F..

        __ id == self.InsertTextButton:
            self.scene.setMode(DiagramScene.InsertText)
        ____
            self.scene.setItemType(id)
            self.scene.setMode(DiagramScene.InsertItem)

    ___ deleteItem(self):
        for item in self.scene.selectedItems
            __ isinstance(item, DiagramItem):
                item.removeArrows()
            self.scene.removeItem(item)

    ___ pointerGroupClicked  i):
        self.scene.setMode(self.pointerTypeGroup.checkedId())

    ___ bringToFront(self):
        __ no. self.scene.selectedItems
            r_

        selectedItem _ self.scene.selectedItems()[0]
        overlapItems _ selectedItem.collidingItems()

        zValue _ 0
        for item in overlapItems:
            __ (item.zValue() >_ zValue and isinstance(item, DiagramItem)):
                zValue _ item.zValue() + 0.1
        selectedItem.setZValue(zValue)

    ___ sendToBack(self):
        __ no. self.scene.selectedItems
            r_

        selectedItem _ self.scene.selectedItems()[0]
        overlapItems _ selectedItem.collidingItems()

        zValue _ 0
        for item in overlapItems:
            __ (item.zValue() <_ zValue and isinstance(item, DiagramItem)):
                zValue _ item.zValue() - 0.1
        selectedItem.setZValue(zValue)

    ___ itemInserted  item):
        self.pointerTypeGroup.button(DiagramScene.MoveItem).setChecked(True)
        self.scene.setMode(self.pointerTypeGroup.checkedId())
        self.buttonGroup.button(item.diagramType).setChecked F..

    ___ textInserted  item):
        self.buttonGroup.button(self.InsertTextButton).setChecked F..
        self.scene.setMode(self.pointerTypeGroup.checkedId())

    ___ currentFontChanged  font):
        self.handleFontChange()

    ___ fontSizeChanged  font):
        self.handleFontChange()

    ___ sceneScaleChanged  scale):
        newScale _ scale.left(scale.indexOf("%")).toDouble()[0] / 100.0
        oldMatrix _ self.view.matrix()
        self.view.resetMatrix()
        self.view.translate(oldMatrix.dx(), oldMatrix.dy())
        self.view.scale(newScale, newScale)

    ___ textColorChanged(self):
        self.textAction _ self.sender()
        self.fontColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/textpointer.png',
                        ?C..(self.textAction.data())))
        self.textButtonTriggered()

    ___ itemColorChanged(self):
        self.fillAction _ self.sender()
        self.fillColorToolButton.setIcon(
                self.createColorToolButtonIcon( ':/images/floodfill.png',
                        ?C..(self.fillAction.data())))
        self.fillButtonTriggered()

    ___ lineColorChanged(self):
        self.lineAction _ self.sender()
        self.lineColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/linecolor.png',
                        ?C..(self.lineAction.data())))
        self.lineButtonTriggered()

    ___ textButtonTriggered(self):
        self.scene.setTextColor(?C..(self.textAction.data()))

    ___ fillButtonTriggered(self):
        self.scene.setItemColor(?C..(self.fillAction.data()))

    ___ lineButtonTriggered(self):
        self.scene.setLineColor(?C..(self.lineAction.data()))

    ___ handleFontChange(self):
        font _ self.fontCombo.currentFont()
        font.setPointSize(self.fontSizeCombo.currentText().toInt()[0])
        __ self.boldAction.isChecked
            font.setWeight(QFont.Bold)
        ____
            font.setWeight(QFont.Normal)
        font.setItalic(self.italicAction.isChecked())
        font.setUnderline(self.underlineAction.isChecked())

        self.scene.setFont(font)

    ___ itemSelected  item):
        font _ item.font()
        color _ item.defaultTextColor()
        self.fontCombo.setCurrentFont(font)
        self.fontSizeCombo.setEditText(str(font.pointSize()))
        self.boldAction.setChecked(font.weight() == QFont.Bold)
        self.italicAction.setChecked(font.italic())
        self.underlineAction.setChecked(font.underline())

    ___ about(self):
        ?MB...about  "About Diagram Scene",
                "The <b>Diagram Scene</b> example shows use of the graphics framework.")

    ___ createToolBox(self):
        self.buttonGroup _ QButtonGroup()
        self.buttonGroup.setExclusive F..
        self.buttonGroup.buttonClicked[int].c..(self.buttonGroupClicked)

        layout _ QGridLayout()
        layout.aW..(self.createCellWidget("Conditional", DiagramItem.Conditional),
                0, 0)
        layout.aW..(self.createCellWidget("Process", DiagramItem.Step), 0,
                1)
        layout.aW..(self.createCellWidget("Input/Output", DiagramItem.Io),
                1, 0)

        textButton _ QToolButton()
        textButton.setCheckable(True)
        self.buttonGroup.addButton(textButton, self.InsertTextButton)
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

        self.backgroundButtonGroup _ QButtonGroup()
        self.backgroundButtonGroup.buttonClicked.c..(self.backgroundButtonGroupClicked)

        backgroundLayout _ QGridLayout()
        backgroundLayout.aW..(self.createBackgroundCellWidget("Blue Grid",
                ':/images/background1.png'), 0, 0)
        backgroundLayout.aW..(self.createBackgroundCellWidget("White Grid",
                ':/images/background2.png'), 0, 1)
        backgroundLayout.aW..(self.createBackgroundCellWidget("Gray Grid",
                ':/images/background3.png'), 1, 0)
        backgroundLayout.aW..(self.createBackgroundCellWidget("No Grid",
                ':/images/background4.png'), 1, 1)

        backgroundLayout.setRowStretch(2, 10)
        backgroundLayout.setColumnStretch(2, 10)

        backgroundWidget _ ?W..
        backgroundWidget.sL..(backgroundLayout)

        self.toolBox _ QToolBox()
        self.toolBox.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored))
        self.toolBox.setMinimumWidth(itemWidget.sizeHint().width())
        self.toolBox.addItem(itemWidget, "Basic Flowchart Shapes")
        self.toolBox.addItem(backgroundWidget, "Backgrounds")

    ___ createActions(self):
        self.toFrontAction _ ?A..(
                QIcon(':/images/bringtofront.png'), "Bring to &Front",
                self, shortcut_"Ctrl+F", statusTip_"Bring item to front",
                triggered_self.bringToFront)

        self.sendBackAction _ ?A..(
                QIcon(':/images/sendtoback.png'), "Send to &Back", self,
                shortcut_"Ctrl+B", statusTip_"Send item to back",
                triggered_self.sendToBack)

        self.deleteAction _ ?A..(QIcon(':/images/delete.png'),
                "&Delete", self, shortcut_"Delete",
                statusTip_"Delete item from diagram",
                triggered_self.deleteItem)

        self.exitAction _ ?A..("E&xit", self, shortcut_"Ctrl+X",
                statusTip_"Quit Scenediagram example", triggered_self.close)

        self.boldAction _ ?A..(QIcon(':/images/bold.png'),
                "Bold", self, checkable_True, shortcut_"Ctrl+B",
                triggered_self.handleFontChange)

        self.italicAction _ ?A..(QIcon(':/images/italic.png'),
                "Italic", self, checkable_True, shortcut_"Ctrl+I",
                triggered_self.handleFontChange)

        self.underlineAction _ ?A..(
                QIcon(':/images/underline.png'), "Underline", self,
                checkable_True, shortcut_"Ctrl+U",
                triggered_self.handleFontChange)

        self.aboutAction _ ?A..("A&bout", self, shortcut_"Ctrl+B",
                triggered_self.about)

    ___ createMenus(self):
        self.fileMenu _ self.mB.. .aM..("&File")
        self.fileMenu.aA..(self.exitAction)

        self.itemMenu _ self.mB.. .aM..("&Item")
        self.itemMenu.aA..(self.deleteAction)
        self.itemMenu.addSeparator()
        self.itemMenu.aA..(self.toFrontAction)
        self.itemMenu.aA..(self.sendBackAction)

        self.aboutMenu _ self.mB.. .aM..("&Help")
        self.aboutMenu.aA..(self.aboutAction)

    ___ createToolbars(self):
        self.editToolBar _ self.addToolBar("Edit")
        self.editToolBar.aA..(self.deleteAction)
        self.editToolBar.aA..(self.toFrontAction)
        self.editToolBar.aA..(self.sendBackAction)

        self.fontCombo _ QFontComboBox()
        self.fontCombo.currentFontChanged.c..(self.currentFontChanged)

        self.fontSizeCombo _ QComboBox()
        self.fontSizeCombo.setEditable(True)
        for i in range(8, 30, 2):
            self.fontSizeCombo.addItem(str(i))
        validator _ QIntValidator(2, 64, self)
        self.fontSizeCombo.setValidator(validator)
        self.fontSizeCombo.currentIndexChanged.c..(self.fontSizeChanged)

        self.fontColorToolButton _ QToolButton()
        self.fontColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.fontColorToolButton.setMenu(
                self.createColorMenu(self.textColorChanged, __.black))
        self.textAction _ self.fontColorToolButton.menu().defaultAction()
        self.fontColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/textpointer.png',
                        __.black))
        self.fontColorToolButton.setAutoFillBackground(True)
        self.fontColorToolButton.c__.c..(self.textButtonTriggered)

        self.fillColorToolButton _ QToolButton()
        self.fillColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.fillColorToolButton.setMenu(
                self.createColorMenu(self.itemColorChanged, __.white))
        self.fillAction _ self.fillColorToolButton.menu().defaultAction()
        self.fillColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/floodfill.png',
                        __.white))
        self.fillColorToolButton.c__.c..(self.fillButtonTriggered)

        self.lineColorToolButton _ QToolButton()
        self.lineColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.lineColorToolButton.setMenu(
                self.createColorMenu(self.lineColorChanged, __.black))
        self.lineAction _ self.lineColorToolButton.menu().defaultAction()
        self.lineColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/linecolor.png',
                        __.black))
        self.lineColorToolButton.c__.c..(self.lineButtonTriggered)

        self.textToolBar _ self.addToolBar("Font")
        self.textToolBar.aW..(self.fontCombo)
        self.textToolBar.aW..(self.fontSizeCombo)
        self.textToolBar.aA..(self.boldAction)
        self.textToolBar.aA..(self.italicAction)
        self.textToolBar.aA..(self.underlineAction)

        self.colorToolBar _ self.addToolBar("Color")
        self.colorToolBar.aW..(self.fontColorToolButton)
        self.colorToolBar.aW..(self.fillColorToolButton)
        self.colorToolBar.aW..(self.lineColorToolButton)

        pointerButton _ QToolButton()
        pointerButton.setCheckable(True)
        pointerButton.setChecked(True)
        pointerButton.setIcon(QIcon(':/images/pointer.png'))
        linePointerButton _ QToolButton()
        linePointerButton.setCheckable(True)
        linePointerButton.setIcon(QIcon(':/images/linepointer.png'))

        self.pointerTypeGroup _ QButtonGroup()
        self.pointerTypeGroup.addButton(pointerButton, DiagramScene.MoveItem)
        self.pointerTypeGroup.addButton(linePointerButton,
                DiagramScene.InsertLine)
        self.pointerTypeGroup.buttonClicked[int].c..(self.pointerGroupClicked)

        self.sceneScaleCombo _ QComboBox()
        self.sceneScaleCombo.addItems(["50%", "75%", "100%", "125%", "150%"])
        self.sceneScaleCombo.setCurrentIndex(2)
        self.sceneScaleCombo.currentIndexChanged[str].c..(self.sceneScaleChanged)

        self.pointerToolbar _ self.addToolBar("Pointer type")
        self.pointerToolbar.aW..(pointerButton)
        self.pointerToolbar.aW..(linePointerButton)
        self.pointerToolbar.aW..(self.sceneScaleCombo)

    ___ createBackgroundCellWidget  t__, image):
        button _ QToolButton()
        button.sT..(t__)
        button.setIcon(QIcon(image))
        button.setIconSize(QSize(50, 50))
        button.setCheckable(True)
        self.backgroundButtonGroup.addButton(button)

        layout _ QGridLayout()
        layout.aW..(button, 0, 0, __.AlignHCenter)
        layout.aW..(QLabel(t__), 1, 0, __.AlignCenter)

        widget _ ?W..
        widget.sL..(layout)

        r_ widget

    ___ createCellWidget  t__, diagramType):
        item _ DiagramItem(diagramType, self.itemMenu)
        icon _ QIcon(item.image())

        button _ QToolButton()
        button.setIcon(icon)
        button.setIconSize(QSize(50, 50))
        button.setCheckable(True)
        self.buttonGroup.addButton(button, diagramType)

        layout _ QGridLayout()
        layout.aW..(button, 0, 0, __.AlignHCenter)
        layout.aW..(QLabel(t__), 1, 0, __.AlignCenter)

        widget _ ?W..
        widget.sL..(layout)

        r_ widget

    ___ createColorMenu  slot, defaultColor):
        colors _ [__.black, __.white, __.red, __.blue, __.yellow]
        names _ ["black", "white", "red", "blue", "yellow"]

        colorMenu _ QMenu(self)
        for color, name in zip(colors, names):
            action _ ?A..(self.createColorIcon(color), name, self,
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


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    mainWindow _ MainWindow()
    mainWindow.setGeometry(100, 100, 800, 500)
    mainWindow.s..

    sys.exit(app.exec_())
