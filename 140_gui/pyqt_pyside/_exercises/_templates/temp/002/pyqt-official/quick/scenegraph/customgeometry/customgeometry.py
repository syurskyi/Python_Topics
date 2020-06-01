#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
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
##   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
##     of its contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
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


____ ?.QtCore ______ pyqtProperty, pyqtSignal, QPointF, QUrl
____ ?.?G.. ______ QColor, QGuiApplication
____ ?.QtQml ______ qmlRegisterType
____ ?.QtQuick ______ (QQuickItem, QQuickView, QSGFlatColorMaterial,
        QSGGeometry, QSGGeometryNode, QSGNode)

______ customgeometry_rc


c_ BezierCurve(QQuickItem):

    p1Changed _ pyqtSignal(QPointF)

    @pyqtProperty(QPointF, notify_p1Changed)
    ___ p1(self):
        r_ self._p1

    @p1.setter
    ___ p1  p):
        __ self._p1 !_ p:
            self._p1 _ QPointF(p)
            self.p1Changed.emit(p)
            self.update()

    p2Changed _ pyqtSignal(QPointF)

    @pyqtProperty(QPointF, notify_p2Changed)
    ___ p2(self):
        r_ self._p2

    @p2.setter
    ___ p2  p):
        __ self._p2 !_ p:
            self._p2 _ QPointF(p)
            self.p2Changed.emit(p)
            self.update()

    p3Changed _ pyqtSignal(QPointF)

    @pyqtProperty(QPointF, notify_p3Changed)
    ___ p3(self):
        r_ self._p3

    @p3.setter
    ___ p3  p):
        __ self._p3 !_ p:
            self._p3 _ QPointF(p)
            self.p3Changed.emit(p)
            self.update()

    p4Changed _ pyqtSignal(QPointF)

    @pyqtProperty(QPointF, notify_p4Changed)
    ___ p4(self):
        r_ self._p4

    @p4.setter
    ___ p4  p):
        __ self._p4 !_ p:
            self._p4 _ QPointF(p)
            self.p4Changed.emit(p)
            self.update()

    segmentCountChanged _ pyqtSignal(int)

    @pyqtProperty(int, notify_segmentCountChanged)
    ___ segmentCount(self):
        r_ self._segmentCount

    @segmentCount.setter
    ___ segmentCount  count):
        __ self._segmentCount !_ count:
            self._segmentCount _ count
            self.segmentCountChanged.emit(count)
            self.update()

    ___ __init__  parent_None):
        super(BezierCurve, self).__init__(parent)

        self._p1 _ QPointF(0, 0)
        self._p2 _ QPointF(1, 0)
        self._p3 _ QPointF(0, 1)
        self._p4 _ QPointF(1, 1)

        self._segmentCount _ 32

        self._root_node _ N..

        self.setFlag(QQuickItem.ItemHasContents, True)

    ___ updatePaintNode  oldNode, nodeData):
        __ self._root_node __ N..:
            self._root_node _ QSGGeometryNode()

            geometry _ QSGGeometry(QSGGeometry.defaultAttributes_Point2D(),
                    self._segmentCount)
            geometry.setLineWidth(2)
            geometry.setDrawingMode(QSGGeometry.GL_LINE_STRIP)
            self._root_node.setGeometry(geometry)
            self._root_node.setFlag(QSGNode.OwnsGeometry)

            material _ QSGFlatColorMaterial()
            material.setColor(QColor(255, 0, 0))
            self._root_node.setMaterial(material)
            self._root_node.setFlag(QSGNode.OwnsMaterial)
        ____
            geometry _ self._root_node.geometry()
            geometry.allocate(self._segmentCount)

        w _ self.width()
        h _ self.height()
        vertices _ geometry.vertexDataAsPoint2D()

        for i in range(self._segmentCount):
            t _ i / float(self._segmentCount - 1)
            invt _ 1 - t

            pos _ invt * invt * invt * self._p1 \
                    + 3 * invt * invt * t * self._p2 \
                    + 3 * invt * t * t * self._p3 \
                    + t * t * t * self._p4

            vertices[i].set(pos.x() * w, pos.y() * h)

        self._root_node.markDirty(QSGNode.DirtyGeometry)

        r_ self._root_node


__ __name__ == '__main__':
    ______ sys

    app _ QGuiApplication(sys.argv)

    qmlRegisterType(BezierCurve, "CustomGeometry", 1, 0, "BezierCurve")

    view _ QQuickView()
    format _ view.format()
    format.setSamples(16)
    view.setFormat(format)

    view.setSource(QUrl('qrc:///scenegraph/customgeometry/main.qml'))
    view.s..

    sys.exit(app.exec_())
