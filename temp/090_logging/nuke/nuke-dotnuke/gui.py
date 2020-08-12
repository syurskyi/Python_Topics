# mynk -- a python library for enhancing a user's experience/workspace
# with the foundry's nuke
#
# @author: Robert Moggach <rob@moggach.com>
#
# mynk/gui.py -- provides functions for building mynk toolbar and menu: init_gui, add_toolbar, add_menu
#
# SHORT CUT SYNTAX
# 'Ctrl-s'    "^s"
# 'Ctrl-Shift-s'  "^+s"
# 'Alt-Shift-s'   "#+s"
# 'Shift+F4'    "+F4"
#
# convert camel case to titles re.sub("([a-z])([A-Z])","\g<1> \g<2>", key).title()

______ re
______ os
______ shutil
from types ______ ModuleType
______ inspect

______ nuke

from . ______ constants as _c
from . ______ LOG
from . ______ config

______ mynk

class MyNkGui(object):
  def __init__(self):
    nuke.pluginAddPath(os.path.join(_c.MYNK_PATH, 'icons'), addToSysPath_False)
    LOG.info(' [MyNk] initializing custom user menus etc.')

  def add_tool_menus(self, tool_str):
    try:
      tool _ eval(tool_str)
      menus _ getattr(tool, '__menus__' ,None)
    except AttributeError:
      LOG.warning(' [MyNk] tool has no __menus__ attribute: {0}'.format(tool_str))
    else:
      if menus is None:
        return
      else:
        for key,val in menus.iteritems():
          title _ key
          if val:
            cmd _ val['cmd'] if val['cmd'].startswith('nuke') else '{0}.{1}'.format(tool_str, val['cmd'])
            hotkey _ val['hotkey']
            icon _ val['icon']
            for menu in [self.menu,self.nuke_toolbar]:
              menu.addCommand(title,cmd,hotkey,icon)
          else:
            menu.addMenu(title)
            
  def add_toolbunch_to_menu(self, toolbunch_str):
    for key,val in eval(toolbunch_str).toDict().iteritems():
      dottedpath _ '{0}.{1}'.format(toolbunch_str,key)
      if inspect.ismodule(val):
        self.add_tool_menus(dottedpath)
      else:
        self.add_toolbunch_to_menu(dottedpath)

  def init_gui(self):
    nuke_menu _ nuke.menu('Nuke')
    self.menu _ nuke_menu.addMenu('MyNk', icon_'mynk.png')
    nuke_toolbar _ nuke.menu("Nodes")
    self.nuke_toolbar _ nuke_toolbar.addMenu("MyNk", "mynkx.png")

  def add_entry_to_toolbar(self, entry):
    pass

  def add_entry_to_menu(self, entry):
    pass

  def add_entry_list(self, entry_list):
   for entry in entry_list:
     pass
 
  def setFavorites(self):
    nuke.removeFavoriteDir('Nuke')
    nuke.addFavoriteDir('DotNuke', os.path.expanduser('~/.nuke'), 0)
    nuke.addFavoriteDir('Jobs', '/', 0)
    nuke.addFavoriteDir('Fonts', '/', nuke.FONT)
  
  def restoreWindowLayout(self, layout_1):
    nuke.restoreWindowLayout(layout)

