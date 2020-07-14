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
__credits__ = # list
__license__ = 'Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)'
__maintainer__ = 'Jaime Rivera'
__email__ = 'jaime.rvq@gmail.com'
__status__ = 'Testing'


___ nuke_paint_nodes(input=None):

    ______ ?

    __ le.(?.sN..()) __ 0:
        r_ 'red', 'No node selected'

    ___ node __ ?.sN..():
        node['tile_color'].sV..(int(input))

    __ le.(?.sN..()) __ 1:
        r_ 'lime', 'Node painted correctly'
    ____
        r_ 'lime', 'Nodes painted correctly'


___ nuke_constant(input=None):

    ______ ?

    const = ?.nodes.Constant()
    const['color'].sV..(input)
    r_ 'lime', 'Constant node created'


___ nuke_backdrop(input=None):

    ______ nukescripts

    bd = nukescripts.autoBackdrop()
    bd['tile_color'].sV..(int(input))
    r_ 'lime', 'Backdrop node created'


___ nuke_IO(input=None):

    ___ execute_nuke(executable):
        ______ ?
        ______ __, math, random
        exec (executable)

    ___
        execute_nuke(input)
        r_ 'lime', 'Command succesfully executed'
    ______ E.. __ e
        r_ 'red', 'ERROR: ' + st.?


___ nuke_set(input, color):

    ______ ?

    __ le.(?.sN.. __ 0

        object = st.(input.s..('.')[0])
        attribute = st.(input.s..('.')[1])

        ___
            node = ?.tN..(object)
            node[attribute].sV..(color)
            r_ 'lime', 'Knob value set correctly'
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not set knob value'

    ____ le.(?.sN..()) __ 1:

        object = ?.sN..()[0].n..
        print object
        attribute = input

        __ '.' __ input:
            r_ 'red', 'Knob value "{}" cannot be set to "{}"'.format(attribute, object)

        ___
            node = ?.tN..(object)
            node[attribute].sV..(color)
            r_ 'lime', 'Knob value set correctly'
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not set knob value'

    ____ le.(?.sN..()) > 1:

        node_number = le.(?.sN..())

        ___
            ___ node __ ?.sN..():
                object = node.n..
                attribute = input
                node = ?.tN..(object)
                node[attribute].sV..(color)
            r_ 'lime', 'Knob value set correctly to {} selected nodes'.format(node_number)
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not set knob value to selected nodes'


___ nuke_get(input):

    ______ ?

    __ le.(?.sN..()) __ 0:

        object = st.(input.s..('.')[0])
        attribute = st.(input.s..('.')[1])

        ___
            node = ?.tN..(object)
            attr = node[attribute].value()
            r_ 'lime', st.(attr)
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not get knob value'

    ____ le.(?.sN..()) __ 1:

        object = st.(?.sN..()[0].n..
        attribute = input

        __ '.' __ input:
            r_ 'red', 'Cannot get knob value "{}" from "{}"'.format(attribute, object)

        ___
            node = ?.tN..(object)
            attr = node[attribute].value()
            r_ 'lime', st.(attr)
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not get knob value'

    ____ le.(?.sN..()) > 1:
        r_ 'red', 'Please, select one object or less'
