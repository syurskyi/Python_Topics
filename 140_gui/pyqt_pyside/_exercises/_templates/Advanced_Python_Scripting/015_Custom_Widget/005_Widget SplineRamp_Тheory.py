____ PySide.?C.. _____ _
____ PySide.?G.. _____ _

c_ splineRampWidget(?W..
    ___  -
        super(splineRampWidget, self). - 
        resize(300, 200)

        lineWidth _ 3
        pointSize _ 10

        point1 _ QPointF(0, 0)
        point2 _ QPointF(300, 200)

        factor1 _ 0.0
        factor2 _ 1.0

        dragged _ None

        region1 _ QRect
        region2 _ QRect
        regionSize _ 40
        updateRegions

    ___ updateRegions
        region1 _ QRect(0, 0, regionSize, regionSize)
        region1.moveCenter(point1.toPoint())

        region2 _ QRect(0, 0, regionSize, regionSize)
        region2.moveCenter(point2.toPoint())

        factor1 _ point1.y / fl..(size.height())
        factor2 _ point2.y / fl..(size.height())
        print factor1, factor2

    ___ paintEvent , event
        rec _ event.rect
        painter _ QPainter
        painter.begin
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect, Qt.black)
        path _ QPainterPath
        path.moveTo(point1)
        path.cubicTo(rec.width/2, point1.y,
                     rec.width/2, point2.y,
                     rec.width, point2.y())
        painter.setPen(QPen(QBrush(Qt.white), lineWidth))
        painter.drawPath(path)
        painter.setBrush(QBrush(Qt.white))

        painter.drawEllipse(point1, pointSize, pointSize)
        painter.drawEllipse(point2, pointSize, pointSize)

        painter.setPen(QPen(QBrush(Qt.white), 1))
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(region1)
        painter.drawRect(region2)
        painter.end

    ___ mousePressEvent , event
        # print self.region1.contains(event.pos())
        __ region1.contains(event.pos()):
            dragged _ point1
        elif region2.contains(event.pos()):
            dragged _ point2
        super(splineRampWidget, self).mousePressEvent(event)

    ___ mouseMoveEvent , event
        # print self.dragged
        __ not dragged is None:
            y _ event.pos.y
            s _ size
            dragged.setY(min(max(y, 1), s.height()))
            update
        super(splineRampWidget, self).mouseMoveEvent(event)

    ___ mouseReleaseEvent , event
        dragged _ None
        updateRegions
        update
        super(splineRampWidget, self).mouseReleaseEvent(event)

    ___ resizeEvent , event

        point1.setY(event.size.height * factor1)
        point2.setY(event.size.height * factor2)
        point2.setX(event.size.width())
        updateRegions
        update
        super(splineRampWidget, self).resizeEvent(event)

__ __name__ __ '__main__':
    app _ ?A..([])
    w _ splineRampWidget
    w.s..
    app.exec_