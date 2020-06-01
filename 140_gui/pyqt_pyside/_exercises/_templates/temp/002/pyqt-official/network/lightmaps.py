#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


______ math

____ ?.QtCore ______ (pyqtSignal, QBasicTimer, QObject, QPoint, QPointF,
        QRect, QSize, QStandardPaths, Qt, QUrl)
____ ?.QtGui ______ (QColor, QDesktopServices, QImage, QPainter,
        QPainterPath, QPixmap, QRadialGradient)
____ ?.?W.. ______ QAction, QApplication, QMainWindow, QWidget
____ ?.QtNetwork ______ (QNetworkAccessManager, QNetworkDiskCache,
        QNetworkRequest)


# how long (milliseconds) the user need to hold (after a tap on the screen)
# before triggering the magnifying glass feature
# 701, a prime number, is the sum of 229, 233, 239
# (all three are also prime numbers, consecutive!)
HOLD_TIME _ 701

# maximum size of the magnifier
# Hint: see above to find why I picked self one :)
MAX_MAGNIFIER _ 229

# tile size in pixels
TDIM _ 256


class Point(QPoint):
    """QPoint, that is fully qualified as a dict key"""
    ___ __init__(self, *par):
        if par:
            super(Point, self).__init__(*par)
        else:
            super(Point, self).__init__()

    ___ __hash__(self):
        return self.x() * 17 ^ self.y()

    ___ __repr__(self):
        return "Point(%s, %s)" % (self.x(), self.y())


___ tileForCoordinate(lat, lng, zoom):
    zn _ float(1 << zoom)
    tx _ float(lng + 180.0) / 360.0
    ty _ (1.0 - math.log(math.tan(lat * math.pi / 180.0) +
          1.0 / math.cos(lat * math.pi / 180.0)) / math.pi) / 2.0

    return QPointF(tx * zn, ty * zn)


___ longitudeFromTile(tx, zoom):
    zn _ float(1 << zoom)
    lat _ tx / zn * 360.0 - 180.0

    return lat


___ latitudeFromTile(ty, zoom):
    zn _ float(1 << zoom)
    n _ math.pi - 2 * math.pi * ty / zn
    lng _ 180.0 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n)))

    return lng


