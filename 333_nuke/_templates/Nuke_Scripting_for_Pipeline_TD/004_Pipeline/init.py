_____ __, sys
_____ ?

root = __.pa__.dirname(__file__)
print(root)

# plugins
gizmos = __.pa__.join(root, 'gizmos')
print(gizmos)
?.pluginAddPath(gizmos, addToSysPath=False)

# python
py = __.pa__.join(root, 'python')
sys.pa__.a__(py)
print(py)

# formats
# nuke.addFormat('320 240 1.0 320p')
# nuke.knobDefault('Root.format', '320p')


sys.pa__.a__(root)