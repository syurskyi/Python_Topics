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


c_ Score(object):
    LOCK_ITEMS, UNLOCK_ITEMS, SKIP_LOCK _ range(3)

    FROM_CURRENT, FROM_START, NEW_ANIMATION_ONLY, ONLY_IF_VISIBLE _ range(4)

    ___ __init__(self):
        self._index _ {}
        self._playlist _ []

    ___ hasQueuedMovies(self):
        r_ len(self._playlist) > 0

    ___ prepare  movie, runMode, lockMode):
        __ lockMode == Score.LOCK_ITEMS:
            for item in movie:
                __ runMode !_ Score.ONLY_IF_VISIBLE or item.isVisible
                    item.setEnabled F..
                    item.prepare()
        ____ lockMode == Score.UNLOCK_ITEMS:
            for item in movie:
                __ runMode !_ Score.ONLY_IF_VISIBLE or item.isVisible
                    item.setEnabled(True)
                    item.prepare()
        ____
            for item in movie:
                __ runMode !_ Score.ONLY_IF_VISIBLE or item.isVisible
                    item.prepare()

    ___ _play  movie, runMode):
        __ runMode == Score.NEW_ANIMATION_ONLY:
            for item in movie:
                __ item.notOwnerOfItem
                    item.play(True)
        ____ runMode == Score.ONLY_IF_VISIBLE:
            for item in movie:
                __ item.isVisible
                    item.play(runMode == Score.FROM_START)
        ____
            for item in movie:
                item.play(runMode == Score.FROM_START)

    ___ queueMovie  indexName, runMode_FROM_START, lockMode_SKIP_LOCK):
        try:
            movie _ self._index[indexName]
        except KeyError:
            Colors.debug("Queuing movie:", indexName, "(does not exist)")
            r_

        self.prepare(movie, runMode, lockMode)
        self._playlist.append((movie, runMode))
        Colors.debug("Queuing movie:", indexName)

    ___ playQue(self):
        for movie, runMode in self._playlist:
            self._play(movie, runMode)

        self._playlist _ []
        Colors.debug("********* Playing que *********")

    ___ insertMovie  indexName):
        movie _ []
        self._index[indexName] _ movie

        r_ movie
