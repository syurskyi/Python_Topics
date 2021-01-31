# Shared ToolSets
# Based on Nuke's ToolSets 
# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.
# Vitaly Musatov 
# emails:
# latest.green[at]gmail[dot]com
# vit.musatov[at]gmail[dot]com
# Use setSharedToolSetsPath function to setup location of shared folder, folder must be called "SharedToolSets", but you can place it anywhere.
# 19 April 2019
# version 1.6
# History:
# 0.1 - Made base functions
# 1.1 - Instead of delete menu added modify menu. There you can edit, rename(move) and delete toolsets.
# 1.2 - Minor bug fixes. Delete .nk~ files and fixed a bug with overwriting of an existed file.
# 1.3 - Added tooltip in menu. Crossplatform way to define the root folder. Added undistractive filefilter.
# 1.4 - Opps... into menu.py added this line of code: toolbar = nuke.menu('Nodes') 
# 1.5 - Support of Nuke 11 and backward compatibility of previous versions.
# 1.6 - fixed a bug that caused Nuke crashing when loading of "big" toolsets

______ __
______ ___
______ ?
______ n_s_
______ posixpath
______ random
______ string


SHARED_TOOLSET_PATH _ ""
FILE_FILTER _ N..

___ setSharedToolSetsPath(pa__):
  global SHARED_TOOLSET_PATH
  SHARED_TOOLSET_PATH _ pa__

___ addFileFilter(externalFilter):
  global FILE_FILTER
  FILE_FILTER _ externalFilter

#def removeToolSets():
#  nodes = nuke.menu('Nodes')
#  nodes.removeItem("ToolSets")

c_ CreateToolsetsPanel(n_s_.PP..):
  # rename is bool var 

  ___  - (, fullFilePath, rename):
    
    rename _ rename
    fullFilePath _ fullFilePath

    __ rename __ F..:
      namePanel _ 'Create ToolSet'
      nameOkButton _ 'Create'
    ____
      namePanel _ 'Rename ToolSet'
      nameOkButton _ 'Rename'
    
    n_s_.PP... - ( , namePanel, 'uk.co.thefoundry.Toolset')
    
    # CREATE KNOBS
    userFolders _ # list
    fullPath _ SHARED_TOOLSET_PATH
    buildFolderList(fullPath, '')


    menuItemChoice _ ?.CascadingEnumeration_Knob('menuItemChoice','SharedToolSets menu', ['root'] + userFolders )
    menuItemChoice.setTooltip("The menu location that the ToolSet will appear in. Specify 'root' to place the SharedToolSets in the main SharedToolSets menu.")
    menuPath _ ?.String_Knob('itemName', 'Menu item:')
    menuPath.setFlag(0x00001000)
    menuPath.setTooltip("ToolSet name. Use the '/' character to create a new submenu for this ToolSet, eg to create a ToolSet named 'Basic3D' and place it in a new submenu '3D', type '3D/Basic3D'. Once created the 3D menu will appear in the ToolSet menu.")
    okButton _ ?.PS_K.. (nameOkButton.lower(), nameOkButton)
    #self.okButton.setToolTip("Create a ToolSet from the currently selected nodes with the given name")
    okButton.setFlag(0x00001000)
    cancelButton _ ?.PS_K.. ('cancel', 'Cancel')
    space _ ?.Text_Knob("space", "", "")
    infoText _ ?.Text_Knob('infoText', '<span style="color:orange">/ - create submenus,</span>',  '<span style="color:orange">example: newMenu/myNewToolSet</span>')

    # ADD KNOBS
    aK..(menuItemChoice)
    aK..(menuPath)
    aK..(okButton)
    aK..(cancelButton)
    aK..(space)
    aK..(infoText)

    __ rename __ T..:
      toolSetPath _ fullFilePath.replace(SHARED_TOOLSET_PATH + "/", '')
      toolSetPath _ toolSetPath.replace(".nk", '')
      menuPath.sV..(toolSetPath)

  #COMMENT:  BUILD A LIST Of PRE_CREATED FOLDER LOCATIONS
  ___ buildFolderList(, fullPath, menuPath):
    filecontents _ sorted(__.l_d_(fullPath), key_st..lower)
    ___ group __ filecontents:
      __ __.pa__.isd..(__.pa__.j..(fullPath, group)):
        userFolders.ap..(menuPath + group)
        buildFolderList(fullPath + '/' + group, menuPath + group + '/')

  ___ createPreset
    __ renameCreateSharedToolset(st.(menuPath.v.. ()), F..):
    #if self.createSharedToolset(str(self.menuPath.value())):
      finishModalDialog( T.. )
  
  ___ renamePreset
    __ renameCreateSharedToolset(st.(menuPath.v.. ()), T..):
      finishModalDialog( T.. )
    
  ___ renameCreateSharedToolset(, name, rename):
    ret _ F..
    
    nameList _ name.s..('/')
    fileName _ nameList[-1]
    
    del nameList[-1]
    dirs _ '/'.j..(nameList)
    
    fullPath _ posixpath.j..(SHARED_TOOLSET_PATH, dirs)
    
    ___
      __ no. __.pa__.isd..(fullPath):
        __.m_d_( fullPath )
      
      filePath _ posixpath.j..(fullPath, fileName + '.nk')
      
      __ no. __.pa__.e..(filePath):
        __ rename __ T..:
          __.rename(fullFilePath, filePath)
        ____
          # create way
          ?.nodeCopy(filePath)

      ____ ?.a..('Overwrite existing \n %s?' % filePath):
        __ rename __ T..:
          __.r__(filePath)
          __.rename(fullFilePath, filePath)
        ____
          # create way
          ?.nodeCopy(filePath)

      ret _ T..
    ______:
      ret _ F..
    r_ ret

  ___ getPresetPath

    #COMMENT: Added a bit of usability. Let's preserve a toolset's name
    tempListToolsetName _ menuPath.v.. ().s..('/')
    tempToolsetName _ tempListToolsetName[-1]

    __ st.(menuItemChoice.v.. ()) __ "root":
      menuPath.sV..( ""+ tempToolsetName)
    ____
      menuPath.sV..(menuItemChoice.v.. () + "/" + tempToolsetName)

  ___ knobChanged( , knob ):
    __ knob __ okButton:
      __ rename __ T..:
        renamePreset()
      ____
        createPreset()
    ____ knob __ cancelButton:
      finishModalDialog( F.. )
    ____ knob __ menuItemChoice:
      getPresetPath()