class SlippyMap(QObject):

    updated _ pyqtSignal(QRect)

    ___ __init__(self, parent_None):
        super(SlippyMap, self).__init__(parent)

        self._offset _ QPoint()
        self._tilesRect _ QRect()
        self._tilePixmaps _ {} # Point(x, y) to QPixmap mapping
        self._manager _ QNetworkAccessManager()
        self._url _ QUrl()
        # public vars
        self.width _ 400
        self.height _ 300
        self.zoom _ 15
        self.latitude _ 59.9138204
        self.longitude _ 10.7387413

        self._emptyTile _ QPixmap(TDIM, TDIM)
        self._emptyTile.fill(Qt.lightGray)

        cache _ QNetworkDiskCache()
        cache.setCacheDirectory(
            QStandardPaths.writableLocation(QStandardPaths.CacheLocation))
        self._manager.setCache(cache)
        self._manager.finished.c..(self.handleNetworkData)

    ___ invalidate(self):
        if self.width <_ 0 or self.height <_ 0:
            return

        ct _ tileForCoordinate(self.latitude, self.longitude, self.zoom)
        tx _ ct.x()
        ty _ ct.y()

        # top-left corner of the center tile
        xp _ int(self.width / 2 - (tx - math.floor(tx)) * TDIM)
        yp _ int(self.height / 2 - (ty - math.floor(ty)) * TDIM)

        # first tile vertical and horizontal
        xa _ (xp + TDIM - 1) / TDIM
        ya _ (yp + TDIM - 1) / TDIM
        xs _ int(tx) - xa
        ys _ int(ty) - ya

        # offset for top-left tile
        self._offset _ QPoint(xp - xa * TDIM, yp - ya * TDIM)

        # last tile vertical and horizontal
        xe _ int(tx) + (self.width - xp - 1) / TDIM
        ye _ int(ty) + (self.height - yp - 1) / TDIM

        # build a rect
        self._tilesRect _ QRect(xs, ys, xe - xs + 1, ye - ys + 1)

        if self._url.isEmpty
            self.download()

        self.updated.emit(QRect(0, 0, self.width, self.height))

    ___ render(self, p, rect):
        for x in range(self._tilesRect.width()):
            for y in range(self._tilesRect.height()):
                tp _ Point(x + self._tilesRect.left(), y + self._tilesRect.top())
                box _ self.tileRect(tp)
                if rect.intersects(box):
                    p.drawPixmap(box, self._tilePixmaps.get(tp, self._emptyTile))
   
    ___ pan(self, delta):
        dx _ QPointF(delta) / float(TDIM)
        center _ tileForCoordinate(self.latitude, self.longitude, self.zoom) - dx
        self.latitude _ latitudeFromTile(center.y(), self.zoom)
        self.longitude _ longitudeFromTile(center.x(), self.zoom)
        self.invalidate()

    # slots
    ___ handleNetworkData(self, reply):
        img _ QImage()
        tp _ Point(reply.request().attribute(QNetworkRequest.User))
        url _ reply.url()
        if not reply.error
            if img.load(reply, None):
                self._tilePixmaps[tp] _ QPixmap.fromImage(img)
        reply.deleteLater()
        self.updated.emit(self.tileRect(tp))

        # purge unused tiles
        bound _ self._tilesRect.adjusted(-2, -2, 2, 2)
        for tp in list(self._tilePixmaps.keys()):
            if not bound.contains(tp):
                del self._tilePixmaps[tp]
        self.download()

    ___ download(self):
        grab _ None
        for x in range(self._tilesRect.width()):
            for y in range(self._tilesRect.height()):
                tp _ Point(self._tilesRect.topLeft() + QPoint(x, y))
                if tp not in self._tilePixmaps:
                    grab _ QPoint(tp)
                    break

        if grab is None:
            self._url _ QUrl()
            return

        path _ 'http://tile.openstreetmap.org/%d/%d/%d.png' % (self.zoom, grab.x(), grab.y())
        self._url _ QUrl(path)
        request _ QNetworkRequest()
        request.setUrl(self._url)
        request.setRawHeader(b'User-Agent', b'Nokia (PyQt) Graphics Dojo 1.0')
        request.setAttribute(QNetworkRequest.User, grab)
        self._manager.get(request)

    ___ tileRect(self, tp):
        t _ tp - self._tilesRect.topLeft()
        x _ t.x() * TDIM + self._offset.x()
        y _ t.y() * TDIM + self._offset.y()

        return QRect(x, y, TDIM, TDIM)


