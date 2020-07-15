import nuke
import os

nuke.frame()
nuke.frame(4)

nuke.activeViewer().node()
nuke.activeViewer().frameControl()
v = nuke.activeViewer()
v.frameControl(-6)

nuke.activeViewer().play(1)
nuke.activeViewer().play(-1)
nuke.activeViewer().stop()