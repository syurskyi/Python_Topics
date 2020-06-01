#!/usr/bin/env python

"""
counterlabelplugin.py

A counter label custom widget plugin for Qt Designer.

Copyright (C) 2006 David Boddie <david@boddie.org.uk>
Copyright (C) 2005-2006 Trolltech ASA. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

____ ?.?G.. ______ QIcon
____ ?.QtDesigner ______ QPyDesignerCustomWidgetPlugin

____ counterlabel ______ CounterLabel


c_ CounterLabelPlugin(QPyDesignerCustomWidgetPlugin):
    """CounterLabelPlugin(QPyDesignerCustomWidgetPlugin)

    Provides a Python custom plugin for Qt Designer by implementing the
    QDesignerCustomWidgetPlugin via a PyQt-specific custom plugin class.
    """

    # The __init__() method is only used to set up the plugin and define its
    # initialized variable.
    ___  -   parent_None):
    
        super(CounterLabelPlugin, self). - (parent)

        initialized _ False

    ___ initialize  formEditor):

        __ initialized:
            r_
        
        initialized _ True

    ___ isInitialized

        r_ initialized

    # This factory method creates new instances of our custom widget with the
    # appropriate parent.
    ___ createWidget  parent):
        widget _ CounterLabel(parent)
        widget.setValue(1)
        r_ widget

    # This method returns the name of the custom widget class that is provided
    # by this plugin.
    ___ name
        r_ "CounterLabel"

    # Returns the name of the group in Qt Designer's widget box that this
    # widget belongs to.
    ___ group
        r_ "PyQt Examples"

    # Returns the icon used to represent the custom widget in Qt Designer's
    # widget box.
    ___ icon
        r_ QIcon()

    # Returns a short description of the custom widget for use in a tool tip.
    ___ toolTip
        r_ ""

    # Returns a short description of the custom widget for use in a "What's
    # This?" help message for the widget.
    ___ whatsThis
        r_ ""

    # Returns True if the custom widget acts as a container for other widgets;
    # otherwise returns False. Note that plugins for custom containers also
    # need to provide an implementation of the QDesignerContainerExtension
    # interface if they need to add custom editing support to Qt Designer.
    ___ isContainer
        r_ False

    # Returns an XML description of a custom widget instance that describes
    # default values for its properties. Each custom widget created by this
    # plugin will be configured using this description.
    ___ domXml
        r_ '<widget class="CounterLabel" name="counterLabel" />\n'

    # Returns the module containing the custom widget class. It may include
    # a module path.
    ___ includeFile
        r_ "counterlabel"