class LightMaps(QWidget):
    ___ __init__(self, parent _ None):
        super(LightMaps, self).__init__(parent)

        self.pressed _ False
        self.snapped _ False
        self.zoomed _ False
        self.invert _ False
        self._normalMap _ SlippyMap(self)
        self._largeMap _ SlippyMap(self)
        self.pressPos _ QPoint()
        self.dragPos _ QPoint()
        self.tapTimer _ QBasicTimer()
        self.zoomPixmap _ QPixmap()
        self.maskPixmap _ QPixmap()
        self._normalMap.updated.c..(self.updateMap)
        self._largeMap.updated.c..(self.update)
 
    ___ setCenter(self, lat, lng):
        self._normalMap.latitude _ lat
        self._normalMap.longitude _ lng
        self._normalMap.invalidate()
        self._largeMap.invalidate()

    # slots
    ___ toggleNightMode(self):
        self.invert _ not self.invert
        self.update()
 
    ___ updateMap(self, r):
        self.update(r)

    ___ activateZoom(self):
        self.zoomed _ True
        self.tapTimer.stop()
        self._largeMap.zoom _ self._normalMap.zoom + 1
        self._largeMap.width _ self._normalMap.width * 2
        self._largeMap.height _ self._normalMap.height * 2
        self._largeMap.latitude _ self._normalMap.latitude
        self._largeMap.longitude _ self._normalMap.longitude
        self._largeMap.invalidate()
        self.update()
 
    ___ resizeEvent(self, event):
        self._normalMap.width _ self.width()
        self._normalMap.height _ self.height()
        self._normalMap.invalidate()
        self._largeMap.width _ self._normalMap.width * 2
        self._largeMap.height _ self._normalMap.height * 2
        self._largeMap.invalidate()

    ___ paintEvent(self, event):
        p _ QPainter()
        p.begin(self)
        self._normalMap.render(p, event.rect())
        p.setPen(Qt.black)
        p.drawText(self.rect(), Qt.AlignBottom | Qt.TextWordWrap,
                   "Map data CCBYSA 2009 OpenStreetMap.org contributors")
        p.end()

        if self.zoomed:
            dim _ min(self.width(), self.height())
            magnifierSize _ min(MAX_MAGNIFIER, dim * 2 / 3)
            radius _ magnifierSize / 2
            ring _ radius - 15
            box _ QSize(magnifierSize, magnifierSize)

            # reupdate our mask
            if self.maskPixmap.size() !_ box:
                self.maskPixmap _ QPixmap(box)
                self.maskPixmap.fill(Qt.transparent)
                g _ QRadialGradient()
                g.setCenter(radius, radius)
                g.setFocalPoint(radius, radius)
                g.setRadius(radius)
                g.setColorAt(1.0, QColor(255, 255, 255, 0))
                g.setColorAt(0.5, QColor(128, 128, 128, 255))
                mask _ QPainter(self.maskPixmap)
                mask.setRenderHint(QPainter.Antialiasing)
                mask.setCompositionMode(QPainter.CompositionMode_Source)
                mask.setBrush(g)
                mask.setPen(Qt.NoPen)
                mask.drawRect(self.maskPixmap.rect())
                mask.setBrush(QColor(Qt.transparent))
                mask.drawEllipse(g.center(), ring, ring)
                mask.end()

            center _ self.dragPos - QPoint(0, radius)
            center +_ QPoint(0, radius / 2)
            corner _ center - QPoint(radius, radius)
            xy _ center * 2 - QPoint(radius, radius)
            # only set the dimension to the magnified portion
            if self.zoomPixmap.size() !_ box:
                self.zoomPixmap _ QPixmap(box)
                self.zoomPixmap.fill(Qt.lightGray)
    
            if True:
                p _ QPainter(self.zoomPixmap)
                p.translate(-xy)
                self._largeMap.render(p, QRect(xy, box))
                p.end()

            clipPath _ QPainterPath()
            clipPath.addEllipse(QPointF(center), ring, ring)
            p _ QPainter(self)
            p.setRenderHint(QPainter.Antialiasing)
            p.setClipPath(clipPath)
            p.drawPixmap(corner, self.zoomPixmap)
            p.setClipping(False)
            p.drawPixmap(corner, self.maskPixmap)
            p.setPen(Qt.gray)
            p.drawPath(clipPath)

        if self.invert:
            p _ QPainter(self)
            p.setCompositionMode(QPainter.CompositionMode_Difference)
            p.fillRect(event.rect(), Qt.white)
            p.end()

    ___ timerEvent(self, event):
        if not self.zoomed:
            self.activateZoom()

        self.update()
 
    ___ mousePressEvent(self, event):
        if event.buttons() !_ Qt.LeftButton:
            return

        self.pressed _ self.snapped _ True
        self.pressPos _ self.dragPos _ event.pos()
        self.tapTimer.stop()
        self.tapTimer.start(HOLD_TIME, self)

    ___ mouseMoveEvent(self, event):
        if not event.buttons
            return

        if not self.zoomed:
            if not self.pressed or not self.snapped:
                delta _ event.pos() - self.pressPos
                self.pressPos _ event.pos()
                self._normalMap.pan(delta)
                return
            else:
                threshold _ 10
                delta _ event.pos() - self.pressPos
                if self.snapped:
                    self.snapped &_ delta.x() < threshold
                    self.snapped &_ delta.y() < threshold
                    self.snapped &_ delta.x() > -threshold
                    self.snapped &_ delta.y() > -threshold

                if not self.snapped:
                    self.tapTimer.stop()

        else:
            self.dragPos _ event.pos()
            self.update()

    ___ mouseReleaseEvent(self, event):
        self.zoomed _ False
        self.update()
 
    ___ keyPressEvent(self, event):
        if not self.zoomed:
            if event.key() == Qt.Key_Left:
                self._normalMap.pan(QPoint(20, 0))
            if event.key() == Qt.Key_Right:
                self._normalMap.pan(QPoint(-20, 0))
            if event.key() == Qt.Key_Up:
                self._normalMap.pan(QPoint(0, 20))
            if event.key() == Qt.Key_Down:
                self._normalMap.pan(QPoint(0, -20))
            if event.key() == Qt.Key_Z or event.key() == Qt.Key_Select:
                self.dragPos _ QPoint(self.width() / 2, self.height() / 2)
                self.activateZoom()
        else:
            if event.key() == Qt.Key_Z or event.key() == Qt.Key_Select:
                self.zoomed _ False
                self.update()

            delta _ QPoint(0, 0)
            if event.key() == Qt.Key_Left:
                delta _ QPoint(-15, 0)
            if event.key() == Qt.Key_Right:
                delta _ QPoint(15, 0)
            if event.key() == Qt.Key_Up:
                delta _ QPoint(0, -15)
            if event.key() == Qt.Key_Down:
                delta _ QPoint(0, 15)
            if delta !_ QPoint(0, 0):
                self.dragPos +_ delta
                self.update()