# NUKESCRIPT FUNCTIONS    
___ renameToolset(fullFilePath):
  p _ CreateToolsetsPanel(fullFilePath, T..)
  p.showModalDialog()
  rootPath _ SHARED_TOOLSET_PATH
  checkForEmptyToolsetDirectories(rootPath)
  refreshToolsetsMenu()
  print fullFilePath
    
___ addToolsetsPanel
  res _ F..
  __ ?.nodesSelected() __ T..:
    res _ CreateToolsetsPanel(N.., F..).showModalDialog()
    #COMMENT: now force a rebuild of the menu
    refreshToolsetsMenu()
  ____
    ?.m__("No nodes are selected")
  r_ res  
  
___ deleteToolset(rootPath, fileName):
  __ ?.a..('Are you sure you want to delete ToolSet %s?' %fileName):
    __.r__(fileName)
    #COMMENT: if this was the last file in this directory, the folder will need to be deleted.
    # Walk the directory tree from the root and recursively delete empty directories
    checkForEmptyToolsetDirectories(rootPath)
    #COMMENT: now force a rebuild of the menu
    refreshToolsetsMenu()

___ checkForEmptyToolsetDirectories(currPath):
  removed _ T..
  w__ removed __ T..:
    removed _ F..
    ___ root, dirs, files __ __.walk(currPath):
      __ files __ # list and dirs == []:
        __ root !_ SHARED_TOOLSET_PATH:
          __.rmdir(root)
          removed _ T..
        
___ refreshToolsetsMenu
  toolbar _ ?.m__("Nodes")
  m _ toolbar.fI..("SharedToolSets")
  __ m !_ N..:
    m.clearMenu()
    createToolsetsMenu(toolbar)

___ createToolsetsMenu(toolbar):
  m _ toolbar.addMenu(name _ "SharedToolSets", icon _ "SharedToolSets.png")
  m.aC..("Create", "shared_toolsets.addToolsetsPanel()", "", icon_"SharedToolSets_Create.png")
  m.aC..("-", "", "")
  __ populateToolsetsMenu(m, F..):
    m.aC..("-", "", "")
    n _ m.addMenu("Modify", "SharedToolSets_Modify.png")
    populateToolsetsMenu(n, T..)
  m.aC..('Refresh', 'shared_toolsets.refreshToolsetsMenu()', icon _ "SharedToolSets_Refresh.png")

___ traversePluginPaths(m, delete, allToolsetsList, isLocal):
  ret _ F..
  fullPath _ SHARED_TOOLSET_PATH
  __ createToolsetMenuItems(m, fullPath, fullPath, delete, allToolsetsList, isLocal):
      ret _ T..
  r_ ret  

___ populateToolsetsMenu(m, delete):
  ret _ F..
  allToolsetsList _ # list
  #COMMENT: now do shared toolsets like the local .nuke  
  __ traversePluginPaths(m, delete, allToolsetsList, T..):
    ret _ T..
  r_ ret   

