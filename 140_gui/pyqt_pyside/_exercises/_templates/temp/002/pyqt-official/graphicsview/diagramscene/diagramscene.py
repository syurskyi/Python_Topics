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

____ ?.QtCore ______ (pyqtSignal, QLineF, QPointF, QRect, QRectF, QSize,
        QSizeF, Qt)
____ ?.QtGui ______ (QBrush, QColor, QFont, QIcon, QIntValidator, QPainter,
        QPainterPath, QPen, QPixmap, QPolygonF)
____ ?.?W.. ______ (QAction, ?A.., QButtonGroup, QComboBox,
        QFontComboBox, QGraphicsItem, QGraphicsLineItem, QGraphicsPolygonItem,
        QGraphicsScene, QGraphicsTextItem, QGraphicsView, QGridLayout,
        QHBoxLayout, QLabel, QMainWindow, QMenu, QMessageBox, QSizePolicy,
        QToolBox, QToolButton, QWidget)

______ diagramscene_rc


class Arrow(QGraphicsLineItem):
    ___ __init__(self, startItem, endItem, parent_None, scene_None):
        super(Arrow, self).__init__(parent, scene)

        self.arrowHead _ QPolygonF()

        self.myStartItem _ startItem
        self.myEndItem _ endItem
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.myColor _ Qt.black
        self.setPen(QPen(self.myColor, 2, Qt.SolidLine, Qt.RoundCap,
                Qt.RoundJoin))

    ___ setColor(self, color):
        self.myColor _ color

    ___ startItem(self):
        return self.myStartItem

    ___ endItem(self):
        return self.myEndItem

    ___ boundingRect(self):
        extra _ (self.pen().width() + 20) / 2.0
        p1 _ self.line().p1()
        p2 _ self.line().p2()
        return QRectF(p1, QSizeF(p2.x() - p1.x(), p2.y() - p1.y())).normalized().adjusted(-extra, -extra, extra, extra)

    ___ shape(self):
        path _ super(Arrow, self).shape()
        path.addPolygon(self.arrowHead)
        return path

    ___ updatePosition(self):
        line _ QLineF(self.mapFromItem(self.myStartItem, 0, 0), self.mapFromItem(self.myEndItem, 0, 0))
        self.setLine(line)

    ___ paint(self, painter, option, widget_None):
        if (self.myStartItem.collidesWithItem(self.myEndItem)):
            return

        myStartItem _ self.myStartItem
        myEndItem _ self.myEndItem
        myColor _ self.myColor
        myPen _ self.pen()
        myPen.setColor(self.myColor)
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
            if intersectType == QLineF.BoundedIntersection:
                break
            p1 _ p2

        self.setLine(QLineF(intersectPoint, myStartItem.pos()))
        line _ self.line()

        angle _ math.acos(line.dx() / line.length())
        if line.dy() >_ 0:
            angle _ (math.pi * 2.0) - angle

        arrowP1 _ line.p1() + QPointF(math.sin(angle + math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi / 3) * arrowSize)
        arrowP2 _ line.p1() + QPointF(math.sin(angle + math.pi - math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi - math.pi / 3.0) * arrowSize)

        self.arrowHead.clear()
        for point in [line.p1(), arrowP1, arrowP2]:
            self.arrowHead.append(point)

        painter.drawLine(line)
        painter.drawPolygon(self.arrowHead)
        if self.isSelected
            painter.setPen(QPen(myColor, 1, Qt.DashLine))
            myLine _ QLineF(line)
            myLine.translate(0, 4.0)
            painter.drawLine(myLine)
            myLine.translate(0,-8.0)
            painter.drawLine(myLine)


class DiagramTextItem(QGraphicsTextItem):
    lostFocus _ pyqtSignal(QGraphicsTextItem)

    selectedChange _ pyqtSignal(QGraphicsItem)

    ___ __init__(self, parent_None, scene_None):
        super(DiagramTextItem, self).__init__(parent, scene)

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    ___ itemChange(self, change, value):
        if change == QGraphicsItem.ItemSelectedChange:
            self.selectedChange.emit(self)
        return value

    ___ focusOutEvent(self, event):
        self.setTextInteractionFlags(Qt.NoTextInteraction)
        self.lostFocus.emit(self)
        super(DiagramTextItem, self).focusOutEvent(event)

    ___ mouseDoubleClickEvent(self, event):
        if self.textInteractionFlags() == Qt.NoTextInteraction:
            self.setTextInteractionFlags(Qt.TextEditorInteraction)
        super(DiagramTextItem, self).mouseDoubleClickEvent(event)


