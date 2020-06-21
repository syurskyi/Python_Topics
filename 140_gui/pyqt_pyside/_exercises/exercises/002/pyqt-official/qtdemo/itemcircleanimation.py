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


______ m__
______ random

____ ?.?C.. ______ QLineF, QPointF, QRectF, __, ?T..

____ colors ______ Colors
____ demoitem ______ DemoItem
____ demoitemanimation ______ DemoItemAnimation
____ guidecircle ______ GuideCircle
____ guideline ______ GuideLine
____ letteritem ______ LetterItem


c_ TickerPostEffect o..
    ___ tick  adjust):
        p..

    ___ transform  item, pos):
        p..


c_ PostRotateXY(TickerPostEffect):
    ___  -   speedx, speedy, curvx, curvy):
        s__(PostRotateXY, self). - ()

        currRotX _ 0.0
        currRotY _ 0.0

        speedx _ speedx
        speedy _ speedy
        curvx _ curvx
        curvy _ curvy

    ___ tick  adjust):
        currRotX +_ speedx * adjust
        currRotY +_ speedy * adjust

    ___ transform  item, pos):
        parent _ item.parentItem()
        center _ parent.boundingRect().center()
        pos.setX(center.x() + (pos.x() - center.x()) * m__.cos(currRotX + pos.x() * curvx))
        pos.setY(center.y() + (pos.y() - center.y()) * m__.cos(currRotY + pos.y() * curvy))


c_ PostRotateXYTwist(PostRotateXY):
    ___ transform  item, pos):
        parent _ item.parentItem()
        center _ parent.boundingRect().center()
        pos.setX(center.x() + (pos.x() - center.x()) * m__.cos(currRotX + pos.y() * curvx))
        pos.setY(center.y() + (pos.y() - center.y()) * m__.cos(currRotY + pos.x() * curvy))


c_ TickerEffect o..
    Normal, Intro, Outro _ ra..(3)

    ___  -   letters):
        postEffect _ TickerPostEffect()
        status _ TickerEffect.Intro
        letters _ letters
        morphSpeed _ normalMorphSpeed _ Colors.tickerMorphSpeed
        moveSpeed _ normalMoveSpeed _ Colors.tickerMoveSpeed
        useSheepDog _ T..
        morphBetweenModels _ no. Colors.noTickerMorph

    ___ setPostEffect  effect):
        postEffect _ effect

    ___ slowDownAfterIntro  adjust):
        __ morphBetweenModels:
            __ status __ TickerEffect.Intro:
                dec _ 0.1 * adjust
                moveSpeed -_ dec
                __ moveSpeed < Colors.tickerMoveSpeed:
                    moveSpeed _ normalMoveSpeed
                    morphSpeed _ normalMorphSpeed
                    status _ TickerEffect.Normal

    ___ moveLetters  adjust):
        adaptedMoveSpeed _ moveSpeed * adjust
        adaptedMorphSpeed _ morphSpeed * adjust
        postEffect.tick(adjust)

        __ morphBetweenModels:
            move_speed _ adaptedMoveSpeed
            morph_speed _ adaptedMorphSpeed
        ____
            move_speed _ Colors.tickerMoveSpeed
            morph_speed _ -1

        ___ letter __ letters:
            letter.guideAdvance(move_speed)
            letter.guideMove(morph_speed)

            pos _ letter.getGuidedPos()
            postEffect.transform(letter, pos)

            __ useSheepDog:
                letter.setPosUsingSheepDog(pos, QRectF(0, 0, 800, 600))
            ____
                letter.setPos(pos)

    ___ tick  adjust):
        slowDownAfterIntro(adjust)
        moveLetters(adjust)


c_ EffectWhirlWind(TickerEffect):
    ___  -   letters):
        s__(EffectWhirlWind, self). - (letters)

        moveSpeed _ 50

        ___ letter __ letters:
            letter.setGuidedPos(QPointF(0, 100))


