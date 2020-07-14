# -*- coding: UTF-8 -*-
'''
Author: Jaime Rivera
File: external_nuke_commands.py
Date: 2018.12.29
Revision: 2018.12.29
Copyright: Copyright Jaime Rivera 2018 | www.jaimervq.com
           The program(s) herein may be used, modified and/or distributed in accordance with the terms and conditions
           stipulated in the Creative Commons license under which the program(s) have been registered. (CC BY-SA 4.0)

Brief:

'''

__author__ = 'Jaime Rivera <jaime.rvq@gmail.com>'
__copyright__ = 'Copyright 2018, Jaime Rivera'
__credits__ = []
__license__ = 'Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)'
__maintainer__ = 'Jaime Rivera'
__email__ = 'jaime.rvq@gmail.com'
__status__ = 'Testing'


def nuke_paint_nodes(input=None):

    import nuke

    if len(nuke.selectedNodes()) == 0:
        return 'red', 'No node selected'

    for node in nuke.selectedNodes():
        node['tile_color'].setValue(int(input))

    if len(nuke.selectedNodes()) == 1:
        return 'lime', 'Node painted correctly'
    else:
        return 'lime', 'Nodes painted correctly'


def nuke_constant(input=None):

    import nuke

    const = nuke.nodes.Constant()
    const['color'].setValue(input)
    return 'lime', 'Constant node created'


def nuke_backdrop(input=None):

    import nukescripts

    bd = nukescripts.autoBackdrop()
    bd['tile_color'].setValue(int(input))
    return 'lime', 'Backdrop node created'


def nuke_IO(input=None):

    def execute_nuke(executable):
        import nuke
        import os, math, random
        exec (executable)

    try:
        execute_nuke(input)
        return 'lime', 'Command succesfully executed'
    except Exception as e:
        return 'red', 'ERROR: ' + str(e)


def nuke_set(input, color):

    import nuke

    if len(nuke.selectedNodes()) == 0:

        object = str(input.split('.')[0])
        attribute = str(input.split('.')[1])

        try:
            node = nuke.toNode(object)
            node[attribute].setValue(color)
            return 'lime', 'Knob value set correctly'
        except Exception as e:
            print e
            return 'red', 'Could not set knob value'

    elif len(nuke.selectedNodes()) == 1:

        object = nuke.selectedNodes()[0].name()
        print object
        attribute = input

        if '.' in input:
            return 'red', 'Knob value "{}" cannot be set to "{}"'.format(attribute, object)

        try:
            node = nuke.toNode(object)
            node[attribute].setValue(color)
            return 'lime', 'Knob value set correctly'
        except Exception as e:
            print e
            return 'red', 'Could not set knob value'

    elif len(nuke.selectedNodes()) > 1:

        node_number = len(nuke.selectedNodes())

        try:
            for node in nuke.selectedNodes():
                object = node.name()
                attribute = input
                node = nuke.toNode(object)
                node[attribute].setValue(color)
            return 'lime', 'Knob value set correctly to {} selected nodes'.format(node_number)
        except Exception as e:
            print e
            return 'red', 'Could not set knob value to selected nodes'


def nuke_get(input):

    import nuke

    if len(nuke.selectedNodes()) == 0:

        object = str(input.split('.')[0])
        attribute = str(input.split('.')[1])

        try:
            node = nuke.toNode(object)
            attr = node[attribute].value()
            return 'lime', str(attr)
        except Exception as e:
            print e
            return 'red', 'Could not get knob value'

    elif len(nuke.selectedNodes()) == 1:

        object = str(nuke.selectedNodes()[0].name())
        attribute = input

        if '.' in input:
            return 'red', 'Cannot get knob value "{}" from "{}"'.format(attribute, object)

        try:
            node = nuke.toNode(object)
            attr = node[attribute].value()
            return 'lime', str(attr)
        except Exception as e:
            print e
            return 'red', 'Could not get knob value'

    elif len(nuke.selectedNodes()) > 1:
        return 'red', 'Please, select one object or less'
