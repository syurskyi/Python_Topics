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


______ ___

____ ?.?G.. ______ ?C.., ?F..
____ ?.?W.. ______ ?MB.., ?W..


c_ Colors o..
    # Colors:
    sceneBg1 _ ?C..(91, 91, 91)
    sceneBg1Line _ ?C..(114, 108, 104)
    sceneBg2 _ ?C..(0, 0, 0)
    sceneLine _ ?C..(255, 255, 255)
    paperBg _ ?C..(100, 100, 100)
    menuTextFg _ ?C..(255, 0, 0)
    buttonBgLow _ ?C..(255, 255, 255, 90)
    buttonBgHigh _ ?C..(255, 255, 255, 20)
    buttonText _ ?C..(255, 255, 255)
    tt_green _ ?C..(166, 206, 57)
    fadeOut _ ?C..(206, 246, 117, 0)
    heading _ ?C..(190, 230, 80)
    contentColor _ "<font color='#eeeeee'>"
    glVersion _ "Not detected!"

    # Guides:
    stageStartY _ 8
    stageHeight _ 536
    stageStartX _ 8
    stageWidth _ 785
    contentStartY _ 22
    contentHeight _ 510

    # Properties:
    noTicker _ F..
    noRescale _ F..
    noAnimations _ F..
    noBlending _ F..
    noScreenSync _ F..
    fullscreen _ F..
    usePixmaps _ F..
    useLoop _ F..
    showBoundingRect _ F..
    showFps _ F..
    noAdapt _ F..
    noWindowMask _ T..
    useButtonBalls _ F..
    useEightBitPalette _ F..
    noTimerUpdate _ F..
    noTickerMorph _ F..
    adapted _ F..
    verbose _ F..
    pause _ T..

    fps _ 100
    menuCount _ 18
    animSpeed _ 1.0
    benchmarkFps _ -1.0
    tickerLetterCount _ 80;
    tickerMoveSpeed _ 0.4
    tickerMorphSpeed _ 2.5
    tickerText _ ".EROM ETAERC .SSEL EDOC"
    rootMenuName _ "PyQt Examples"

    @staticmethod
    ___ contentFont
        font _ ?F..()
        font.setStyleStrategy(?F...PreferAntialias)

        __ ___.platform __ 'darwin':
            font.setPixelSize(14)
            font.sF..('Arial')
        ____
            font.setPixelSize(13)
            font.sF..('Verdana')

        r_ font

    @staticmethod
    ___ headingFont
        font _ ?F..()
        font.setStyleStrategy(?F...PreferAntialias)

        font.setPixelSize(23)
        font.setBold( st.
        font.sF..('Verdana')

        r_ font;

    @staticmethod
    ___ buttonFont
        font _ ?F..()
        font.setStyleStrategy(?F...PreferAntialias)

        font.setPixelSize(11)
        font.sF..('Verdana')

        r_ font

    @staticmethod
    ___ tickerFont
        font _ ?F..()
        font.setStyleStrategy(?F...PreferAntialias)

        __ ___.platform __ 'darwin':
            font.setPixelSize(11)
            font.setBold( st.
            font.sF..('Arial')
        ____
            font.setPixelSize(10)
            font.setBold( st.
            font.sF..('sans serif')

        r_ font

    @classmethod
    ___ debug(cls, *args):
        __ cls.verbose:
            ___.stderr.w..("%s\n" % " ".join([st.(arg) ___ arg __ args]))

    @classmethod
    ___ parseArgs(cls, a..:
        # Some arguments should be processed before others.  Handle them now.
        __ "-verbose" __ argv:
            cls.verbose _ T..

        # Handle the rest of the arguments.  They may override attributes
        # already set.
        ___ s __ argv:
            __ s __ "-no-ticker":
                cls.noTicker _ T..
            ____ s.s_w_("-ticker"):
                cls.noTicker _  no. bool(parseFloat(s, "-ticker"))
            ____ s __ "-no-animations":
                cls.noAnimations _ T..
            ____ s.s_w_("-animations"):
                cls.noAnimations _ no. bool(parseFloat(s, "-animations"))
            ____ s __ "-no-adapt":
                # Don't adapt the animations based on the actual performance.
                cls.noAdapt _ T..
            ____ s __ "-low":
                cls.setLowSettings()
            ____ s __ "-no-rescale":
                cls.noRescale _ T..
            ____ s __ "-use-pixmaps":
                cls.usePixmaps _ T..
            ____ s __ "-fullscreen":
                cls.fullscreen _ T..
            ____ s __ "-show-br":
                cls.showBoundingRect _ T..
            ____ s __ "-show-fps":
                cls.showFps _ T..
            ____ s __ "-no-blending":
                cls.noBlending _ T..
            ____ s __ "-no-sync":
                cls.noScreenSync _ T..
            ____ s.s_w_("-menu"):
                cls.menuCount _ in.(parseFloat(s, "-menu"))
            ____ s.s_w_("-use-timer-update"):
                cls.noTimerUpdate _ no. bool(parseFloat(s, "-use-timer-update"))
            ____ s.s_w_("-pause"):
                cls.pause _ bool(parseFloat(s, "-pause"))
            ____ s __ "-no-ticker-morph":
                cls.noTickerMorph _ T..
            ____ s __ "-use-window-mask":
                cls.noWindowMask _ F..
            ____ s __ "-use-loop":
                cls.useLoop _ T..
            ____ s __ "-use-8bit":
                cls.useEightBitPalette _ T..
            ____ s.s_w_("-8bit"):
                cls.useEightBitPalette _ bool(parseFloat(s, "-8bit"))
            ____ s __ "-use-balls":
                cls.useButtonBalls _ T..
            ____ s.s_w_("-ticker-letters"):
                cls.tickerLetterCount _ in.(parseFloat(s, "-ticker-letters"))
            ____ s.s_w_("-ticker-text"):
                cls.tickerText _ parseText(s, "-ticker-text")
            ____ s.s_w_("-ticker-speed"):
                cls.tickerMoveSpeed _ parseFloat(s, "-ticker-speed")
            ____ s.s_w_("-ticker-morph-speed"):
                cls.tickerMorphSpeed _ parseFloat(s, "-ticker-morph-speed")
            ____ s.s_w_("-animation-speed"):
                cls.animSpeed _ parseFloat(s, "-animation-speed")
            ____ s.s_w_("-fps"):
                cls.fps _ in.(parseFloat(s, "-fps"))
            ____ s.s_w_("-h") or s.s_w_("-help"):
                ?MB...w..(N.., "Arguments",
                        "Usage: qtdemo.py [-verbose] [-no-adapt] "
                        "[-fullscreen] [-ticker[0|1]] "
                        "[-animations[0|1]] [-no-blending] [-no-sync] "
                        "[-use-timer-update[0|1]] [-pause[0|1]] "
                        "[-use-window-mask] [-no-rescale] [-use-pixmaps] "
                        "[-show-fps] [-show-br] [-8bit[0|1]] [-menu<int>] "
                        "[-use-loop] [-use-balls] [-animation-speed<float>] "
                        "[-fps<int>] [-low] [-ticker-letters<int>] "
                        "[-ticker-speed<float>] [-no-ticker-morph] "
                        "[-ticker-morph-speed<float>] [-ticker-text<string>]")
                ___.e..(0)

        cls.postConfigure()

    @classmethod
    ___ setLowSettings(cls):
        cls.noTicker _ T..
        cls.noTimerUpdate _ T..
        cls.fps _ 30
        cls.usePixmaps _ T..
        cls.noAnimations _ T..
        cls.noBlending _ T..

    @classmethod
    ___ postConfigure(cls):
        __ no. cls.noAdapt:
            w _ ?W..

            __ w.depth() < 16:
                cls.useEightBitPalette _ T..
                cls.adapted _ T..
                cls.debug("- Adapt: Color depth less than 16 bit. Using 8 bit palette")


___ parseFloat(argument, name):
    ___
        value _ fl..(parseText(argument, name))
    _____ V..:
        value _ 0.0

    r_ value


___ parseText(argument, name):
    __ le.(name) __ le.(argument):
        ?MB...w..(N.., "Arguments",
                "No argument number found for %s. Remember to put name and "
                "value adjacent! (e.g. -fps100)")
        ___.e..(0)

    r_ argument[le.(name):]
