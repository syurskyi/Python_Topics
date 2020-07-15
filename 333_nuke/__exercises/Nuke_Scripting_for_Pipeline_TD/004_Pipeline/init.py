import os, sys
import nuke

root = os.path.dirname(__file__)
print(root)

# plugins
gizmos = os.path.join(root, 'gizmos')
print(gizmos)
nuke.pluginAddPath(gizmos, addToSysPath=False)

# python
py = os.path.join(root, 'python')
sys.path.append(py)
print(py)

# formats
# nuke.addFormat('320 240 1.0 320p')
# nuke.knobDefault('Root.format', '320p')


sys.path.append(root)