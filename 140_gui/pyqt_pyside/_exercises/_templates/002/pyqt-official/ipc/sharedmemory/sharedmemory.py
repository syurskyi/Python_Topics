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


____ ?.?C.. ______ QBuffer, ?DS.., QSharedMemory
____ ?.?G.. ______ QImage, ?P..
____ ?.?W.. ______ ?A.., ?D.., ?FD..

____ dialog ______ Ui_Dialog


c_ Dialog(?D..):
    """ This class is a simple example of how to use QSharedMemory.  It is a
    simple dialog that presents a few buttons.  Run the executable twice to
    create two processes running the dialog.  In one of the processes, press
    the button to load an image into a shared memory segment, and then select
    an image file to load.  Once the first process has loaded and displayed the
    image, in the second process, press the button to read the same image from
    shared memory.  The second process displays the same image loaded from its
    new location in shared memory.

    The class contains a data member sharedMemory, which is initialized with
    the key "QSharedMemoryExample" to force all instances of Dialog to access
    the same shared memory segment.  The constructor also connects the
    clicked() signal from each of the three dialog buttons to the slot function
    appropriate for handling each button.
    """

    ___  -   parent _ N..):
        s__(Dialog, self). - (parent)

        sharedMemory _ QSharedMemory('QSharedMemoryExample')

        ui _ Ui_Dialog()
        ui.setupUi

        ui.loadFromFileButton.c__.c..(loadFromFile)
        ui.loadFromSharedMemoryButton.c__.c..(loadFromMemory)

        sWT..("SharedMemory Example")

    ___ loadFromFile 
        """ This slot function is called when the "Load Image From File..."
        button is pressed on the firs Dialog process.  First, it tests whether
        the process is already connected to a shared memory segment and, if so,
        detaches from that segment.  This ensures that we always start the
        example from the beginning if we run it multiple times with the same
        two Dialog processes.  After detaching from an existing shared memory
        segment, the user is prompted to select an image file.  The selected
        file is loaded into a QImage.  The QImage is displayed in the Dialog
        and streamed into a QBuffer with a QDataStream.  Next, it gets a new
        shared memory segment from the system big enough to hold the image data
        in the QBuffer, and it locks the segment to prevent the second Dialog
        process from accessing it.  Then it copies the image from the QBuffer
        into the shared memory segment.  Finally, it unlocks the shared memory
        segment so the second Dialog process can access it.  After self
        function runs, the user is expected to press the "Load Image from
        Shared Memory" button on the second Dialog process.
        """

        __ sharedMemory.isAttached
            detach()

        ui.label.sT..("Select an image file")
        fileName, _ _ ?FD...gOFN..  N.., N..,
                "Images (*.png *.xpm *.jpg)")
        image _ QImage()
        __ no. image.load(fileName):
            ui.label.sT..(
                    "Selected file is not an image, please select another.")
            r_

        ui.label.sP..(?P...fromImage(image))

        # Load into shared memory.
        buf _ QBuffer()
        buf.o..(QBuffer.ReadWrite)
        out _ ?DS..(buf)
        out << image
        size _ buf.size()

        __ no. sharedMemory.create(size):
            ui.label.sT..("Unable to create shared memory segment.")
            r_

        size _ min(sharedMemory.size(), size)
        sharedMemory.lock()

        # Copy image data from buf into shared memory area.
        sharedMemory.data()[:size] _ buf.data()[:size]
        sharedMemory.unlock()

    ___ loadFromMemory 
        """ This slot function is called in the second Dialog process, when the
        user presses the "Load Image from Shared Memory" button.  First, it
        attaches the process to the shared memory segment created by the first
        Dialog process.  Then it locks the segment for exclusive access, copies
        the image data from the segment into a QBuffer, and streams the QBuffer
        into a QImage.  Then it unlocks the shared memory segment, detaches
        from it, and finally displays the QImage in the Dialog.
        """

        __ no. sharedMemory.attach
            ui.label.sT..(
                    "Unable to attach to shared memory segment.\nLoad an "
                    "image first.")
            r_
 
        buf _ QBuffer()
        ins _ ?DS..(buf)
        image _ QImage()

        sharedMemory.lock()
        buf.setData(sharedMemory.constData())
        buf.o..(QBuffer.ReadOnly)
        ins >> image
        sharedMemory.unlock()
        sharedMemory.detach()

        ui.label.sP..(?P...fromImage(image))

    ___ detach 
        """ This private function is called by the destructor to detach the
        process from its shared memory segment.  When the last process detaches
        from a shared memory segment, the system releases the shared memory.
        """

        __ no. sharedMemory.detach
            ui.label.sT..("Unable to detach from shared memory.")


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    dialog _ Dialog()
    dialog.s..
    ___.e.. ?.e..
