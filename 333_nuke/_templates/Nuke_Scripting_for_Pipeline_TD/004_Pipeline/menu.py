_____ __, sys
_____ ?

root = __.pa__.d..( -f)
?.tprint(root)

gizmos = __.pa__.join(root, 'icons')
print(gizmos)
?.pluginAddPath(gizmos, addToSysPath=T..)


_____ multi_script_editor

# add to menu
menubar = ?.m__("Nuke")
toolMenu = menubar.addMenu('&Tools')
toolMenu.aC..("Multi Script Editor", multi_script_editor.showNuke)

from clipboard _____ clipboard_core

m__ = ?.m__("Nuke")
fxphd = m__.addMenu("FXPHD")
fxphd.aC..("Clipboard","clipboardCore.start()")

# nodes
nodes = ?.m__("Nodes")
gizmos = nodes.addMenu('Gizmos', icon='cgninjas.png')

gizPath = __.pa__.join(root, 'gizmos')
___ gizmo __ __.l_d_(gizPath):
    __ __.pa__.s__(gizmo)[-1] __ '.gizmo':
        name = __.pa__.s__(gizmo)[0]
        ico = name+'.png'
        gizmos.aC..(name, "nuke.createNode('%s')" % name, icon=ico)

# Favorites
# nuke.addFavoriteDir('Pipeline', root)
# os.environ['JOB'] = 'c:/PROJECTS/project1'
# nuke.addFavoriteDir('JOB', '[getenv JOB]',nuke.IMAGE | nuke.GEO | nuke.FONT | nuke.PYTHON)



# sys.path.append('D:/PW_DATA/WinFolders/desktop/pipeline/nuke/python')
# _____ resizeNuke