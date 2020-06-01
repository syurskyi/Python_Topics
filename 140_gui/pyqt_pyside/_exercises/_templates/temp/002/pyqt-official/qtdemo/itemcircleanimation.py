#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
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
______ random

____ ?.QtCore ______ QLineF, QPointF, QRectF, Qt, QTime

____ colors ______ Colors
____ demoitem ______ DemoItem
____ demoitemanimation ______ DemoItemAnimation
____ guidecircle ______ GuideCircle
____ guideline ______ GuideLine
____ letteritem ______ LetterItem


class TickerPostEffect(object):
    ___ tick(self, adjust):
        pass

    ___ transform(self, item, pos):
        pass


class PostRotateXY(TickerPostEffect):
    ___ __init__(self, speedx, speedy, curvx, curvy):
        super(PostRotateXY, self).__init__()

        self.currRotX _ 0.0
        self.currRotY _ 0.0

        self.speedx _ speedx
        self.speedy _ speedy
        self.curvx _ curvx
        self.curvy _ curvy

    ___ tick(self, adjust):
        self.currRotX +_ self.speedx * adjust
        self.currRotY +_ self.speedy * adjust

    ___ transform(self, item, pos):
        parent _ item.parentItem()
        center _ parent.boundingRect().center()
        pos.setX(center.x() + (pos.x() - center.x()) * math.cos(self.currRotX + pos.x() * self.curvx))
        pos.setY(center.y() + (pos.y() - center.y()) * math.cos(self.currRotY + pos.y() * self.curvy))


class PostRotateXYTwist(PostRotateXY):
    ___ transform(self, item, pos):
        parent _ item.parentItem()
        center _ parent.boundingRect().center()
        pos.setX(center.x() + (pos.x() - center.x()) * math.cos(self.currRotX + pos.y() * self.curvx))
        pos.setY(center.y() + (pos.y() - center.y()) * math.cos(self.currRotY + pos.x() * self.curvy))


class TickerEffect(object):
    Normal, Intro, Outro _ range(3)

    ___ __init__(self, letters):
        self.postEffect _ TickerPostEffect()
        self.status _ TickerEffect.Intro
        self.letters _ letters
        self.morphSpeed _ self.normalMorphSpeed _ Colors.tickerMorphSpeed
        self.moveSpeed _ self.normalMoveSpeed _ Colors.tickerMoveSpeed
        self.useSheepDog _ True
        self.morphBetweenModels _ not Colors.noTickerMorph

    ___ setPostEffect(self, effect):
        self.postEffect _ effect

    ___ slowDownAfterIntro(self, adjust):
        if self.morphBetweenModels:
            if self.status == TickerEffect.Intro:
                dec _ 0.1 * adjust
                self.moveSpeed -_ dec
                if self.moveSpeed < Colors.tickerMoveSpeed:
                    self.moveSpeed _ self.normalMoveSpeed
                    self.morphSpeed _ self.normalMorphSpeed
                    self.status _ TickerEffect.Normal

    ___ moveLetters(self, adjust):
        adaptedMoveSpeed _ self.moveSpeed * adjust
        adaptedMorphSpeed _ self.morphSpeed * adjust
        self.postEffect.tick(adjust)

        if self.morphBetweenModels:
            move_speed _ adaptedMoveSpeed
            morph_speed _ adaptedMorphSpeed
        else:
            move_speed _ Colors.tickerMoveSpeed
            morph_speed _ -1

        for letter in self.letters:
            letter.guideAdvance(move_speed)
            letter.guideMove(morph_speed)

            pos _ letter.getGuidedPos()
            self.postEffect.transform(letter, pos)

            if self.useSheepDog:
                letter.setPosUsingSheepDog(pos, QRectF(0, 0, 800, 600))
            else:
                letter.setPos(pos)

    ___ tick(self, adjust):
        self.slowDownAfterIntro(adjust)
        self.moveLetters(adjust)


class EffectWhirlWind(TickerEffect):
    ___ __init__(self, letters):
        super(EffectWhirlWind, self).__init__(letters)

        self.moveSpeed _ 50

        for letter in self.letters:
            letter.setGuidedPos(QPointF(0, 100))


