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

____ ?.?C.. ______ (qAbs, QLineF, QPointF, qrand, QRectF, QSizeF, qsrand,
        __, QTime)
____ ?.?G.. ______ (QBrush, ?C.., QLinearGradient, QPainter,
        QPainterPath, QPen, QPolygonF, QRadialGradient)
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsScene,
        QGraphicsView, QStyle)


c_ Edge(QGraphicsItem):
    Pi _ math.pi
    TwoPi _ 2.0 * Pi

    Type _ QGraphicsItem.UserType + 2

    ___ __init__  sourceNode, destNode):
        super(Edge, self).__init__()

        self.arrowSize _ 10.0
        self.sourcePoint _ QPointF()
        self.destPoint _ QPointF()

        self.setAcceptedMouseButtons(__.NoButton)
        self.source _ sourceNode
        self.dest _ destNode
        self.source.addEdge(self)
        self.dest.addEdge(self)
        self.adjust()

    ___ type(self):
        r_ Edge.Type

    ___ sourceNode(self):
        r_ self.source

    ___ setSourceNode  node):
        self.source _ node
        self.adjust()

    ___ destNode(self):
        r_ self.dest

    ___ setDestNode  node):
        self.dest _ node
        self.adjust()

    ___ adjust(self):
        __ no. self.source or no. self.dest:
            r_

        line _ QLineF(self.mapFromItem(self.source, 0, 0),
                self.mapFromItem(self.dest, 0, 0))
        length _ line.length()

        self.prepareGeometryChange()

        __ length > 20.0:
            edgeOffset _ QPointF((line.dx() * 10) / length,
                    (line.dy() * 10) / length)

            self.sourcePoint _ line.p1() + edgeOffset
            self.destPoint _ line.p2() - edgeOffset
        ____
            self.sourcePoint _ line.p1()
            self.destPoint _ line.p1()

    ___ boundingRect(self):
        __ no. self.source or no. self.dest:
            r_ QRectF()

        penWidth _ 1.0
        extra _ (penWidth + self.arrowSize) / 2.0

        r_ QRectF(self.sourcePoint,
                QSizeF(self.destPoint.x() - self.sourcePoint.x(),
                        self.destPoint.y() - self.sourcePoint.y())).normalized().adjusted(-extra, -extra, extra, extra)

    ___ paint  painter, option, widget):
        __ no. self.source or no. self.dest:
            r_

        # Draw the line itself.
        line _ QLineF(self.sourcePoint, self.destPoint)

        __ line.length() == 0.0:
            r_

        painter.setPen(QPen(__.black, 1, __.SolidLine, __.RoundCap,
                __.RoundJoin))
        painter.drawLine(line)

        # Draw the arrows if there's enough room.
        angle _ math.acos(line.dx() / line.length())
        __ line.dy() >_ 0:
            angle _ Edge.TwoPi - angle

        sourceArrowP1 _ self.sourcePoint + QPointF(math.sin(angle + Edge.Pi / 3) * self.arrowSize,
                                                          math.cos(angle + Edge.Pi / 3) * self.arrowSize)
        sourceArrowP2 _ self.sourcePoint + QPointF(math.sin(angle + Edge.Pi - Edge.Pi / 3) * self.arrowSize,
                                                          math.cos(angle + Edge.Pi - Edge.Pi / 3) * self.arrowSize);   
        destArrowP1 _ self.destPoint + QPointF(math.sin(angle - Edge.Pi / 3) * self.arrowSize,
                                                      math.cos(angle - Edge.Pi / 3) * self.arrowSize)
        destArrowP2 _ self.destPoint + QPointF(math.sin(angle - Edge.Pi + Edge.Pi / 3) * self.arrowSize,
                                                      math.cos(angle - Edge.Pi + Edge.Pi / 3) * self.arrowSize)

        painter.setBrush(__.black)
        painter.drawPolygon(QPolygonF([line.p1(), sourceArrowP1, sourceArrowP2]))
        painter.drawPolygon(QPolygonF([line.p2(), destArrowP1, destArrowP2]))


