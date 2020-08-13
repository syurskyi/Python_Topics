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
______ __
______ shutil
____ types ______ ModuleType
______ inspect

______ nuke

____ . ______ constants __ _c
____ . ______ LOG
____ . ______ config

______ mynk

c_ MyNkGui(object):
  ___  -
    nuke.pluginAddPath(__.path.j..(_c.MYNK_PATH, 'icons'), addToSysPath_False)
    LOG.i..(' [MyNk] initializing custom user menus etc.')

  ___ add_tool_menus(, tool_str):
    ___
      tool _ eval(tool_str)
      menus _ getattr(tool, '__menus__' ,None)
    _____ AttributeError:
      LOG.w..(' [MyNk] tool has no __menus__ attribute: {0}'.f..(tool_str))
    ____
      __ menus is None:
        r_
      ____
        ___ key,val __ menus.iteritems():
          title _ key
          __ val:
            cmd _ val['cmd'] __ val['cmd'].startswith('nuke') else '{0}.{1}'.f..(tool_str, val['cmd'])
            hotkey _ val['hotkey']
            icon _ val['icon']
            ___ menu __ [menu,nuke_toolbar]:
              menu.addCommand(title,cmd,hotkey,icon)
          ____
            menu.addMenu(title)
            
  ___ add_toolbunch_to_menu(, toolbunch_str):
    ___ key,val __ eval(toolbunch_str).toDict().iteritems():
      dottedpath _ '{0}.{1}'.f..(toolbunch_str,key)
      __ inspect.ismodule(val):
        add_tool_menus(dottedpath)
      ____
        add_toolbunch_to_menu(dottedpath)

  ___ init_gui
    nuke_menu _ nuke.menu('Nuke')
    menu _ nuke_menu.addMenu('MyNk', icon_'mynk.png')
    nuke_toolbar _ nuke.menu("Nodes")
    nuke_toolbar _ nuke_toolbar.addMenu("MyNk", "mynkx.png")

  ___ add_entry_to_toolbar(, entry):
    p..

  ___ add_entry_to_menu(, entry):
    p..

  ___ add_entry_list(, entry_list):
   ___ entry __ entry_list:
     p..
 
  ___ setFavorites
    nuke.removeFavoriteDir('Nuke')
    nuke.addFavoriteDir('DotNuke', __.path.expanduser('~/.nuke'), 0)
    nuke.addFavoriteDir('Jobs', '/', 0)
    nuke.addFavoriteDir('Fonts', '/', nuke.FONT)
  
  ___ restoreWindowLayout(, layout_1):
    nuke.restoreWindowLayout(layout)