c_ EffectSnake(TickerEffect):
    ___  -   letters):
        s__(EffectSnake, self). - (letters)

        moveSpeed _ 40

        ___ i, letter __ en..(letters):
            letter.setGuidedPos(QPointF(0, -250 - (i * 5)))


c_ EffectScan(TickerEffect):
    ___  -   letters):
        s__(EffectScan, self). - (letters)

        ___ letter __ letters:
            letter.setGuidedPos(QPointF(100, -300))


c_ EffectRaindrops(TickerEffect):
    ___  -   letters):
        s__(EffectRaindrops, self). - (letters)

        ___ letter __ letters:
            letter.setGuidedPos(QPointF(random.randint(-100, 100),
                    random.randint(-200, 1100)))


c_ EffectLine(TickerEffect):
    ___  -   letters):
        s__(EffectLine, self). - (letters)

        ___ i, letter __ en..(letters):
            letter.setGuidedPos(QPointF(100, 500 + i * 20))


c_ ItemCircleAnimation(DemoItem):
    ___  -   parent_None):
        s__(ItemCircleAnimation, self). - (parent)

        letterList _   # list
        letterCount _ Colors.tickerLetterCount
        scale _ 1.0
        showCount _ -1
        tickOnPaint _ F..
        paused _ F..
        doIntroTransitions _ T..
        setAcceptHoverEvents( st.
        setCursor(__.OpenHandCursor)
        setupGuides()
        setupLetters()
        useGuideQt()
        effect _ N..

        mouseMoveLastPosition _ QPointF()
        tickTimer _ ?T..()

    ___ createLetter  c):
        letter _ LetterItem(c, self)
        letterList.ap..(letter)

    ___ setupLetters
        letterList _   # list

        s _ Colors.tickerText
        tlen _ le.(s)
        room _ letterCount
        w__ room >_ tlen:
            ___ c __ s:
                createLetter(c)

            room -_ tlen

        # Fill in with blanks.
        w__ room > 0:
            createLetter(' ')
            room -_ 1

    ___ setupGuides
        x _ 0
        y _ 20

        qtGuide1 _ GuideCircle(QRectF(x, y, 260, 260), -36, 342)
        GuideLine(QPointF(x + 240, y + 268), qtGuide1)
        GuideLine(QPointF(x + 265, y + 246), qtGuide1)
        GuideLine(QPointF(x + 158, y + 134), qtGuide1)
        GuideLine(QPointF(x + 184, y + 109), qtGuide1)
        GuideLine(QPointF(x + 160, y +  82), qtGuide1)
        GuideLine(QPointF(x +  77, y + 163), qtGuide1)
        GuideLine(QPointF(x + 100, y + 190), qtGuide1)
        GuideLine(QPointF(x + 132, y + 159), qtGuide1)
        GuideLine(QPointF(x + 188, y + 211), qtGuide1)
        GuideCircle(QRectF(x + 30, y + 30, 200, 200), -30, 336, GuideCircle.CW, qtGuide1)
        GuideLine(QPointF(x + 238, y + 201), qtGuide1)

        y _ 30
        qtGuide2 _ GuideCircle(QRectF(x + 30, y + 30, 200, 200), 135, 270, GuideCircle.CCW)
        GuideLine(QPointF(x + 222, y + 38), qtGuide2)
        GuideCircle(QRectF(x, y, 260, 260), 135, 270, GuideCircle.CW, qtGuide2)
        GuideLine(QPointF(x + 59, y + 59), qtGuide2)

        x _ 115
        y _ 10
        qtGuide3 _ GuideLine(QLineF(x, y, x + 30, y))
        GuideLine(QPointF(x + 30, y + 170), qtGuide3)
        GuideLine(QPointF(x, y + 170), qtGuide3)
        GuideLine(QPointF(x, y), qtGuide3)

        qtGuide1.setFence(QRectF(0, 0, 800, 600))
        qtGuide2.setFence(QRectF(0, 0, 800, 600))
        qtGuide3.setFence(QRectF(0, 0, 800, 600))

    ___ useGuide  guide, firstLetter, lastLetter):
        padding _ guide.lengthAll() / fl..(lastLetter - firstLetter)

        ___ i, letter __ en..(letterList[firstLetter:lastLetter]):
            letter.useGuide(guide, i * padding)

    ___ useGuideQt
        __ currGuide __ no. qtGuide1:
            useGuide(qtGuide1, 0, letterCount)
            currGuide _ qtGuide1

    ___ useGuideTt
        __ currGuide __ no. qtGuide2:
            sp.. _ in.(letterCount * 5.0 / 7.0)
            useGuide(qtGuide2, 0, sp..)
            useGuide(qtGuide3, sp.., letterCount)
            currGuide _ qtGuide2

    ___ boundingRect
        r_ QRectF(0, 0, 300, 320)

    ___ prepare
        p..

    ___ switchToNextEffect
        showCount +_ 1

        __ showCount __ 1:
            effect _ EffectSnake(letterList)
        ____ showCount __ 2:
            effect _ EffectLine(letterList)
            effect.setPostEffect(PostRotateXYTwist(0.01, 0.0, 0.003, 0.0))
        ____ showCount __ 3:
            effect _ EffectRaindrops(letterList)
            effect.setPostEffect(PostRotateXYTwist(0.01, 0.005, 0.003, 0.003))
        ____ showCount __ 4:
            effect _ EffectScan(letterList)
            effect.normalMoveSpeed _ 0
            effect.setPostEffect(PostRotateXY(0.008, 0.0, 0.005, 0.0))
        ____
            showCount _ 0
            effect _ EffectWhirlWind(letterList)

    ___ animationStarted  id):
        __ id __ DemoItemAnimation.ANIM_IN:
            __ doIntroTransitions:
                # Make all letters disappear.
                ___ letter __ letterList:
                    letter.setPos(1000, 0)

                switchToNextEffect()
                useGuideQt()
                scale _ 1.0

                # The first time we run, we have a rather large delay to
                # perform benchmark before the ticker shows.  But now, since we
                # are showing, use a more appropriate value.
                currentAnimation.setStartDelay(1500)
        ____ effect __ no. N..:
            effect.useSheepDog _ F..

        tickTimer _ ?T...currentTime()

    ___ swapModel
        __ currGuide __ qtGuide2:
            useGuideQt()
        ____
            useGuideTt()

    ___ hoverEnterEvent  event):
        # Skip swap here to enhance ticker dragging.
        p..

    ___ hoverLeaveEvent  event):
        swapModel()

    ___ setTickerScale  s):
        scale _ s
        qtGuide1.setScale(scale, scale)
        qtGuide2.setScale(scale, scale)
        qtGuide3.setScale(scale, scale)

    ___ mousePressEvent  event):
        mouseMoveLastPosition _ event.scenePos();

        __ event.button() __ __.LeftButton:
            setCursor(__.ClosedHandCursor)
        ____
            switchToNextEffect()

    ___ mouseReleaseEvent  event):
        __ event.button() __ __.LeftButton:
            setCursor(__.OpenHandCursor)

    ___ mouseMoveEvent  event):
        newPosition _ event.scenePos()
        setPosUsingSheepDog(pos() + newPosition - mouseMoveLastPosition, QRectF(-260, -280, 1350, 1160))
        mouseMoveLastPosition _ newPosition

    ___ wheelEvent  event):
        __ event.angleDelta().y() > 0:
            effect.moveSpeed -_ 0.20
        ____
            effect.moveSpeed +_ 0.20

        __ effect.moveSpeed < 0:
            effect.moveSpeed _ 0.0

    ___ pause  on):
        paused _ on
        tickTimer _ ?T...currentTime()

    ___ tick
        __ paused or no. effect:
            r_

        t _ tickTimer.msecsTo(?T...currentTime())
        tickTimer _ ?T...currentTime()
        effect.tick(t / 10.0)

    ___ paint  painter, opt, widget):
        __ tickOnPaint:
            tick()
