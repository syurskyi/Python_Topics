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

__author__ _ 'Jaime Rivera <jaime.rvq@gmail.com>'
__copyright__ _ 'Copyright 2018, Jaime Rivera'
__credits__ _ # list
__license__ _ 'Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)'
__maintainer__ _ 'Jaime Rivera'
__email__ _ 'jaime.rvq@gmail.com'
__status__ _ 'Testing'


___ nuke_paint_nodes(input_N..):

    ______ ?

    __ le.(?.sN..()) __ 0:
        r_ 'red', 'No node selected'

    ___ node __ ?.sN..
        node['tile_color'].sV..(in_(input))

    __ le.(?.sN..()) __ 1:
        r_ 'lime', 'Node painted correctly'
    ____
        r_ 'lime', 'Nodes painted correctly'


___ nuke_constant(input_N..):

    ______ ?

    const _ ?.n__.Constant()
    const['color'].sV..(input)
    r_ 'lime', 'Constant node created'


___ nuke_backdrop(input_N..):

    ______ n_s_

    bd _ n_s_.autoBackdrop()
    bd['tile_color'].sV..(in_(input))
    r_ 'lime', 'Backdrop node created'


___ nuke_IO(input_N..):

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

        object _ st.(input.s..('.')[0])
        attribute _ st.(input.s..('.')[1])

        ___
            node _ ?.tN..(object)
            node[attribute].sV..(color)
            r_ 'lime', 'Knob value set correctly'
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not set knob value'

    ____ le.(?.sN..()) __ 1:

        object _ ?.sN..()[0].n..
        print object
        attribute _ input

        __ '.' __ input:
            r_ 'red', 'Knob value "{}" cannot be set to "{}"'.f..(attribute, object)

        ___
            node _ ?.tN..(object)
            node[attribute].sV..(color)
            r_ 'lime', 'Knob value set correctly'
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not set knob value'

    ____ le.(?.sN..()) > 1:

        node_number _ le.(?.sN..())

        ___
            ___ node __ ?.sN..
                object _ node.n..
                attribute _ input
                node _ ?.tN..(object)
                node[attribute].sV..(color)
            r_ 'lime', 'Knob value set correctly to {} selected nodes'.f..(node_number)
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not set knob value to selected nodes'


___ nuke_get(input):

    ______ ?

    __ le.(?.sN..()) __ 0:

        object _ st.(input.s..('.')[0])
        attribute _ st.(input.s..('.')[1])

        ___
            node _ ?.tN..(object)
            attr _ node[attribute].v.. ()
            r_ 'lime', st.(attr)
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not get knob value'

    ____ le.(?.sN..()) __ 1:

        object _ st.(?.sN..()[0].n..
        attribute _ input

        __ '.' __ input:
            r_ 'red', 'Cannot get knob value "{}" from "{}"'.f..(attribute, object)

        ___
            node _ ?.tN..(object)
            attr _ node[attribute].v.. ()
            r_ 'lime', st.(attr)
        ______ E.. __ e:
            print e
            r_ 'red', 'Could not get knob value'

    ____ le.(?.sN..()) > 1:
        r_ 'red', 'Please, select one object or less'
