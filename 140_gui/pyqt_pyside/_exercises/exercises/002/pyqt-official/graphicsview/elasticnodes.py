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


______ m__

____ ?.?C.. ______ (qAbs, QLineF, QPointF, qrand, QRectF, QSizeF, qsrand,
        __, ?T..)
____ ?.?G.. ______ (?B.., ?C.., QLinearGradient, QPainter,
        QPainterPath, ?P.., QPolygonF, QRadialGradient)
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsScene,
        QGraphicsView, ?S..)


c_ Edge(QGraphicsItem):
    Pi _ m__.pi
    TwoPi _ 2.0 * Pi

    Type _ QGraphicsItem.UserType + 2

    ___  -   sourceNode, destNode):
        s__(Edge, self). - ()

        arrowSize _ 10.0
        sourcePoint _ QPointF()
        destPoint _ QPointF()

        setAcceptedMouseButtons(__.NoButton)
        source _ sourceNode
        dest _ destNode
        source.addEdge
        dest.addEdge
        adjust()

    ___ type
        r_ Edge.Type

    ___ sourceNode
        r_ source

    ___ setSourceNode  node):
        source _ node
        adjust()

    ___ destNode
        r_ dest

    ___ setDestNode  node):
        dest _ node
        adjust()

    ___ adjust
        __ no. source or no. dest:
            r_

        line _ QLineF(mapFromItem(source, 0, 0),
                mapFromItem(dest, 0, 0))
        length _ line.length()

        prepareGeometryChange()

        __ length > 20.0:
            edgeOffset _ QPointF((line.dx() * 10) / length,
                    (line.dy() * 10) / length)

            sourcePoint _ line.p1() + edgeOffset
            destPoint _ line.p2() - edgeOffset
        ____
            sourcePoint _ line.p1()
            destPoint _ line.p1()

    ___ boundingRect
        __ no. source or no. dest:
            r_ QRectF()

        penWidth _ 1.0
        extra _ (penWidth + arrowSize) / 2.0

        r_ QRectF(sourcePoint,
                QSizeF(destPoint.x() - sourcePoint.x(),
                        destPoint.y() - sourcePoint.y())).normalized().adjusted(-extra, -extra, extra, extra)

    ___ paint  painter, option, widget):
        __ no. source or no. dest:
            r_

        # Draw the line itself.
        line _ QLineF(sourcePoint, destPoint)

        __ line.length() __ 0.0:
            r_

        painter.sP..(?P..(__.black, 1, __.SolidLine, __.RoundCap,
                __.RoundJoin))
        painter.drawLine(line)

        # Draw the arrows if there's enough room.
        angle _ m__.acos(line.dx() / line.length())
        __ line.dy() >_ 0:
            angle _ Edge.TwoPi - angle

        sourceArrowP1 _ sourcePoint + QPointF(m__.sin(angle + Edge.Pi / 3) * arrowSize,
                                                          m__.cos(angle + Edge.Pi / 3) * arrowSize)
        sourceArrowP2 _ sourcePoint + QPointF(m__.sin(angle + Edge.Pi - Edge.Pi / 3) * arrowSize,
                                                          m__.cos(angle + Edge.Pi - Edge.Pi / 3) * arrowSize);
        destArrowP1 _ destPoint + QPointF(m__.sin(angle - Edge.Pi / 3) * arrowSize,
                                                      m__.cos(angle - Edge.Pi / 3) * arrowSize)
        destArrowP2 _ destPoint + QPointF(m__.sin(angle - Edge.Pi + Edge.Pi / 3) * arrowSize,
                                                      m__.cos(angle - Edge.Pi + Edge.Pi / 3) * arrowSize)

        painter.sB..(__.black)
        painter.drawPolygon(QPolygonF([line.p1(), sourceArrowP1, sourceArrowP2]))
        painter.drawPolygon(QPolygonF([line.p2(), destArrowP1, destArrowP2]))


