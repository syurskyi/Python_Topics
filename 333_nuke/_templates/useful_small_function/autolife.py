# Autolife v1.0
# Autolife is based on SetRotoLifetimeAll by Marc Gutowski (http://www.nukepedia.com/python/nodegraph/setrotolifetimeall/)

# Instructions
# Put autolife.py in your .nuke directory or path
# Put "______ autolife" in your menu.py file

# This python script adds an 'autolife!' button to a 'user' tab on all Roto and Rotopaint nodes
# When clicked, all shapes or strokes that are locked, will have the lifetime automatically set
# to their first and last keyframe. I found myself setting the frame range manually for this a lot,
# especially when roto'ing objects that need new shapes very often, so I made Autolife to speed the
# workflow up.

# Please let me know if you come across any bugs or have suggestions, and I'll try fix or add them!

______ nuke

elements = []

___ addAutoLife():
  n = nuke.thisNode()
  n.addKnob(nuke.PyScript_Knob('autolife', 'autolife!', 'autolife.autoLife()'))

___ getElements(layer):
  ___ element __ layer:
    __ isinstance(element, nuke.rotopaint.Layer):
      getElements(element)
    ____ isinstance(element, nuke.rotopaint.Stroke) or isinstance(element, nuke.rotopaint.Shape):
      elements.append(element)

  r_ elements

___ autoLife():
  n = nuke.thisNode()
  
  nodec = n['curves']
  nlayer = nodec.rootLayer
  
  g__ elements
  # Clear global elements array so that only the current Roto/Rotopaint node's elements are 'autolifed'
  elements = []
  getElements(nlayer)
  
  ___ element __ elements:
    __ element.locked:
      element.locked = False
      
      # Get keyframes for the 0-indexed control point
      __ isinstance(element, nuke.rotopaint.Stroke):
	keys = element[0].getControlPointKeyTimes()
      ____ isinstance(element, nuke.rotopaint.Shape):
	keys = element[0].center.getControlPointKeyTimes()
      
      firstKey = keys[0]
      lastKey = keys[-1]
      
      attrs = element.getAttributes()
      attrs.set('ltn', firstKey) # frame range 'from' value
      attrs.set('ltm', lastKey) # frame range 'to' value
      attrs.set('ltt', 4) # set 'lifetime type' of element to 'frame range' - index 4 in combobox
      
      element.locked = T..
      nodec.changed()

nuke.addOnCreate(addAutoLife, nodeClass='Roto')
nuke.addOnCreate(addAutoLife, nodeClass='RotoPaint')
