"""
Tankity-tank-tank-tank

Example program for Qt Animation using QGraphicsScene
"""

______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtGui as qtg
____ ? ______ QtCore as qtc

SCREEN_WIDTH _ 800
SCREEN_HEIGHT _ 600
BORDER_HEIGHT _ 100


class Bullet(qtw.QGraphicsObject):

    # arguments are the tank and the bullet
    hit _ qtc.pyqtSignal()

    ___ __init__(self, y_pos, up_True):
        super().__init__()
        self.up _ up
        self.y_pos _ y_pos

        # For fun, let's blur the object
        blur _ qtw.QGraphicsBlurEffect()
        blur.setBlurRadius(10)
        blur.setBlurHints(
            qtw.QGraphicsBlurEffect.AnimationHint)
        self.setGraphicsEffect(blur)

        # Animate the object
        self.animation _ qtc.QPropertyAnimation(self, b'y')
        self.animation.setStartValue(y_pos)
        end _ 0 if up else SCREEN_HEIGHT
        self.animation.setEndValue(end)
        self.animation.setDuration(1000)
        self.yChanged.c..(self.check_collision)

    ___ boundingRect(self):
        # Must be defined for collision detection
        return qtc.QRectF(0, 0, 10, 10)

    ___ paint(self, painter, options, widget):
        painter.setBrush(qtg.QBrush(qtg.QColor('yellow')))
        painter.drawRect(0, 0, 10, 10)

    ___ shoot(self, x_pos):
        self.animation.stop()
        self.setPos(x_pos, self.y_pos)
        self.animation.start()

    ___ check_collision(self):
        colliding_items _ self.collidingItems()
        if colliding_items:
            self.scene().removeItem(self)
            for item in colliding_items:
                if type(item).__name__ == 'Tank':
                    self.hit.emit()


class Tank(qtw.QGraphicsObject):

    #  An 8x8 bitmap of the tank shape
    TANK_BM _ b'\x18\x18\xFF\xFF\xFF\xFF\xFF\x66'
    BOTTOM, TOP _ 0, 1

    ___ __init__(self, color, y_pos, side_TOP):
        super().__init__()
        self.side _ side
        # Define the tank's lookp
        self.bitmap _ qtg.QBitmap.fromData(qtc.QSize(8, 8), self.TANK_BM)
        transform _ qtg.QTransform()
        transform.scale(4, 4)  # scale to 32x32
        if self.side == self.TOP:  # We're pointing down
            transform.rotate(180)
        self.bitmap _ self.bitmap.transformed(transform)
        self.pen _ qtg.QPen(qtg.QColor(color))

        # Define the tank's position
        if self.side == self.BOTTOM:
            y_pos -_ self.bitmap.height()
        self.setPos(0, y_pos)

        # Move the tank
        self.animation _ qtc.QPropertyAnimation(self, b'x')
        self.animation.setStartValue(0)
        self.animation.setEndValue(SCREEN_WIDTH - self.bitmap.width())
        self.animation.setDuration(2000)
        self.animation.finished.c..(self.toggle_direction)
        if self.side == self.TOP:
            self.toggle_direction()
        self.animation.start()

        # create a bullet
        bullet_y _ (
            y_pos - self.bitmap.height()
            if self.side == self.BOTTOM
            else y_pos + self.bitmap.height()
        )
        self.bullet _ Bullet(bullet_y, self.side == self.BOTTOM)

    ___ boundingRect(self):
        # Must be defined for collision detection
        return qtc.QRectF(0, 0, self.bitmap.width(), self.bitmap.height())

    ___ paint(self, painter, option, widget):
        painter.setPen(self.pen)
        painter.drawPixmap(0, 0, self.bitmap)

    ___ toggle_direction(self):
        if self.animation.direction() == qtc.QPropertyAnimation.Forward:
            self.left()
        else:
            self.right()

    ___ right(self):
        self.animation.setDirection(qtc.QPropertyAnimation.Forward)
        self.animation.start()

    ___ left(self):
        self.animation.setDirection(qtc.QPropertyAnimation.Backward)
        self.animation.start()

    ___ shoot(self):
        if not self.bullet.scene
            self.scene().addItem(self.bullet)
        self.bullet.shoot(self.x())


class Scene(qtw.QGraphicsScene):

    ___ __init__(self):
        super().__init__()
        self.setBackgroundBrush(qtg.QBrush(qtg.QColor('black')))
        self.setSceneRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        # add a drawn item
        wall_brush _ qtg.QBrush(qtg.QColor('blue'), qtc.Qt.Dense5Pattern)
        floor _ self.addRect(
            qtc.QRectF(0, SCREEN_HEIGHT - BORDER_HEIGHT,
                       SCREEN_WIDTH, BORDER_HEIGHT),
            brush_wall_brush)
        ceiling _ self.addRect(
            qtc.QRectF(0, 0, SCREEN_WIDTH, BORDER_HEIGHT),
            brush_wall_brush)


        # Show scores
        self.top_score _ 0
        self.bottom_score _ 0
        score_font _ qtg.QFont('Sans', 32)
        self.top_score_display _ self.addText(
            str(self.top_score), score_font)
        self.top_score_display.setPos(10, 10)
        self.bottom_score_display _ self.addText(
            str(self.bottom_score), score_font)
        self.bottom_score_display.setPos(
            SCREEN_WIDTH - 60, SCREEN_HEIGHT - 60)

        # Draw the tanks
        self.bottom_tank _ Tank(
            'red', floor.rect().top(), Tank.BOTTOM)
        self.addItem(self.bottom_tank)

        self.top_tank _ Tank(
            'green', ceiling.rect().bottom(), Tank.TOP)
        self.addItem(self.top_tank)

        # Connect the bullet hits
        self.top_tank.bullet.hit.c..(self.top_score_increment)
        self.bottom_tank.bullet.hit.c..(self.bottom_score_increment)

    ___ top_score_increment(self):
        self.top_score +_ 1
        self.top_score_display.setPlainText(str(self.top_score))

    ___ bottom_score_increment(self):
        self.bottom_score +_ 1
        self.bottom_score_display.setPlainText(str(self.bottom_score))

    ___ keyPressEvent(self, event):
        keymap _ {
            qtc.Qt.Key_Right: self.bottom_tank.right,
            qtc.Qt.Key_Left: self.bottom_tank.left,
            qtc.Qt.Key_Return: self.bottom_tank.shoot,
            qtc.Qt.Key_A: self.top_tank.left,
            qtc.Qt.Key_D: self.top_tank.right,
            qtc.Qt.Key_Space: self.top_tank.shoot
        }
        callback _ keymap.get(event.key())
        if callback:
            callback()


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        self.resize(qtc.QSize(SCREEN_WIDTH, SCREEN_HEIGHT))
        # Basic setup
        self.scene _ Scene()
        view _ qtw.QGraphicsView(self.scene)
        self.setCentralWidget(view)
        # End main UI code
        self.s..


if __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
