______ os
______ re
______ sys
______ platform
______ inspect
______ nuke
______ string


D.. _ False

def camel(value, delimiter_' '):
  def camelCase():
    yield str.lower
    while True:
      yield str.capitalize
  c _ camelCase()
  return "".join(c.next()(x) if x else delimiter for x in value.split(delimiter))


def unCamel(value, delimiter_'_', lowercase_True, capitals_False):
  s1 _ re.sub('(.)([A-Z][a-z]+)', r'\1%s\2'%delimiter, value)
  s2 _ re.sub('([a-z0-9])([A-Z])', r'\1%s\2'%delimiter, s1)
  if lowercase is True:
    s2_s2.lower()
  elif capitals is True:
    s2_string.capwords(s2)
  return s2


class GizmoPathManager(object):

  def __init__(self, exclude_r'^(\.|icons|.*\.bak|readme\.txt)', searchPaths_None):
    '''Used to add folders within the gizmo folder(s) to the gizmo path
    exclude: a regular expression for folders / gizmos which should NOT be
    added; by default, excludes files / folders that begin with a "."
    searchPaths: a list of paths to recursively search; if not given, it
    will use the NUKE_GIZMO_PATH environment variable; if that is
    not defined, it will use the directory in which this file resides;
    and if it cannot detect that, it will use the pluginPath
    '''
    #if isinstance(exclude, basestring):
    exclude _ re.compile(exclude)
    self.exclude _ exclude
    if searchPaths is None:
      searchPaths _ os.environ.get('NUKE_GIZMO_PATH', '').split(os.pathsep)
      if not searchPaths:
        ______ inspect
        this_file _ inspect.getsourcefile(lambda: None)
        if this_file:
          searchPaths _ [os.path.dirname(os.path.abspath(this_file))]
        else:
          searchPaths _ list(nuke.pluginPath())
    self.searchPaths _ searchPaths
    self.reset()

  @classmethod
  def canonicalPath(cls, path):
    # fixes path names and resolution
    return os.path.normcase(os.path.normpath((os.path.abspath(path))))
    # return os.path.normcase(os.path.normpath(os.path.realpath(os.path.abspath(path))))

  def reset(self):
    # reset the _crawlData dict
    self._crawlData _ {}

  def addGizmoPaths(self):
    '''
    Recursively search searchPaths for folders to add to the nuke
    pluginPath.
    '''
    self.reset()
    self._visited _ set()
    for gizmoPath in self.searchPaths:
      self._recursiveAddGizmoPaths(gizmoPath, self._crawlData, foldersOnly_False)

  def _recursiveAddGizmoPaths(self, folder, crawlData, foldersOnly_False):
    # If we're in GUI mode, also store away data in _crawlData to to be used
    # later by addGizmoMenuItems
    if not os.path.isdir(folder):
      return

    if nuke.GUI:
      if 'files' not in crawlData:
        crawlData['gizmos'] _ {}
      if 'dirs' not in crawlData:
        crawlData['dirs'] _ {}

    # avoid an infinite loop due to symlinks...
    canonicalPath _ self.canonicalPath(folder)
    if canonicalPath in self._visited:
      return
    self._visited.add(canonicalPath)

    for subItem in sorted(os.listdir(canonicalPath)):
      if self.exclude and self.exclude.search(subItem):
        continue
      subPath _ os.path.join(canonicalPath, subItem)
      if os.path.isdir(subPath):
        nuke.pluginAppendPath(subPath)
        nuke.pluginAppendPath(os.path.join(subPath,'icons'))
        if D..:
          nuke.tprint('GIZMO PATH: %s' % subPath)
        subData _ {}
        if nuke.GUI:
          crawlData['dirs'][subItem] _ subData
        self._recursiveAddGizmoPaths(subPath, subData)
      elif nuke.GUI and (not foldersOnly) and os.path.isfile(subPath):
        name, ext _ os.path.splitext(subItem)
        if ext == '.gizmo':
          if re.match('[0-9]{3}', name[-3:]):
            gizmoName _ name[:-4]
            version _ name[-3:]
          else:
            gizmoName _ name
            version _ '000'
          crawlData['gizmos'][gizmoName]_[]
          crawlData['gizmos'][gizmoName].append(int(version))
          if D..:
            nuke.tprint('GIZMO NAME: %s' % name)
            nuke.tprint('GIZMO VERS: %s' % version )


  def addGizmoMenuItems(self, toolbar_None, default_top_menu_None):
    '''
    Recursively create menu items for gizmos found on the searchPaths.
    Only call this if youre in nuke GUI mode! (ie, from inside menu.py)
    toolbar - the toolbar to which to add the menus; defaults to "Nodes"
    default_top_menu - if you do not wish to create new "top level" menu items,
    then top-level directories for which there is not already a top-level
    menu will be added to this menu instead (which must already exist)
    '''
    if not self._crawlData:
      self.addGizmoPaths()
    if toolbar is None:
      toolbar _ nuke.menu("Nodes")
    elif isinstance(toolbar, basestring):
      toolbar _ nuke.menu(toolbar)
    #toolbar.addCommand("-", "", "")
    self._recursiveAddGizmoMenuItems(toolbar, self._crawlData, defaultSubMenu_default_top_menu, topLevel_True)


  def _recursiveAddGizmoMenuItems(self, toolbar, crawlData, defaultSubMenu_None, topLevel_False):
    for name, versions in crawlData['gizmos'].items():
      niceName _ name
      filename _ "%s_%03d" % (name, max(versions))
      niceName _ name.replace('_',' ')
      niceName _ unCamel(niceName,' ',False,True)
      if D..:
        nuke.tprint('GIZMO NAME: %s' % name)
        nuke.tprint('GIZMO VERS: %s' % ('%03d' % max(versions)) )
        nuke.tprint('GIZMO NICENAME: %s' % niceName)
      toolbar.addCommand(niceName,"nuke.createNode('%s')" % filename, '%s.png' % name )

    for folder, data in crawlData.get('dirs', {}).iteritems():
      ______ sys
      subMenu _ toolbar.findItem(folder)
      if subMenu is None:
        if defaultSubMenu:
          subMenu _ toolbar.findItem(defaultSubMenu)
          subMenu.addCommand("-", "", "")
        else:
          subMenu _ toolbar.addMenu(folder, "%s.png" % folder)
      subMenu.addCommand("-", "", "")
      self._recursiveAddGizmoMenuItems(subMenu, data)



