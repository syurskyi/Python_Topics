#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
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


______ sys

____ ?.?C.. ______ QCoreApplication
____ ?.QtDBus ______ QDBusConnection, QDBusInterface


___ method1
    sys.stdout.w..("Method 1:\n")

    reply _ QDBusConnection.sessionBus().interface().registeredServiceNames()
    __ no. reply.isValid
        sys.stdout.w..("Error: %s\n" % reply.error().message())
        sys.exit(1)

    # Mimic the output from the C++ version.
    for name in reply.value
        sys.stdout.w..('"%s"\n' % name)


___ method2
    sys.stdout.w..("Method 2:\n")

    bus _ QDBusConnection.sessionBus()
    dbus_iface _ QDBusInterface('org.freedesktop.DBus',
            '/org/freedesktop/DBus', 'org.freedesktop.DBus', bus)
    names _ dbus_iface.call('ListNames').arguments()[0]

    # Mimic the output from the C++ version.
    sys.stdout.w..('QVariant(QStringList, ("%s") )\n' % '", "'.join(names))


___ method3
    sys.stdout.w..("Method 3:\n")

    names _ QDBusConnection.sessionBus().interface().registeredServiceNames().value()

    # Mimic the output from the C++ version.
    sys.stdout.w..('("%s")\n' % '", "'.join(names))


__ __name__ == '__main__':
    app _ QCoreApplication(sys.argv)

    __ no. QDBusConnection.sessionBus().isConnected
        sys.stderr.w..("Cannot connect to the D-Bus session bus.\n"
                "To start it, run:\n"
                "\teval `dbus-launch --auto-syntax`\n");
        sys.exit(1)

    method1()
    method2()
    method3()

    sys.exit()