c_ Node(QGraphicsItem):
    Type _ QGraphicsItem.UserType + 1

    ___ __init__  graphWidget):
        super(Node, self).__init__()

        self.graph _ graphWidget
        self.edgeList _   # list
        self.newPos _ QPointF()

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(1)

    ___ type(self):
        r_ Node.Type

    ___ addEdge  edge):
        self.edgeList.ap..(edge)
        edge.adjust()

    ___ edges(self):
        r_ self.edgeList

    ___ calculateForces(self):
        __ no. self.scene() or self.scene().mouseGrabberItem() __ self:
            self.newPos _ self.pos()
            r_
    
        # Sum up all forces pushing this item away.
        xvel _ 0.0
        yvel _ 0.0
        for item in self.scene().items
            __ no. isinstance(item, Node):
                continue

            line _ QLineF(self.mapFromItem(item, 0, 0), QPointF(0, 0))
            dx _ line.dx()
            dy _ line.dy()
            l _ 2.0 * (dx * dx + dy * dy)
            __ l > 0:
                xvel +_ (dx * 150.0) / l
                yvel +_ (dy * 150.0) / l

        # Now subtract all forces pulling items together.
        weight _ (le.(self.edgeList) + 1) * 10.0
        for edge in self.edgeList:
            __ edge.sourceNode() __ self:
                pos _ self.mapFromItem(edge.destNode(), 0, 0)
            ____
                pos _ self.mapFromItem(edge.sourceNode(), 0, 0)
            xvel +_ pos.x() / weight
            yvel +_ pos.y() / weight
    
        __ qAbs(xvel) < 0.1 and qAbs(yvel) < 0.1:
            xvel _ yvel _ 0.0

        sceneRect _ self.scene().sceneRect()
        self.newPos _ self.pos() + QPointF(xvel, yvel)
        self.newPos.setX(min(max(self.newPos.x(), sceneRect.left() + 10), sceneRect.right() - 10))
        self.newPos.setY(min(max(self.newPos.y(), sceneRect.top() + 10), sceneRect.bottom() - 10))

    ___ advance(self):
        __ self.newPos == self.pos
            r_ False

        self.setPos(self.newPos)
        r_ True

    ___ boundingRect(self):
        adjust _ 2.0
        r_ QRectF(-10 - adjust, -10 - adjust, 23 + adjust, 23 + adjust)

    ___ shape(self):
        path _ QPainterPath()
        path.addEllipse(-10, -10, 20, 20)
        r_ path

    ___ paint  painter, option, widget):
        painter.setPen(__.NoPen)
        painter.setBrush(__.darkGray)
        painter.drawEllipse(-7, -7, 20, 20)

        gradient _ QRadialGradient(-3, -3, 10)
        __ option.state & QStyle.State_Sunken:
            gradient.setCenter(3, 3)
            gradient.setFocalPoint(3, 3)
            gradient.setColorAt(1, ?C..(__.yellow).lighter(120))
            gradient.setColorAt(0, ?C..(__.darkYellow).lighter(120))
        ____
            gradient.setColorAt(0, __.yellow)
            gradient.setColorAt(1, __.darkYellow)

        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(__.black, 0))
        painter.drawEllipse(-10, -10, 20, 20)

    ___ itemChange  change, value):
        __ change == QGraphicsItem.ItemPositionHasChanged:
            for edge in self.edgeList:
                edge.adjust()
            self.graph.itemMoved()

        r_ super(Node, self).itemChange(change, value)

    ___ mousePressEvent  event):
        self.update()
        super(Node, self).mousePressEvent(event)

    ___ mouseReleaseEvent  event):
        self.update()
        super(Node, self).mouseReleaseEvent(event)


