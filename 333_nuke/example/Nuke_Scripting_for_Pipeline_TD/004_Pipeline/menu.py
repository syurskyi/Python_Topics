import os, sys
import nuke

root = os.path.dirname(__file__)
nuke.tprint(root)

gizmos = os.path.join(root, 'icons')
print(gizmos)
nuke.pluginAddPath(gizmos, addToSysPath=True)


import multi_script_editor

# add to menu
menubar = nuke.menu("Nuke")
toolMenu = menubar.addMenu('&Tools')
toolMenu.addCommand("Multi Script Editor", multi_script_editor.showNuke)

from clipboard import clipboard_core

menu = nuke.menu("Nuke")
fxphd = menu.addMenu("FXPHD")
fxphd.addCommand("Clipboard","clipboardCore.start()")

# nodes
nodes = nuke.menu("Nodes")
gizmos = nodes.addMenu('Gizmos', icon='cgninjas.png')

gizPath = os.path.join(root, 'gizmos')
for gizmo in os.listdir(gizPath):
    if os.path.splitext(gizmo)[-1] == '.gizmo':
        name = os.path.splitext(gizmo)[0]
        ico = name+'.png'
        gizmos.addCommand(name, "nuke.createNode('%s')" % name, icon=ico)

# Favorites
# nuke.addFavoriteDir('Pipeline', root)
# os.environ['JOB'] = 'c:/PROJECTS/project1'
# nuke.addFavoriteDir('JOB', '[getenv JOB]',nuke.IMAGE | nuke.GEO | nuke.FONT | nuke.PYTHON)



# sys.path.append('D:/PW_DATA/WinFolders/desktop/pipeline/nuke/python')
# import resizeNuke