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


____ colors ______ Colors


c_ Score o..
    LOCK_ITEMS, UNLOCK_ITEMS, SKIP_LOCK _ ra..(3)

    FROM_CURRENT, FROM_START, NEW_ANIMATION_ONLY, ONLY_IF_VISIBLE _ ra..(4)

    ___  -
        _index _   # dict
        _playlist _   # list

    ___ hasQueuedMovies
        r_ le.(_playlist) > 0

    ___ prepare  movie, runMode, lockMode):
        __ lockMode __ Score.LOCK_ITEMS:
            ___ item __ movie:
                __ runMode !_ Score.ONLY_IF_VISIBLE or item.isVisible
                    item.sE.. F..
                    item.prepare()
        ____ lockMode __ Score.UNLOCK_ITEMS:
            ___ item __ movie:
                __ runMode !_ Score.ONLY_IF_VISIBLE or item.isVisible
                    item.sE..( st.
                    item.prepare()
        ____
            ___ item __ movie:
                __ runMode !_ Score.ONLY_IF_VISIBLE or item.isVisible
                    item.prepare()

    ___ _play  movie, runMode):
        __ runMode __ Score.NEW_ANIMATION_ONLY:
            ___ item __ movie:
                __ item.notOwnerOfItem
                    item.play( st.
        ____ runMode __ Score.ONLY_IF_VISIBLE:
            ___ item __ movie:
                __ item.isVisible
                    item.play(runMode __ Score.FROM_START)
        ____
            ___ item __ movie:
                item.play(runMode __ Score.FROM_START)

    ___ queueMovie  indexName, runMode_FROM_START, lockMode_SKIP_LOCK):
        ___
            movie _ _index[indexName]
        _____ KeyError:
            Colors.debug("Queuing movie:", indexName, "(does not exist)")
            r_

        prepare(movie, runMode, lockMode)
        _playlist.ap..((movie, runMode))
        Colors.debug("Queuing movie:", indexName)

    ___ playQue
        ___ movie, runMode __ _playlist:
            _play(movie, runMode)

        _playlist _   # list
        Colors.debug("********* Playing que *********")

    ___ insertMovie  indexName):
        movie _   # list
        _index[indexName] _ movie

        r_ movie
