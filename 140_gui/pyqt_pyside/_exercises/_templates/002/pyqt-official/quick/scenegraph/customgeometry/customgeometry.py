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


____ ?.?C.. ______ pP.., pS.., QPointF, ?U..
____ ?.?G.. ______ ?C.., QGuiApplication
____ ?.QtQml ______ qmlRegisterType
____ ?.QtQuick ______ (QQuickItem, QQuickView, QSGFlatColorMaterial,
        QSGGeometry, QSGGeometryNode, QSGNode)

______ customgeometry_rc


c_ BezierCurve(QQuickItem):

    p1Changed _ pS..(QPointF)

    @pP..(QPointF, notify_p1Changed)
    ___ p1
        r_ _p1

    @p1.setter
    ___ p1  p):
        __ _p1 !_ p:
            _p1 _ QPointF(p)
            p1Changed.e..(p)
            update()

    p2Changed _ pS..(QPointF)

    @pP..(QPointF, notify_p2Changed)
    ___ p2
        r_ _p2

    @p2.setter
    ___ p2  p):
        __ _p2 !_ p:
            _p2 _ QPointF(p)
            p2Changed.e..(p)
            update()

    p3Changed _ pS..(QPointF)

    @pP..(QPointF, notify_p3Changed)
    ___ p3
        r_ _p3

    @p3.setter
    ___ p3  p):
        __ _p3 !_ p:
            _p3 _ QPointF(p)
            p3Changed.e..(p)
            update()

    p4Changed _ pS..(QPointF)

    @pP..(QPointF, notify_p4Changed)
    ___ p4
        r_ _p4

    @p4.setter
    ___ p4  p):
        __ _p4 !_ p:
            _p4 _ QPointF(p)
            p4Changed.e..(p)
            update()

    segmentCountChanged _ pS..(in.)

    @pP..(in., notify_segmentCountChanged)
    ___ segmentCount
        r_ _segmentCount

    @segmentCount.setter
    ___ segmentCount  count):
        __ _segmentCount !_ count:
            _segmentCount _ count
            segmentCountChanged.e..(count)
            update()

    ___  -   parent_None):
        s__(BezierCurve, self). - (parent)

        _p1 _ QPointF(0, 0)
        _p2 _ QPointF(1, 0)
        _p3 _ QPointF(0, 1)
        _p4 _ QPointF(1, 1)

        _segmentCount _ 32

        _root_node _ N..

        setFlag(QQuickItem.ItemHasContents,  st.

    ___ updatePaintNode  oldNode, nodeData):
        __ _root_node __ N..:
            _root_node _ QSGGeometryNode()

            geometry _ QSGGeometry(QSGGeometry.defaultAttributes_Point2D(),
                    _segmentCount)
            geometry.setLineWidth(2)
            geometry.setDrawingMode(QSGGeometry.GL_LINE_STRIP)
            _root_node.setGeometry(geometry)
            _root_node.setFlag(QSGNode.OwnsGeometry)

            material _ QSGFlatColorMaterial()
            material.sC..(?C..(255, 0, 0))
            _root_node.setMaterial(material)
            _root_node.setFlag(QSGNode.OwnsMaterial)
        ____
            geometry _ _root_node.geometry()
            geometry.allocate(_segmentCount)

        w _ width()
        h _ height()
        vertices _ geometry.vertexDataAsPoint2D()

        ___ i __ ra..(_segmentCount):
            t _ i / fl..(_segmentCount - 1)
            invt _ 1 - t

            pos _ invt * invt * invt * _p1 \
                    + 3 * invt * invt * t * _p2 \
                    + 3 * invt * t * t * _p3 \
                    + t * t * t * _p4

            vertices[i].set(pos.x() * w, pos.y() * h)

        _root_node.markDirty(QSGNode.DirtyGeometry)

        r_ _root_node


__ ______ __ ______
    ______ ___

    app _ QGuiApplication(___.a..

    qmlRegisterType(BezierCurve, "CustomGeometry", 1, 0, "BezierCurve")

    view _ QQuickView()
    f.. _ view.f..()
    f...setSamples(16)
    view.setFormat(f..)

    view.setSource(?U..('qrc:///scenegraph/customgeometry/main.qml'))
    view.s..

    ___.e.. ?.e..