class DiagramItem(QGraphicsPolygonItem):
    Step, Conditional, StartEnd, Io _ range(4)

    ___ __init__(self, diagramType, contextMenu, parent_None):
        super(DiagramItem, self).__init__(parent)

        self.arrows _ []

        self.diagramType _ diagramType
        self.contextMenu _ contextMenu

        path _ QPainterPath()
        if self.diagramType == self.StartEnd:
            path.moveTo(200, 50)
            path.arcTo(150, 0, 50, 50, 0, 90)
            path.arcTo(50, 0, 50, 50, 90, 90)
            path.arcTo(50, 50, 50, 50, 180, 90)
            path.arcTo(150, 50, 50, 50, 270, 90)
            path.lineTo(200, 25)
            self.myPolygon _ path.toFillPolygon()
        elif self.diagramType == self.Conditional:
            self.myPolygon _ QPolygonF([
                    QPointF(-100, 0), QPointF(0, 100),
                    QPointF(100, 0), QPointF(0, -100),
                    QPointF(-100, 0)])
        elif self.diagramType == self.Step:
            self.myPolygon _ QPolygonF([
                    QPointF(-100, -100), QPointF(100, -100),
                    QPointF(100, 100), QPointF(-100, 100),
                    QPointF(-100, -100)])
        else:
            self.myPolygon _ QPolygonF([
                    QPointF(-120, -80), QPointF(-70, 80),
                    QPointF(120, 80), QPointF(70, -80),
                    QPointF(-120, -80)])

        self.setPolygon(self.myPolygon)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

    ___ removeArrow(self, arrow):
        try:
            self.arrows.remove(arrow)
        except ValueError:
            pass

    ___ removeArrows(self):
        for arrow in self.arrows[:]:
            arrow.startItem().removeArrow(arrow)
            arrow.endItem().removeArrow(arrow)
            self.scene().removeItem(arrow)

    ___ addArrow(self, arrow):
        self.arrows.append(arrow)

    ___ image(self):
        pixmap _ QPixmap(250, 250)
        pixmap.fill(Qt.transparent)
        painter _ QPainter(pixmap)
        painter.setPen(QPen(Qt.black, 8))
        painter.translate(125, 125)
        painter.drawPolyline(self.myPolygon)
        return pixmap

    ___ contextMenuEvent(self, event):
        self.scene().clearSelection()
        self.setSelected(True)
        self.myContextMenu.exec_(event.screenPos())

    ___ itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for arrow in self.arrows:
                arrow.updatePosition()

        return value


