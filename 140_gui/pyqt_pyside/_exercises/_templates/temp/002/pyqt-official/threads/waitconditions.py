#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
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


______ ___
______ random

____ ?.?C.. ______  ?CA.., QMutex, ?T.., QWaitCondition


DataSize _ 100000
BufferSize _ 8192
buffer _ li..(ra..(BufferSize))

bufferNotEmpty _ QWaitCondition()
bufferNotFull _ QWaitCondition()
mutex _ QMutex()
numUsedBytes _ 0


c_ Producer(?T..):
    ___ run 
        gl.. numUsedBytes

        ___ i __ ra..(DataSize):
            mutex.lock()
            __ numUsedBytes __ BufferSize:
                bufferNotFull.wait(mutex)
            mutex.unlock()
            
            buffer[i % BufferSize] _ "ACGT"[random.randint(0, 3)]

            mutex.lock()
            numUsedBytes +_ 1
            bufferNotEmpty.wakeAll()
            mutex.unlock()


c_ Consumer(?T..):
    ___ run 
        gl.. numUsedBytes

        ___ i __ ra..(DataSize):
            mutex.lock()
            __ numUsedBytes __ 0:
                bufferNotEmpty.wait(mutex)
            mutex.unlock()
            
            ___.stderr.w..(buffer[i % BufferSize])

            mutex.lock()
            numUsedBytes -_ 1
            bufferNotFull.wakeAll()
            mutex.unlock()
            
        ___.stderr.w..("\n")


__ ______ __ ______
    app _  ?CA..(___.a..
    producer _ Producer()
    consumer _ Consumer()
    producer.start()
    consumer.start()
    producer.wait()
    consumer.wait()
