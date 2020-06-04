#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
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

____ ?.?C.. ______ pyqtSlot, Q_CLASSINFO, QRectF, __
____ ?.?G.. ______ ?B.., QPainter, QTransform
____ ?.?W.. ______ (?A.., QGraphicsItem, QGraphicsObject,
        QGraphicsScene, QGraphicsView)
____ ?.QtDBus ______ QDBusAbstractAdaptor, QDBusConnection


c_ Car(QGraphicsObject):

    ___  -
        s__(Car, self). - ()

        color _ ?B..(__.green)
        wheelsAngle _ 0.0
        speed _ 0.0

        startTimer(1000 // 33)
        setFlag(QGraphicsItem.ItemIsMovable,  st.
        setFlag(QGraphicsItem.ItemIsFocusable,  st.

    ___ accelerate 
        __ speed < 10:
            speed +_ 1

    ___ decelerate 
        __ speed > -10:
            speed -_ 1

    ___ turnLeft 
        __ wheelsAngle > -30:
            wheelsAngle -_ 5

    ___ turnRight 
        __ wheelsAngle < 30:
            wheelsAngle +_ 5

    ___ boundingRect 
        r_ QRectF(-35, -81, 70, 115)

    ___ timerEvent  event):
        axelDistance _ 54.0
        wheelsAngleRads _ (wheelsAngle * m__.pi) / 180
        turnDistance _ m__.cos(wheelsAngleRads) * axelDistance * 2
        turnRateRads _ wheelsAngleRads / turnDistance
        turnRate _ (turnRateRads * 180) / m__.pi
        rotation _ speed * turnRate

        setTransform(QTransform().rotate(rotation),  st.
        setTransform(QTransform.fromTranslate(0, -speed),  st.
        update()

    ___ paint  painter, option, widget):
        painter.sB..(__.gray)
        painter.drawRect(-20, -58, 40, 2)       # Front axel
        painter.drawRect(-20, 7, 40, 2)         # Rear axel

        painter.sB..(color)
        painter.drawRect(-25, -79, 50, 10)      # Front wing

        painter.drawEllipse(-25, -48, 50, 20)   # Side pods
        painter.drawRect(-25, -38, 50, 35)      # Side pods
        painter.drawRect(-5, 9, 10, 10)         # Back pod

        painter.drawEllipse(-10, -81, 20, 100)  # Main body

        painter.drawRect(-17, 19, 34, 15)       # Rear wing

        painter.sB..(__.black)
        painter.drawPie(-5, -51, 10, 15, 0, 180 * 16)
        painter.drawRect(-5, -44, 10, 10)       # Cockpit

        painter.save()
        painter.translate(-20, -58)
        painter.rotate(wheelsAngle)
        painter.drawRect(-10, -7, 10, 15)       # Front left
        painter.restore()

        painter.save()
        painter.translate(20, -58)
        painter.rotate(wheelsAngle)
        painter.drawRect(0, -7, 10, 15)         # Front right
        painter.restore()

        painter.drawRect(-30, 0, 12, 17)        # Rear left
        painter.drawRect(19, 0, 12, 17)         # Rear right


c_ CarInterfaceAdaptor(QDBusAbstractAdaptor):

    Q_CLASSINFO("D-Bus Interface", 'org.example.Examples.CarInterface')

    Q_CLASSINFO("D-Bus Introspection", ''
            '  <interface name="org.example.Examples.CarInterface">\n'
            '    <method name="accelerate"/>\n'
            '    <method name="decelerate"/>\n'
            '    <method name="turnLeft"/>\n'
            '    <method name="turnRight"/>\n'
            '  </interface>\n'
            '')

    ___  -   parent):
        s__(CarInterfaceAdaptor, self). - (parent)

        setAutoRelaySignals( st.

    @pyqtSlot()
    ___ accelerate 
        parent().accelerate()

    @pyqtSlot()
    ___ decelerate 
        parent().decelerate()

    @pyqtSlot()
    ___ turnLeft 
        parent().turnLeft()

    @pyqtSlot()
    ___ turnRight 
        parent().turnRight()


__ ______ __ ______
    ______ ___

    app _ ?A..(___.a..

    scene _ QGraphicsScene()
    scene.setSceneRect(-500, -500, 1000, 1000)
    scene.setItemIndexMethod(QGraphicsScene.NoIndex)

    car _ Car()
    scene.aI..(car)

    view _ QGraphicsView(scene)
    view.setRenderHint(QPainter.Antialiasing)
    view.setBackgroundBrush(__.darkGray)
    view.sWT..("Qt DBus Controlled Car")
    view.r..(400, 300)
    view.s..

    a _ CarInterfaceAdaptor(car)
    connection _ QDBusConnection.sessionBus()
    connection.registerObject('/Car', car)
    connection.registerService('org.example.CarExample')

    rc _ app.e..

    # Make sure things get destroyed in the right order.
    del view

    ___.e..(rc)