class EffectSnake(TickerEffect):
    ___ __init__(self, letters):
        super(EffectSnake, self).__init__(letters)

        self.moveSpeed _ 40

        for i, letter in enumerate(self.letters):
            letter.setGuidedPos(QPointF(0, -250 - (i * 5)))


class EffectScan(TickerEffect):
    ___ __init__(self, letters):
        super(EffectScan, self).__init__(letters)

        for letter in self.letters:
            letter.setGuidedPos(QPointF(100, -300))


class EffectRaindrops(TickerEffect):
    ___ __init__(self, letters):
        super(EffectRaindrops, self).__init__(letters)

        for letter in self.letters:
            letter.setGuidedPos(QPointF(random.randint(-100, 100),
                    random.randint(-200, 1100)))


class EffectLine(TickerEffect):
    ___ __init__(self, letters):
        super(EffectLine, self).__init__(letters)

        for i, letter in enumerate(self.letters):
            letter.setGuidedPos(QPointF(100, 500 + i * 20))


class ItemCircleAnimation(DemoItem):
    ___ __init__(self, parent_None):
        super(ItemCircleAnimation, self).__init__(parent)

        self.letterList _ []
        self.letterCount _ Colors.tickerLetterCount
        self.scale _ 1.0
        self.showCount _ -1
        self.tickOnPaint _ False
        self.paused _ False
        self.doIntroTransitions _ True
        self.setAcceptHoverEvents(True)
        self.setCursor(Qt.OpenHandCursor)
        self.setupGuides()
        self.setupLetters()
        self.useGuideQt()
        self.effect _ None

        self.mouseMoveLastPosition _ QPointF()
        self.tickTimer _ QTime()

    ___ createLetter(self, c):
        letter _ LetterItem(c, self)
        self.letterList.append(letter)

    ___ setupLetters(self):
        self.letterList _ []

        s _ Colors.tickerText
        tlen _ len(s)
        room _ self.letterCount
        while room >_ tlen:
            for c in s:
                self.createLetter(c)

            room -_ tlen

        # Fill in with blanks.
        while room > 0:
            self.createLetter(' ')
            room -_ 1

    ___ setupGuides(self):
        x _ 0
        y _ 20

        self.qtGuide1 _ GuideCircle(QRectF(x, y, 260, 260), -36, 342)
        GuideLine(QPointF(x + 240, y + 268), self.qtGuide1)
        GuideLine(QPointF(x + 265, y + 246), self.qtGuide1)
        GuideLine(QPointF(x + 158, y + 134), self.qtGuide1)
        GuideLine(QPointF(x + 184, y + 109), self.qtGuide1)
        GuideLine(QPointF(x + 160, y +  82), self.qtGuide1)
        GuideLine(QPointF(x +  77, y + 163), self.qtGuide1)
        GuideLine(QPointF(x + 100, y + 190), self.qtGuide1)
        GuideLine(QPointF(x + 132, y + 159), self.qtGuide1)
        GuideLine(QPointF(x + 188, y + 211), self.qtGuide1)
        GuideCircle(QRectF(x + 30, y + 30, 200, 200), -30, 336, GuideCircle.CW, self.qtGuide1)
        GuideLine(QPointF(x + 238, y + 201), self.qtGuide1)

        y _ 30
        self.qtGuide2 _ GuideCircle(QRectF(x + 30, y + 30, 200, 200), 135, 270, GuideCircle.CCW)
        GuideLine(QPointF(x + 222, y + 38), self.qtGuide2)
        GuideCircle(QRectF(x, y, 260, 260), 135, 270, GuideCircle.CW, self.qtGuide2)
        GuideLine(QPointF(x + 59, y + 59), self.qtGuide2)

        x _ 115
        y _ 10
        self.qtGuide3 _ GuideLine(QLineF(x, y, x + 30, y))
        GuideLine(QPointF(x + 30, y + 170), self.qtGuide3)
        GuideLine(QPointF(x, y + 170), self.qtGuide3)
        GuideLine(QPointF(x, y), self.qtGuide3)

        self.qtGuide1.setFence(QRectF(0, 0, 800, 600))
        self.qtGuide2.setFence(QRectF(0, 0, 800, 600))
        self.qtGuide3.setFence(QRectF(0, 0, 800, 600))

    ___ useGuide(self, guide, firstLetter, lastLetter):
        padding _ guide.lengthAll() / float(lastLetter - firstLetter)

        for i, letter in enumerate(self.letterList[firstLetter:lastLetter]):
            letter.useGuide(guide, i * padding)

    ___ useGuideQt(self):
        if self.currGuide is not self.qtGuide1:
            self.useGuide(self.qtGuide1, 0, self.letterCount)
            self.currGuide _ self.qtGuide1

    ___ useGuideTt(self):
        if self.currGuide is not self.qtGuide2:
            split _ int(self.letterCount * 5.0 / 7.0)
            self.useGuide(self.qtGuide2, 0, split)
            self.useGuide(self.qtGuide3, split, self.letterCount)
            self.currGuide _ self.qtGuide2

    ___ boundingRect(self):
        return QRectF(0, 0, 300, 320)

    ___ prepare(self):
        pass

    ___ switchToNextEffect(self):
        self.showCount +_ 1

        if self.showCount == 1:
            self.effect _ EffectSnake(self.letterList)
        elif self.showCount == 2:
            self.effect _ EffectLine(self.letterList)
            self.effect.setPostEffect(PostRotateXYTwist(0.01, 0.0, 0.003, 0.0))
        elif self.showCount == 3:
            self.effect _ EffectRaindrops(self.letterList)
            self.effect.setPostEffect(PostRotateXYTwist(0.01, 0.005, 0.003, 0.003))
        elif self.showCount == 4:
            self.effect _ EffectScan(self.letterList)
            self.effect.normalMoveSpeed _ 0
            self.effect.setPostEffect(PostRotateXY(0.008, 0.0, 0.005, 0.0))
        else:
            self.showCount _ 0
            self.effect _ EffectWhirlWind(self.letterList)

    ___ animationStarted(self, id):
        if id == DemoItemAnimation.ANIM_IN:
            if self.doIntroTransitions:
                # Make all letters disappear.
                for letter in self.letterList:
                    letter.setPos(1000, 0)

                self.switchToNextEffect()
                self.useGuideQt()
                self.scale _ 1.0

                # The first time we run, we have a rather large delay to
                # perform benchmark before the ticker shows.  But now, since we
                # are showing, use a more appropriate value.
                self.currentAnimation.setStartDelay(1500)
        elif self.effect is not None:
            self.effect.useSheepDog _ False

        self.tickTimer _ QTime.currentTime()

    ___ swapModel(self):
        if self.currGuide is self.qtGuide2:
            self.useGuideQt()
        else:
            self.useGuideTt()

    ___ hoverEnterEvent(self, event):
        # Skip swap here to enhance ticker dragging.
        pass

    ___ hoverLeaveEvent(self, event):
        self.swapModel()

    ___ setTickerScale(self, s):
        self.scale _ s
        self.qtGuide1.setScale(self.scale, self.scale)
        self.qtGuide2.setScale(self.scale, self.scale)
        self.qtGuide3.setScale(self.scale, self.scale)

    ___ mousePressEvent(self, event):
        self.mouseMoveLastPosition _ event.scenePos();

        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
        else:
            self.switchToNextEffect()

    ___ mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.OpenHandCursor)

    ___ mouseMoveEvent(self, event):
        newPosition _ event.scenePos()
        self.setPosUsingSheepDog(self.pos() + newPosition - self.mouseMoveLastPosition, QRectF(-260, -280, 1350, 1160))
        self.mouseMoveLastPosition _ newPosition

    ___ wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.effect.moveSpeed -_ 0.20
        else:
            self.effect.moveSpeed +_ 0.20

        if self.effect.moveSpeed < 0:
            self.effect.moveSpeed _ 0.0

    ___ pause(self, on):
        self.paused _ on
        self.tickTimer _ QTime.currentTime()

    ___ tick(self):
        if self.paused or not self.effect:
            return

        t _ self.tickTimer.msecsTo(QTime.currentTime())
        self.tickTimer _ QTime.currentTime()
        self.effect.tick(t / 10.0)

    ___ paint(self, painter, opt, widget):
        if self.tickOnPaint:
            self.tick()
