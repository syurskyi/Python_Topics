______ __
______ re
______ ___
______ platform
______ inspect
______ nuke
______ string


D.. _ F..

___ camel(value, delimiter_' '):
  ___ camelCase():
    yield str.lower
    while T..:
      yield str.capitalize
  c _ camelCase()
  r_ "".j..(c.next()(x) __ x else delimiter ___ x __ value.split(delimiter))


___ unCamel(value, delimiter_'_', lowercase_True, capitals_False):
  s1 _ re.sub('(.)([A-Z][a-z]+)', r'\1%s\2'%delimiter, value)
  s2 _ re.sub('([a-z0-9])([A-Z])', r'\1%s\2'%delimiter, s1)
  __ lowercase is T..:
    s2_s2.lower()
  ____ capitals is T..:
    s2_string.capwords(s2)
  r_ s2


c_ GizmoPathManager(object):

  ___  - (, exclude_r'^(\.|icons|.*\.bak|readme\.txt)', searchPaths_None):
    '''Used to add folders within the gizmo folder(s) to the gizmo path
    exclude: a regular expression for folders / gizmos which should NOT be
    added; by default, excludes files / folders that begin with a "."
    searchPaths: a list of paths to recursively search; __ not given, it
    will use the NUKE_GIZMO_PATH environment variable; __ that is
    not defined, it will use the directory in which this file resides;
    and __ it cannot detect that, it will use the pluginPath
    '''
    #__ isinstance(exclude, basestring):
    exclude _ re.compile(exclude)
    exclude _ exclude
    __ searchPaths is N..:
      searchPaths _ __.environ.get('NUKE_GIZMO_PATH', '').split(__.pathsep)
      __ no. searchPaths:
        ______ inspect
        this_file _ inspect.getsourcefile(lambda: N..)
        __ this_file:
          searchPaths _ [__.path.dirname(__.path.abspath(this_file))]
        ____
          searchPaths _ list(nuke.pluginPath())
    searchPaths _ searchPaths
    reset()

  ??
  ___ canonicalPath(___, path):
    # fixes path names and resolution
    r_ __.path.normcase(__.path.normpath((__.path.abspath(path))))
    # return os.path.normcase(os.path.normpath(os.path.realpath(os.path.abspath(path))))

  ___ reset
    # reset the _crawlData dict
    _crawlData _ {}

  ___ addGizmoPaths
    '''
    Recursively search searchPaths for folders to add to the nuke
    pluginPath.
    '''
    reset()
    _visited _ set()
    ___ gizmoPath __ searchPaths:
      _recursiveAddGizmoPaths(gizmoPath, _crawlData, foldersOnly_False)

  ___ _recursiveAddGizmoPaths(, folder, crawlData, foldersOnly_False):
    # If we're in GUI mode, also store away data in _crawlData to to be used
    # later by addGizmoMenuItems
    __ no. __.path.isdir(folder):
      r_

    __ nuke.GUI:
      __ 'files' no. __ crawlData:
        crawlData['gizmos'] _ {}
      __ 'dirs' no. __ crawlData:
        crawlData['dirs'] _ {}

    # avoid an infinite loop due to symlinks...
    canonicalPath _ canonicalPath(folder)
    __ canonicalPath __ _visited:
      r_
    _visited.add(canonicalPath)

    ___ subItem __ sorted(__.listdir(canonicalPath)):
      __ exclude and exclude.search(subItem):
        continue
      subPath _ __.path.j..(canonicalPath, subItem)
      __ __.path.isdir(subPath):
        nuke.pluginAppendPath(subPath)
        nuke.pluginAppendPath(__.path.j..(subPath,'icons'))
        __ D..:
          nuke.tprint('GIZMO PATH: %s' % subPath)
        subData _ {}
        __ nuke.GUI:
          crawlData['dirs'][subItem] _ subData
        _recursiveAddGizmoPaths(subPath, subData)
      ____ nuke.GUI and (no. foldersOnly) and __.path.isfile(subPath):
        name, ext _ __.path.splitext(subItem)
        __ ext __ '.gizmo':
          __ re.match('[0-9]{3}', name[-3:]):
            gizmoName _ name[:-4]
            version _ name[-3:]
          ____
            gizmoName _ name
            version _ '000'
          crawlData['gizmos'][gizmoName]_[]
          crawlData['gizmos'][gizmoName].ap..(int(version))
          __ D..:
            nuke.tprint('GIZMO NAME: %s' % name)
            nuke.tprint('GIZMO VERS: %s' % version )


  ___ addGizmoMenuItems(, toolbar_None, default_top_menu_None):
    '''
    Recursively create menu items for gizmos found on the searchPaths.
    Only call this __ youre in nuke GUI mode! (ie, from inside menu.py)
    toolbar - the toolbar to which to add the menus; defaults to "Nodes"
    default_top_menu - __ you do not wish to create new "top level" menu items,
    then top-level directories for which there is not already a top-level
    menu will be added to this menu instead (which must already exist)
    '''
    __ no. _crawlData:
      addGizmoPaths()
    __ toolbar is N..:
      toolbar _ nuke.menu("Nodes")
    ____ isinstance(toolbar, basestring):
      toolbar _ nuke.menu(toolbar)
    #toolbar.addCommand("-", "", "")
    _recursiveAddGizmoMenuItems(toolbar, _crawlData, defaultSubMenu_default_top_menu, topLevel_True)


  ___ _recursiveAddGizmoMenuItems(, toolbar, crawlData, defaultSubMenu_None, topLevel_False):
    ___ name, versions __ crawlData['gizmos'].items():
      niceName _ name
      filename _ "%s_%03d" % (name, max(versions))
      niceName _ name.replace('_',' ')
      niceName _ unCamel(niceName,' ',F..,T..)
      __ D..:
        nuke.tprint('GIZMO NAME: %s' % name)
        nuke.tprint('GIZMO VERS: %s' % ('%03d' % max(versions)) )
        nuke.tprint('GIZMO NICENAME: %s' % niceName)
      toolbar.addCommand(niceName,"nuke.createNode('%s')" % filename, '%s.png' % name )

    ___ folder, data __ crawlData.get('dirs', {}).iteritems():
      ______ ___
      subMenu _ toolbar.findItem(folder)
      __ subMenu is N..:
        __ defaultSubMenu:
          subMenu _ toolbar.findItem(defaultSubMenu)
          subMenu.addCommand("-", "", "")
        ____
          subMenu _ toolbar.addMenu(folder, "%s.png" % folder)
      subMenu.addCommand("-", "", "")
      _recursiveAddGizmoMenuItems(subMenu, data)



