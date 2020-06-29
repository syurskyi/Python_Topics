"""Defines viewer utility functions.
"""

import math
import nuke
import itertools


def toggle_viewer_lut():
    """Iterates thru viewer luts in the viewer"""
    viewer = nuke.activeViewer().node()['viewerProcess']
    luts = viewer.values()
    x = itertools.cycle(luts)
    for dummy in range(len(luts)):
        if viewer.value() == next(x):
            viewer.setValue(next(x))


def adjust_gain(original_gain, stop_offset):
    """Does the math for stop adjustments"""
    return 2 ** (math.log(original_gain, 2.0) + stop_offset)


def viewer_stop_adjust(increment):
    """Adjusts current viewer in stops"""
    nodes = nuke.allNodes('Viewer')
    for node in nodes:
        knob = node.knob('gain')
        gain = knob.value()
        knob.setValue(adjust_gain(gain, increment))


def viewer_stop_up():
    """Adjusts current viewer 1/4 stop up"""
    viewer_stop_adjust(0.25)


def viewer_stop_down():
    """Adjusts current viewer 1/4 stop down"""
    viewer_stop_adjust(-0.25)


def viewer_stop_reset():
    """Resets exposure on current viewer"""
    nodes = nuke.allNodes('Viewer')
    for node in nodes:
        knob = node.knob('gain')
        knob.setValue(1)
