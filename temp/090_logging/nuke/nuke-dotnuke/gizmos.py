______ os
______ re
______ sys
______ platform
______ inspect
______ nuke
______ string


D.. _ False

___ camel(value, delimiter_' '):
  ___ camelCase():
    yield str.lower
    while True:
      yield str.capitalize
  c _ camelCase()
  r_ "".join(c.next()(x) __ x else delimiter for x __ value.split(delimiter))


___ unCamel(value, delimiter_'_', lowercase_True, capitals_False):
  s1 _ re.sub('(.)([A-Z][a-z]+)', r'\1%s\2'%delimiter, value)
  s2 _ re.sub('([a-z0-9])([A-Z])', r'\1%s\2'%delimiter, s1)
  __ lowercase is True:
    s2_s2.lower()
  elif capitals is True:
    s2_string.capwords(s2)
  r_ s2


c_ GizmoPathManager(object):

  ___  - (self, exclude_r'^(\.|icons|.*\.bak|readme\.txt)', searchPaths_None):
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
    __ searchPaths is None:
      searchPaths _ os.environ.get('NUKE_GIZMO_PATH', '').split(os.pathsep)
      __ no. searchPaths:
        ______ inspect
        this_file _ inspect.getsourcefile(lambda: None)
        __ this_file:
          searchPaths _ [os.path.dirname(os.path.abspath(this_file))]
        else:
          searchPaths _ list(nuke.pluginPath())
    searchPaths _ searchPaths
    reset()

  @classmethod
  ___ canonicalPath(cls, path):
    # fixes path names and resolution
    r_ os.path.normcase(os.path.normpath((os.path.abspath(path))))
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
    for gizmoPath __ searchPaths:
      _recursiveAddGizmoPaths(gizmoPath, _crawlData, foldersOnly_False)

  ___ _recursiveAddGizmoPaths(self, folder, crawlData, foldersOnly_False):
    # If we're in GUI mode, also store away data in _crawlData to to be used
    # later by addGizmoMenuItems
    __ no. os.path.isdir(folder):
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

    for subItem __ sorted(os.listdir(canonicalPath)):
      __ exclude and exclude.search(subItem):
        continue
      subPath _ os.path.join(canonicalPath, subItem)
      __ os.path.isdir(subPath):
        nuke.pluginAppendPath(subPath)
        nuke.pluginAppendPath(os.path.join(subPath,'icons'))
        __ D..:
          nuke.tprint('GIZMO PATH: %s' % subPath)
        subData _ {}
        __ nuke.GUI:
          crawlData['dirs'][subItem] _ subData
        _recursiveAddGizmoPaths(subPath, subData)
      elif nuke.GUI and (no. foldersOnly) and os.path.isfile(subPath):
        name, ext _ os.path.splitext(subItem)
        __ ext == '.gizmo':
          __ re.match('[0-9]{3}', name[-3:]):
            gizmoName _ name[:-4]
            version _ name[-3:]
          else:
            gizmoName _ name
            version _ '000'
          crawlData['gizmos'][gizmoName]_[]
          crawlData['gizmos'][gizmoName].append(int(version))
          __ D..:
            nuke.tprint('GIZMO NAME: %s' % name)
            nuke.tprint('GIZMO VERS: %s' % version )


  ___ addGizmoMenuItems(self, toolbar_None, default_top_menu_None):
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
    __ toolbar is None:
      toolbar _ nuke.menu("Nodes")
    elif isinstance(toolbar, basestring):
      toolbar _ nuke.menu(toolbar)
    #toolbar.addCommand("-", "", "")
    _recursiveAddGizmoMenuItems(toolbar, _crawlData, defaultSubMenu_default_top_menu, topLevel_True)


  ___ _recursiveAddGizmoMenuItems(self, toolbar, crawlData, defaultSubMenu_None, topLevel_False):
    for name, versions __ crawlData['gizmos'].items():
      niceName _ name
      filename _ "%s_%03d" % (name, max(versions))
      niceName _ name.replace('_',' ')
      niceName _ unCamel(niceName,' ',False,True)
      __ D..:
        nuke.tprint('GIZMO NAME: %s' % name)
        nuke.tprint('GIZMO VERS: %s' % ('%03d' % max(versions)) )
        nuke.tprint('GIZMO NICENAME: %s' % niceName)
      toolbar.addCommand(niceName,"nuke.createNode('%s')" % filename, '%s.png' % name )

    for folder, data __ crawlData.get('dirs', {}).iteritems():
      ______ sys
      subMenu _ toolbar.findItem(folder)
      __ subMenu is None:
        __ defaultSubMenu:
          subMenu _ toolbar.findItem(defaultSubMenu)
          subMenu.addCommand("-", "", "")
        else:
          subMenu _ toolbar.addMenu(folder, "%s.png" % folder)
      subMenu.addCommand("-", "", "")
      _recursiveAddGizmoMenuItems(subMenu, data)