c_ GraphWidget(QGraphicsView):
    ___ __init__(self):
        super(GraphWidget, self).__init__()

        self.timerId _ 0

        scene _ QGraphicsScene(self)
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.setSceneRect(-200, -200, 400, 400)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        node1 _ Node(self)
        node2 _ Node(self)
        node3 _ Node(self)
        node4 _ Node(self)
        self.centerNode _ Node(self)
        node6 _ Node(self)
        node7 _ Node(self)
        node8 _ Node(self)
        node9 _ Node(self)
        scene.addItem(node1)
        scene.addItem(node2)
        scene.addItem(node3)
        scene.addItem(node4)
        scene.addItem(self.centerNode)
        scene.addItem(node6)
        scene.addItem(node7)
        scene.addItem(node8)
        scene.addItem(node9)
        scene.addItem(Edge(node1, node2))
        scene.addItem(Edge(node2, node3))
        scene.addItem(Edge(node2, self.centerNode))
        scene.addItem(Edge(node3, node6))
        scene.addItem(Edge(node4, node1))
        scene.addItem(Edge(node4, self.centerNode))
        scene.addItem(Edge(self.centerNode, node6))
        scene.addItem(Edge(self.centerNode, node8))
        scene.addItem(Edge(node6, node9))
        scene.addItem(Edge(node7, node4))
        scene.addItem(Edge(node8, node7))
        scene.addItem(Edge(node9, node8))

        node1.setPos(-50, -50)
        node2.setPos(0, -50)
        node3.setPos(50, -50)
        node4.setPos(-50, 0)
        self.centerNode.setPos(0, 0)
        node6.setPos(50, 0)
        node7.setPos(-50, 50)
        node8.setPos(0, 50)
        node9.setPos(50, 50)

        self.scale(0.8, 0.8)
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Elastic Nodes")

    ___ itemMoved(self):
        __ no. self.timerId:
            self.timerId _ self.startTimer(1000 / 25)

    ___ keyPressEvent  event):
        key _ event.key()

        __ key == __.Key_Up:
            self.centerNode.moveBy(0, -20)
        ____ key == __.Key_Down:
            self.centerNode.moveBy(0, 20)
        ____ key == __.Key_Left:
            self.centerNode.moveBy(-20, 0)
        ____ key == __.Key_Right:
            self.centerNode.moveBy(20, 0)
        ____ key == __.Key_Plus:
            self.scaleView(1.2)
        ____ key == __.Key_Minus:
            self.scaleView(1 / 1.2)
        ____ key == __.Key_Space or key == __.Key_Enter:
            for item in self.scene().items
                __ isinstance(item, Node):
                    item.setPos(-150 + qrand() % 300, -150 + qrand() % 300)
        ____
            super(GraphWidget, self).keyPressEvent(event)

    ___ timerEvent  event):
        nodes _ [item for item in self.scene().items() __ isinstance(item, Node)]

        for node in nodes:
            node.calculateForces()

        itemsMoved _ False
        for node in nodes:
            __ node.advance
                itemsMoved _ True

        __ no. itemsMoved:
            self.killTimer(self.timerId)
            self.timerId _ 0

    ___ wheelEvent  event):
        self.scaleView(math.pow(2.0, -event.angleDelta().y() / 240.0))

    ___ drawBackground  painter, rect):
        # Shadow.
        sceneRect _ self.sceneRect()
        rightShadow _ QRectF(sceneRect.right(), sceneRect.top() + 5, 5,
                sceneRect.height())
        bottomShadow _ QRectF(sceneRect.left() + 5, sceneRect.bottom(),
                sceneRect.width(), 5)
        __ rightShadow.intersects(rect) or rightShadow.contains(rect):
	        painter.fillRect(rightShadow, __.darkGray)
        __ bottomShadow.intersects(rect) or bottomShadow.contains(rect):
	        painter.fillRect(bottomShadow, __.darkGray)

        # Fill.
        gradient _ QLinearGradient(sceneRect.topLeft(), sceneRect.bottomRight())
        gradient.setColorAt(0, __.white)
        gradient.setColorAt(1, __.lightGray)
        painter.fillRect(rect.intersected(sceneRect), QBrush(gradient))
        painter.setBrush(__.NoBrush)
        painter.drawRect(sceneRect)

        # Text.
        textRect _ QRectF(sceneRect.left() + 4, sceneRect.top() + 4,
                sceneRect.width() - 4, sceneRect.height() - 4)
        message _ "Click and drag the nodes around, and zoom with the " \
                "mouse wheel or the '+' and '-' keys"

        font _ painter.font()
        font.setBold(True)
        font.setPointSize(14)
        painter.setFont(font)
        painter.setPen(__.lightGray)
        painter.drawText(textRect.translated(2, 2), message)
        painter.setPen(__.black)
        painter.drawText(textRect, message)

    ___ scaleView  scaleFactor):
        factor _ self.transform().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()

        __ factor < 0.07 or factor > 100:
            r_

        self.scale(scaleFactor, scaleFactor)


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    qsrand(QTime(0,0,0).secsTo(QTime.currentTime()))

    widget _ GraphWidget()
    widget.s..

    ___.exit(app.exec_())