c_ Node(QGraphicsItem):
    Type _ QGraphicsItem.UserType + 1

    ___  -   graphWidget):
        s__(Node, self). - ()

        graph _ graphWidget
        edgeList _   # list
        newPos _ QPointF()

        setFlag(QGraphicsItem.ItemIsMovable)
        setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        setZValue(1)

    ___ type
        r_ Node.Type

    ___ addEdge  edge):
        edgeList.ap..(edge)
        edge.adjust()

    ___ edges
        r_ edgeList

    ___ calculateForces
        __ no. scene() or scene().mouseGrabberItem() __ self:
            newPos _ pos()
            r_
    
        # Sum up all forces pushing this item away.
        xvel _ 0.0
        yvel _ 0.0
        ___ item __ scene().i..
            __ no. isinstance(item, Node):
                c___

            line _ QLineF(mapFromItem(item, 0, 0), QPointF(0, 0))
            dx _ line.dx()
            dy _ line.dy()
            l _ 2.0 * (dx * dx + dy * dy)
            __ l > 0:
                xvel +_ (dx * 150.0) / l
                yvel +_ (dy * 150.0) / l

        # Now subtract all forces pulling items together.
        weight _ (le.(edgeList) + 1) * 10.0
        ___ edge __ edgeList:
            __ edge.sourceNode() __ self:
                pos _ mapFromItem(edge.destNode(), 0, 0)
            ____
                pos _ mapFromItem(edge.sourceNode(), 0, 0)
            xvel +_ pos.x() / weight
            yvel +_ pos.y() / weight
    
        __ qAbs(xvel) < 0.1 and qAbs(yvel) < 0.1:
            xvel _ yvel _ 0.0

        sceneRect _ scene().sceneRect()
        newPos _ pos() + QPointF(xvel, yvel)
        newPos.setX(min(max(newPos.x(), sceneRect.left() + 10), sceneRect.right() - 10))
        newPos.setY(min(max(newPos.y(), sceneRect.top() + 10), sceneRect.bottom() - 10))

    ___ advance
        __ newPos __ pos
            r_ F..

        setPos(newPos)
        r_ T..

    ___ boundingRect
        adjust _ 2.0
        r_ QRectF(-10 - adjust, -10 - adjust, 23 + adjust, 23 + adjust)

    ___ shape
        pa__ _ QPainterPath()
        pa__.addEllipse(-10, -10, 20, 20)
        r_ pa__

    ___ paint  painter, option, widget):
        painter.sP..(__.NoPen)
        painter.sB..(__.darkGray)
        painter.drawEllipse(-7, -7, 20, 20)

        gradient _ QRadialGradient(-3, -3, 10)
        __ option.state & ?S...State_Sunken:
            gradient.setCenter(3, 3)
            gradient.setFocalPoint(3, 3)
            gradient.setColorAt(1, ?C..(__.yellow).lighter(120))
            gradient.setColorAt(0, ?C..(__.darkYellow).lighter(120))
        ____
            gradient.setColorAt(0, __.yellow)
            gradient.setColorAt(1, __.darkYellow)

        painter.sB..(?B..(gradient))
        painter.sP..(?P..(__.black, 0))
        painter.drawEllipse(-10, -10, 20, 20)

    ___ itemChange  change, value):
        __ change __ QGraphicsItem.ItemPositionHasChanged:
            ___ edge __ edgeList:
                edge.adjust()
            graph.itemMoved()

        r_ s__(Node, self).itemChange(change, value)

    ___ mousePressEvent  event):
        update()
        s__(Node, self).mousePressEvent(event)

    ___ mouseReleaseEvent  event):
        update()
        s__(Node, self).mouseReleaseEvent(event)