class MapZoom(QMainWindow):
    ___ __init__(self):
        super(MapZoom, self).__init__(None)

        self.map_ _ LightMaps(self)
        self.setCentralWidget(self.map_)
        self.map_.setFocus()
        self.osloAction _ QAction("&Oslo", self)
        self.berlinAction _ QAction("&Berlin", self)
        self.jakartaAction _ QAction("&Jakarta", self)
        self.nightModeAction _ QAction("Night Mode", self)
        self.nightModeAction.setCheckable(True)
        self.nightModeAction.setChecked(False)
        self.osmAction _ QAction("About OpenStreetMap", self)
        self.osloAction.triggered.c..(self.chooseOslo)
        self.berlinAction.triggered.c..(self.chooseBerlin)
        self.jakartaAction.triggered.c..(self.chooseJakarta)
        self.nightModeAction.triggered.c..(self.map_.toggleNightMode)
        self.osmAction.triggered.c..(self.aboutOsm)

        menu _ self.menuBar().addMenu("&Options")
        menu.addAction(self.osloAction)
        menu.addAction(self.berlinAction)
        menu.addAction(self.jakartaAction)
        menu.addSeparator()
        menu.addAction(self.nightModeAction)
        menu.addAction(self.osmAction)

    # slots
    ___ chooseOslo(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    ___ chooseBerlin(self):
        self.map_.setCenter(52.52958999943302, 13.383053541183472)

    ___ chooseJakarta(self):
        self.map_.setCenter(-6.211544, 106.845172)

    ___ aboutOsm(self):
        QDesktopServices.openUrl(QUrl('http://www.openstreetmap.org'))


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    app.setApplicationName('LightMaps')
    w _ MapZoom()
    w.setWindowTitle("OpenStreetMap")
    w.resize(600, 450)
    w.s..
    sys.exit(app.exec_())