class DiagramScene(QGraphicsScene):
    InsertItem, InsertLine, InsertText, MoveItem  _ range(4)

    itemInserted _ pyqtSignal(DiagramItem)

    textInserted _ pyqtSignal(QGraphicsTextItem)

    itemSelected _ pyqtSignal(QGraphicsItem)

    ___ __init__(self, itemMenu, parent_None):
        super(DiagramScene, self).__init__(parent)

        self.myItemMenu _ itemMenu
        self.myMode _ self.MoveItem
        self.myItemType _ DiagramItem.Step
        self.line _ None
        self.textItem _ None
        self.myItemColor _ Qt.white
        self.myTextColor _ Qt.black
        self.myLineColor _ Qt.black
        self.myFont _ QFont()

    ___ setLineColor(self, color):
        self.myLineColor _ color
        if self.isItemChange(Arrow):
            item _ self.selectedItems()[0]
            item.setColor(self.myLineColor)
            self.update()

    ___ setTextColor(self, color):
        self.myTextColor _ color
        if self.isItemChange(DiagramTextItem):
            item _ self.selectedItems()[0]
            item.setDefaultTextColor(self.myTextColor)

    ___ setItemColor(self, color):
        self.myItemColor _ color
        if self.isItemChange(DiagramItem):
            item _ self.selectedItems()[0]
            item.setBrush(self.myItemColor)

    ___ setFont(self, font):
        self.myFont _ font
        if self.isItemChange(DiagramTextItem):
            item _ self.selectedItems()[0]
            item.setFont(self.myFont)

    ___ setMode(self, mode):
        self.myMode _ mode

    ___ setItemType(self, type):
        self.myItemType _ type

    ___ editorLostFocus(self, item):
        cursor _ item.textCursor()
        cursor.clearSelection()
        item.setTextCursor(cursor)

        if item.toPlainText
            self.removeItem(item)
            item.deleteLater()

    ___ mousePressEvent(self, mouseEvent):
        if (mouseEvent.button() !_ Qt.LeftButton):
            return

        if self.myMode == self.InsertItem:
            item _ DiagramItem(self.myItemType, self.myItemMenu)
            item.setBrush(self.myItemColor)
            self.addItem(item)
            item.setPos(mouseEvent.scenePos())
            self.itemInserted.emit(item)
        elif self.myMode == self.InsertLine:
            self.line _ QGraphicsLineItem(QLineF(mouseEvent.scenePos(),
                    mouseEvent.scenePos()))
            self.line.setPen(QPen(self.myLineColor, 2))
            self.addItem(self.line)
        elif self.myMode == self.InsertText:
            textItem _ DiagramTextItem()
            textItem.setFont(self.myFont)
            textItem.setTextInteractionFlags(Qt.TextEditorInteraction)
            textItem.setZValue(1000.0)
            textItem.lostFocus.c..(self.editorLostFocus)
            textItem.selectedChange.c..(self.itemSelected)
            self.addItem(textItem)
            textItem.setDefaultTextColor(self.myTextColor)
            textItem.setPos(mouseEvent.scenePos())
            self.textInserted.emit(textItem)

        super(DiagramScene, self).mousePressEvent(mouseEvent)

    ___ mouseMoveEvent(self, mouseEvent):
        if self.myMode == self.InsertLine and self.line:
            newLine _ QLineF(self.line.line().p1(), mouseEvent.scenePos())
            self.line.setLine(newLine)
        elif self.myMode == self.MoveItem:
            super(DiagramScene, self).mouseMoveEvent(mouseEvent)

    ___ mouseReleaseEvent(self, mouseEvent):
        if self.line and self.myMode == self.InsertLine:
            startItems _ self.items(self.line.line().p1())
            if len(startItems) and startItems[0] == self.line:
                startItems.pop(0)
            endItems _ self.items(self.line.line().p2())
            if len(endItems) and endItems[0] == self.line:
                endItems.pop(0)

            self.removeItem(self.line)
            self.line _ None

            if len(startItems) and len(endItems) and \
                    isinstance(startItems[0], DiagramItem) and \
                    isinstance(endItems[0], DiagramItem) and \
                    startItems[0] !_ endItems[0]:
                startItem _ startItems[0]
                endItem _ endItems[0]
                arrow _ Arrow(startItem, endItem)
                arrow.setColor(self.myLineColor)
                startItem.addArrow(arrow)
                endItem.addArrow(arrow)
                arrow.setZValue(-1000.0)
                self.addItem(arrow)
                arrow.updatePosition()

        self.line _ None
        super(DiagramScene, self).mouseReleaseEvent(mouseEvent)

    ___ isItemChange(self, type):
        for item in self.selectedItems
            if isinstance(item, type):
                return True
        return False