c_ GraphWidget(QGraphicsView):
    ___  - 
        s__(GraphWidget, self). - ()

        timerId _ 0

        scene _ QGraphicsScene
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.setSceneRect(-200, -200, 400, 400)
        setScene(scene)
        setCacheMode(QGraphicsView.CacheBackground)
        setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        setRenderHint(QPainter.Antialiasing)
        setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        setResizeAnchor(QGraphicsView.AnchorViewCenter)

        node1 _ Node
        node2 _ Node
        node3 _ Node
        node4 _ Node
        centerNode _ Node
        node6 _ Node
        node7 _ Node
        node8 _ Node
        node9 _ Node
        scene.aI..(node1)
        scene.aI..(node2)
        scene.aI..(node3)
        scene.aI..(node4)
        scene.aI..(centerNode)
        scene.aI..(node6)
        scene.aI..(node7)
        scene.aI..(node8)
        scene.aI..(node9)
        scene.aI..(Edge(node1, node2))
        scene.aI..(Edge(node2, node3))
        scene.aI..(Edge(node2, centerNode))
        scene.aI..(Edge(node3, node6))
        scene.aI..(Edge(node4, node1))
        scene.aI..(Edge(node4, centerNode))
        scene.aI..(Edge(centerNode, node6))
        scene.aI..(Edge(centerNode, node8))
        scene.aI..(Edge(node6, node9))
        scene.aI..(Edge(node7, node4))
        scene.aI..(Edge(node8, node7))
        scene.aI..(Edge(node9, node8))

        node1.setPos(-50, -50)
        node2.setPos(0, -50)
        node3.setPos(50, -50)
        node4.setPos(-50, 0)
        centerNode.setPos(0, 0)
        node6.setPos(50, 0)
        node7.setPos(-50, 50)
        node8.setPos(0, 50)
        node9.setPos(50, 50)

        scale(0.8, 0.8)
        sMS..(400, 400)
        sWT..("Elastic Nodes")

    ___ itemMoved
        __ no. timerId:
            timerId _ startTimer(1000 / 25)

    ___ keyPressEvent  event):
        key _ event.key()

        __ key __ __.Key_Up:
            centerNode.moveBy(0, -20)
        ____ key __ __.Key_Down:
            centerNode.moveBy(0, 20)
        ____ key __ __.Key_Left:
            centerNode.moveBy(-20, 0)
        ____ key __ __.Key_Right:
            centerNode.moveBy(20, 0)
        ____ key __ __.Key_Plus:
            scaleView(1.2)
        ____ key __ __.Key_Minus:
            scaleView(1 / 1.2)
        ____ key __ __.Key_Space or key __ __.Key_Enter:
            ___ item __ scene().i..
                __ isinstance(item, Node):
                    item.setPos(-150 + qrand() % 300, -150 + qrand() % 300)
        ____
            s__(GraphWidget, self).keyPressEvent(event)

    ___ timerEvent  event):
        nodes _ [item ___ item __ scene().i..() __ isinstance(item, Node)]

        ___ node __ nodes:
            node.calculateForces()

        itemsMoved _ F..
        ___ node __ nodes:
            __ node.advance
                itemsMoved _ T..

        __ no. itemsMoved:
            killTimer(timerId)
            timerId _ 0

    ___ wheelEvent  event):
        scaleView(m__.pow(2.0, -event.angleDelta().y() / 240.0))

    ___ drawBackground  painter, rect):
        # Shadow.
        sceneRect _ sceneRect()
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
        painter.fillRect(rect.intersected(sceneRect), ?B..(gradient))
        painter.sB..(__.NoBrush)
        painter.drawRect(sceneRect)

        # Text.
        textRect _ QRectF(sceneRect.left() + 4, sceneRect.top() + 4,
                sceneRect.width() - 4, sceneRect.height() - 4)
        message _ "Click and drag the nodes around, and zoom with the " \
                "mouse wheel or the '+' and '-' keys"

        font _ painter.font()
        font.setBold( st.
        font.sPS..(14)
        painter.sF..(font)
        painter.sP..(__.lightGray)
        painter.drawText(textRect.translated(2, 2), message)
        painter.sP..(__.black)
        painter.drawText(textRect, message)

    ___ scaleView  scaleFactor):
        factor _ transform().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()

        __ factor < 0.07 or factor > 100:
            r_

        scale(scaleFactor, scaleFactor)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    qsrand(?T..(0,0,0).secsTo(?T...currentTime()))

    widget _ GraphWidget()
    widget.s..

    ___.e.. ?.e..