___ randomStringDigits(stringLength_6):
    """Generate a random string of letters and digits """
    lettersAndDigits _ string.ascii_letters + string.digits
    r_ ''.j..(random.choice(lettersAndDigits) ___ i __ ra__(stringLength))

#COMMENT: warper around loadToolset
___ toolsetLoader(fullFileName):
    __ FILE_FILTER !_ N..:
        data _ fileFilter(fullFileName, FILE_FILTER)
        # SAVING TEMPORAL TOOLSET | instead of 
        #QApplication.clipboard().setText(data)
        #nuke.nodePaste("%clipboard%") is craching with big files BUG
        randomPostfix _ randomStringDigits(10)
        randomName _ posixpath.j..( SHARED_TOOLSET_PATH , "temp_toolset_%s.nk" % randomPostfix)
        saveTempToolSet _ open(randomName,"w+")
        saveTempToolSet.w..(data)
        saveTempToolSet.close()
        ?.loadToolset(randomName)
        __.r__(randomName)
    ____
        ?.loadToolset(fullFileName)
    r_ T..

#COMMENT: modify file before loading 
___ fileFilter(fileName, filterFunc):
    with open(fileName) __ f:
        content _ f.readlines()
    modifiedContentList _ # list
    ___ line __ content:
        __ "file" __ line:
            line _ filterFunc(line)
        modifiedContentList.ap..(line)
    modifiedContent _ "".j..(modifiedContentList)
    r_ modifiedContent

#COMMENT: Main function, construct menuName
___ createToolsetMenuItems(m, rootPath, fullPath, delete, allToolsetsList, isLocal):
  #TODO: CLEAN THIS FUNCTION

  filecontents _ sorted(__.l_d_(fullPath), key_st..lower)
  excludePaths _ ?.getToolsetExcludePaths()
  #COMMENT: First list all directories
  retval _ F..
  __ filecontents !_ # list:
    ___ group __ filecontents:
      newPath _ "/".j..([fullPath, group])
      ignore _ F..
      __ newPath.find(".svn") !_ -1:
        ignore _ T..
      ____
        ___ i __ excludePaths:
          i _ i.replace('\\', '/')
          __ newPath.find(i) !_ -1:
            ignore _ T..
            break
      __ __.pa__.isd..(newPath) and no. ignore:
        menuName _ group
        __ isLocal and (menuName __ allToolsetsList):
          menuName _ "[user] " + menuName
        ____ no. isLocal:
          allToolsetsList.ap..(menuName)
        n _ m.addMenu(menuName)
        retval _ createToolsetMenuItems(n, rootPath, "/".j..([fullPath, group]), delete, allToolsetsList, isLocal)
        #COMMENT: if we are deleting, and the sub directory is now empty, delete the directory also
        __ delete and __.l_d_(fullPath)__# list:
          __.rmdir(fullPath)
    # Now list individual files
    ___ group __ filecontents:
      fullFileName _ "/".j..([fullPath, group])
      __ no. __.pa__.isd..(fullFileName):
        
        #COMMENT: delete file with an extention ".nk~" created by edit.
        __ ".nk~" __ group:
          __.r__(fullFileName)
        
        extPos _ group.find(".nk")
        __ extPos !_ -1 and extPos __ le.(group) - 3:
          group _ group.replace('.nk', '')
          __ delete:
            subM _ m.addMenu(group)
            subM.aC..("Edit", 'nuke.scriptOpen("%s")' % fullFileName, "")
            subM.aC..("Rename", 'shared_toolsets.renameToolset("%s")' % fullFileName, "")
            subM.aC..("-", "", "")
            subM.aC..("Delete", 'shared_toolsets.deleteToolset("%s", "%s")' % (rootPath, fullFileName), "")
            retval _ T..
          ____
            #COMMENT: get the filename below toolsets
            i _ fullFileName.find("SharedToolSets/")
            __ i !_ -1:
              subfilename _ fullFileName[i:]
            ____
              #COMMENT: should never happen, but just in case ...
              subfilename _ fullfilename
            __ isLocal and (subfilename __ allToolsetsList):
              #COMMENT: if we've already appended [user] to the menu name, don't need it on the filename
              __ (i !_ -1) and subfilename[le.("SharedToolSets/"):].find("/") __ -1:
                group _ "[user] " + group
            ____ no. isLocal:
              allToolsetsList.ap..(subfilename)

            #TODO: get ref module name, now it is static linking
            #current_module = sys.modules[__name__]
            #print current_module
            m.aC..(group, 'shared_toolsets.toolsetLoader("%s")' %  fullFileName, "")
            retval _ T..
  r_ retval