class MainWindow(QMainWindow):
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
        layout.addWidget(self.toolBox)
        self.view _ QGraphicsView(self.scene)
        layout.addWidget(self.view)

        self.widget _ QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        self.setWindowTitle("Diagramscene")

    ___ backgroundButtonGroupClicked(self, button):
        buttons _ self.backgroundButtonGroup.buttons()
        for myButton in buttons:
            if myButton !_ button:
                button.setChecked(False)

        text _ button.text()
        if text == "Blue Grid":
            self.scene.setBackgroundBrush(QBrush(QPixmap(':/images/background1.png')))
        elif text == "White Grid":
            self.scene.setBackgroundBrush(QBrush(QPixmap(':/images/background2.png')))
        elif text == "Gray Grid":
            self.scene.setBackgroundBrush(QBrush(QPixmap(':/images/background3.png')))
        else:
            self.scene.setBackgroundBrush(QBrush(QPixmap(':/images/background4.png')))

        self.scene.update()
        self.view.update()

    ___ buttonGroupClicked(self, id):
        buttons _ self.buttonGroup.buttons()
        for button in buttons:
            if self.buttonGroup.button(id) !_ button:
                button.setChecked(False)

        if id == self.InsertTextButton:
            self.scene.setMode(DiagramScene.InsertText)
        else:
            self.scene.setItemType(id)
            self.scene.setMode(DiagramScene.InsertItem)

    ___ deleteItem(self):
        for item in self.scene.selectedItems
            if isinstance(item, DiagramItem):
                item.removeArrows()
            self.scene.removeItem(item)

    ___ pointerGroupClicked(self, i):
        self.scene.setMode(self.pointerTypeGroup.checkedId())

    ___ bringToFront(self):
        if not self.scene.selectedItems
            return

        selectedItem _ self.scene.selectedItems()[0]
        overlapItems _ selectedItem.collidingItems()

        zValue _ 0
        for item in overlapItems:
            if (item.zValue() >_ zValue and isinstance(item, DiagramItem)):
                zValue _ item.zValue() + 0.1
        selectedItem.setZValue(zValue)

    ___ sendToBack(self):
        if not self.scene.selectedItems
            return

        selectedItem _ self.scene.selectedItems()[0]
        overlapItems _ selectedItem.collidingItems()

        zValue _ 0
        for item in overlapItems:
            if (item.zValue() <_ zValue and isinstance(item, DiagramItem)):
                zValue _ item.zValue() - 0.1
        selectedItem.setZValue(zValue)

    ___ itemInserted(self, item):
        self.pointerTypeGroup.button(DiagramScene.MoveItem).setChecked(True)
        self.scene.setMode(self.pointerTypeGroup.checkedId())
        self.buttonGroup.button(item.diagramType).setChecked(False)

    ___ textInserted(self, item):
        self.buttonGroup.button(self.InsertTextButton).setChecked(False)
        self.scene.setMode(self.pointerTypeGroup.checkedId())

    ___ currentFontChanged(self, font):
        self.handleFontChange()

    ___ fontSizeChanged(self, font):
        self.handleFontChange()

    ___ sceneScaleChanged(self, scale):
        newScale _ scale.left(scale.indexOf("%")).toDouble()[0] / 100.0
        oldMatrix _ self.view.matrix()
        self.view.resetMatrix()
        self.view.translate(oldMatrix.dx(), oldMatrix.dy())
        self.view.scale(newScale, newScale)

    ___ textColorChanged(self):
        self.textAction _ self.sender()
        self.fontColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/textpointer.png',
                        QColor(self.textAction.data())))
        self.textButtonTriggered()

    ___ itemColorChanged(self):
        self.fillAction _ self.sender()
        self.fillColorToolButton.setIcon(
                self.createColorToolButtonIcon( ':/images/floodfill.png',
                        QColor(self.fillAction.data())))
        self.fillButtonTriggered()

    ___ lineColorChanged(self):
        self.lineAction _ self.sender()
        self.lineColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/linecolor.png',
                        QColor(self.lineAction.data())))
        self.lineButtonTriggered()

    ___ textButtonTriggered(self):
        self.scene.setTextColor(QColor(self.textAction.data()))

    ___ fillButtonTriggered(self):
        self.scene.setItemColor(QColor(self.fillAction.data()))

    ___ lineButtonTriggered(self):
        self.scene.setLineColor(QColor(self.lineAction.data()))

    ___ handleFontChange(self):
        font _ self.fontCombo.currentFont()
        font.setPointSize(self.fontSizeCombo.currentText().toInt()[0])
        if self.boldAction.isChecked
            font.setWeight(QFont.Bold)
        else:
            font.setWeight(QFont.Normal)
        font.setItalic(self.italicAction.isChecked())
        font.setUnderline(self.underlineAction.isChecked())

        self.scene.setFont(font)

    ___ itemSelected(self, item):
        font _ item.font()
        color _ item.defaultTextColor()
        self.fontCombo.setCurrentFont(font)
        self.fontSizeCombo.setEditText(str(font.pointSize()))
        self.boldAction.setChecked(font.weight() == QFont.Bold)
        self.italicAction.setChecked(font.italic())
        self.underlineAction.setChecked(font.underline())

    ___ about(self):
        QMessageBox.about(self, "About Diagram Scene",
                "The <b>Diagram Scene</b> example shows use of the graphics framework.")

    ___ createToolBox(self):
        self.buttonGroup _ QButtonGroup()
        self.buttonGroup.setExclusive(False)
        self.buttonGroup.buttonClicked[int].c..(self.buttonGroupClicked)

        layout _ QGridLayout()
        layout.addWidget(self.createCellWidget("Conditional", DiagramItem.Conditional),
                0, 0)
        layout.addWidget(self.createCellWidget("Process", DiagramItem.Step), 0,
                1)
        layout.addWidget(self.createCellWidget("Input/Output", DiagramItem.Io),
                1, 0)

        textButton _ QToolButton()
        textButton.setCheckable(True)
        self.buttonGroup.addButton(textButton, self.InsertTextButton)
        textButton.setIcon(QIcon(QPixmap(':/images/textpointer.png').scaled(30, 30)))
        textButton.setIconSize(QSize(50, 50))

        textLayout _ QGridLayout()
        textLayout.addWidget(textButton, 0, 0, Qt.AlignHCenter)
        textLayout.addWidget(QLabel("Text"), 1, 0, Qt.AlignCenter)
        textWidget _ QWidget()
        textWidget.setLayout(textLayout)
        layout.addWidget(textWidget, 1, 1)

        layout.setRowStretch(3, 10)
        layout.setColumnStretch(2, 10)

        itemWidget _ QWidget()
        itemWidget.setLayout(layout)

        self.backgroundButtonGroup _ QButtonGroup()
        self.backgroundButtonGroup.buttonClicked.c..(self.backgroundButtonGroupClicked)

        backgroundLayout _ QGridLayout()
        backgroundLayout.addWidget(self.createBackgroundCellWidget("Blue Grid",
                ':/images/background1.png'), 0, 0)
        backgroundLayout.addWidget(self.createBackgroundCellWidget("White Grid",
                ':/images/background2.png'), 0, 1)
        backgroundLayout.addWidget(self.createBackgroundCellWidget("Gray Grid",
                ':/images/background3.png'), 1, 0)
        backgroundLayout.addWidget(self.createBackgroundCellWidget("No Grid",
                ':/images/background4.png'), 1, 1)

        backgroundLayout.setRowStretch(2, 10)
        backgroundLayout.setColumnStretch(2, 10)

        backgroundWidget _ QWidget()
        backgroundWidget.setLayout(backgroundLayout)

        self.toolBox _ QToolBox()
        self.toolBox.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored))
        self.toolBox.setMinimumWidth(itemWidget.sizeHint().width())
        self.toolBox.addItem(itemWidget, "Basic Flowchart Shapes")
        self.toolBox.addItem(backgroundWidget, "Backgrounds")

    ___ createActions(self):
        self.toFrontAction _ QAction(
                QIcon(':/images/bringtofront.png'), "Bring to &Front",
                self, shortcut_"Ctrl+F", statusTip_"Bring item to front",
                triggered_self.bringToFront)

        self.sendBackAction _ QAction(
                QIcon(':/images/sendtoback.png'), "Send to &Back", self,
                shortcut_"Ctrl+B", statusTip_"Send item to back",
                triggered_self.sendToBack)

        self.deleteAction _ QAction(QIcon(':/images/delete.png'),
                "&Delete", self, shortcut_"Delete",
                statusTip_"Delete item from diagram",
                triggered_self.deleteItem)

        self.exitAction _ QAction("E&xit", self, shortcut_"Ctrl+X",
                statusTip_"Quit Scenediagram example", triggered_self.close)

        self.boldAction _ QAction(QIcon(':/images/bold.png'),
                "Bold", self, checkable_True, shortcut_"Ctrl+B",
                triggered_self.handleFontChange)

        self.italicAction _ QAction(QIcon(':/images/italic.png'),
                "Italic", self, checkable_True, shortcut_"Ctrl+I",
                triggered_self.handleFontChange)

        self.underlineAction _ QAction(
                QIcon(':/images/underline.png'), "Underline", self,
                checkable_True, shortcut_"Ctrl+U",
                triggered_self.handleFontChange)

        self.aboutAction _ QAction("A&bout", self, shortcut_"Ctrl+B",
                triggered_self.about)

    ___ createMenus(self):
        self.fileMenu _ self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.exitAction)

        self.itemMenu _ self.menuBar().addMenu("&Item")
        self.itemMenu.addAction(self.deleteAction)
        self.itemMenu.addSeparator()
        self.itemMenu.addAction(self.toFrontAction)
        self.itemMenu.addAction(self.sendBackAction)

        self.aboutMenu _ self.menuBar().addMenu("&Help")
        self.aboutMenu.addAction(self.aboutAction)

    ___ createToolbars(self):
        self.editToolBar _ self.addToolBar("Edit")
        self.editToolBar.addAction(self.deleteAction)
        self.editToolBar.addAction(self.toFrontAction)
        self.editToolBar.addAction(self.sendBackAction)

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
                self.createColorMenu(self.textColorChanged, Qt.black))
        self.textAction _ self.fontColorToolButton.menu().defaultAction()
        self.fontColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/textpointer.png',
                        Qt.black))
        self.fontColorToolButton.setAutoFillBackground(True)
        self.fontColorToolButton.c__.c..(self.textButtonTriggered)

        self.fillColorToolButton _ QToolButton()
        self.fillColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.fillColorToolButton.setMenu(
                self.createColorMenu(self.itemColorChanged, Qt.white))
        self.fillAction _ self.fillColorToolButton.menu().defaultAction()
        self.fillColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/floodfill.png',
                        Qt.white))
        self.fillColorToolButton.c__.c..(self.fillButtonTriggered)

        self.lineColorToolButton _ QToolButton()
        self.lineColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.lineColorToolButton.setMenu(
                self.createColorMenu(self.lineColorChanged, Qt.black))
        self.lineAction _ self.lineColorToolButton.menu().defaultAction()
        self.lineColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/linecolor.png',
                        Qt.black))
        self.lineColorToolButton.c__.c..(self.lineButtonTriggered)

        self.textToolBar _ self.addToolBar("Font")
        self.textToolBar.addWidget(self.fontCombo)
        self.textToolBar.addWidget(self.fontSizeCombo)
        self.textToolBar.addAction(self.boldAction)
        self.textToolBar.addAction(self.italicAction)
        self.textToolBar.addAction(self.underlineAction)

        self.colorToolBar _ self.addToolBar("Color")
        self.colorToolBar.addWidget(self.fontColorToolButton)
        self.colorToolBar.addWidget(self.fillColorToolButton)
        self.colorToolBar.addWidget(self.lineColorToolButton)

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
        self.pointerToolbar.addWidget(pointerButton)
        self.pointerToolbar.addWidget(linePointerButton)
        self.pointerToolbar.addWidget(self.sceneScaleCombo)

    ___ createBackgroundCellWidget(self, text, image):
        button _ QToolButton()
        button.sT..(text)
        button.setIcon(QIcon(image))
        button.setIconSize(QSize(50, 50))
        button.setCheckable(True)
        self.backgroundButtonGroup.addButton(button)

        layout _ QGridLayout()
        layout.addWidget(button, 0, 0, Qt.AlignHCenter)
        layout.addWidget(QLabel(text), 1, 0, Qt.AlignCenter)

        widget _ QWidget()
        widget.setLayout(layout)

        return widget

    ___ createCellWidget(self, text, diagramType):
        item _ DiagramItem(diagramType, self.itemMenu)
        icon _ QIcon(item.image())

        button _ QToolButton()
        button.setIcon(icon)
        button.setIconSize(QSize(50, 50))
        button.setCheckable(True)
        self.buttonGroup.addButton(button, diagramType)

        layout _ QGridLayout()
        layout.addWidget(button, 0, 0, Qt.AlignHCenter)
        layout.addWidget(QLabel(text), 1, 0, Qt.AlignCenter)

        widget _ QWidget()
        widget.setLayout(layout)

        return widget

    ___ createColorMenu(self, slot, defaultColor):
        colors _ [Qt.black, Qt.white, Qt.red, Qt.blue, Qt.yellow]
        names _ ["black", "white", "red", "blue", "yellow"]

        colorMenu _ QMenu(self)
        for color, name in zip(colors, names):
            action _ QAction(self.createColorIcon(color), name, self,
                    triggered_slot)
            action.setData(QColor(color)) 
            colorMenu.addAction(action)
            if color == defaultColor:
                colorMenu.setDefaultAction(action)
        return colorMenu

    ___ createColorToolButtonIcon(self, imageFile, color):
        pixmap _ QPixmap(50, 80)
        pixmap.fill(Qt.transparent)
        painter _ QPainter(pixmap)
        image _ QPixmap(imageFile)
        target _ QRect(0, 0, 50, 60)
        source _ QRect(0, 0, 42, 42)
        painter.fillRect(QRect(0, 60, 50, 80), color)
        painter.drawPixmap(target, image, source)
        painter.end()

        return QIcon(pixmap)

    ___ createColorIcon(self, color):
        pixmap _ QPixmap(20, 20)
        painter _ QPainter(pixmap)
        painter.setPen(Qt.NoPen)
        painter.fillRect(QRect(0, 0, 20, 20), color)
        painter.end()

        return QIcon(pixmap)


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)

    mainWindow _ MainWindow()
    mainWindow.setGeometry(100, 100, 800, 500)
    mainWindow.s..

    sys.exit(app.exec_())
