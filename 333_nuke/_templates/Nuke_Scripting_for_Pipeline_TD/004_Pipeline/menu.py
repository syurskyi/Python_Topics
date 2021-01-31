_____ __, ___
_____ ?

root _ __.pa__.d..( -f)
?.tprint(root)

gizmos _ __.pa__.j..(root, 'icons')
print(gizmos)
?.pAP..(gizmos, addToSysPath_T..)


_____ multi_script_editor

# add to menu
menubar _ ?.m__("Nuke")
toolMenu _ menubar.addMenu('&Tools')
toolMenu.aC..("Multi Script Editor", multi_script_editor.showNuke)

____ clipboard _____ clipboard_core

m__ _ ?.m__("Nuke")
fxphd _ m__.addMenu("FXPHD")
fxphd.aC..("Clipboard","clipboardCore.start()")

# nodes
n__ _ ?.m__("Nodes")
gizmos _ n__.addMenu('Gizmos', icon_'cgninjas.png')

gizPath _ __.pa__.j..(root, 'gizmos')
___ gizmo __ __.l_d_(gizPath):
    __ __.pa__.s__(gizmo)[-1] __ '.gizmo':
        name _ __.pa__.s__(gizmo)[0]
        ico _ name+'.png'
        gizmos.aC..(name, "nuke.createNode('%s')" % name, icon_ico)

# Favorites
# nuke.addFavoriteDir('Pipeline', root)
# os.environ['JOB'] = 'c:/PROJECTS/project1'
# nuke.addFavoriteDir('JOB', '[getenv JOB]',nuke.IMAGE | nuke.GEO | nuke.FONT | nuke.PYTHON)



# sys.path.append('D:/PW_DATA/WinFolders/desktop/pipeline/nuke/python')
# _____ resizeNuke