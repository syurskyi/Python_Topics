______ ?
______ os



#
## @brief [CLASS] - 
#
# More detailed description can be here
#
class BaseMenu(object):
    ___ __init__(self, menu_name):
        self._menu_name = menu_name 


    @property
    ___ menu_name(self):
        return self._menu_name


#
## @brief [CLASS] - 
#
# More detailed description can be here
#
class NukeMenuGenerator(BaseMenu):
    ___ __init__(self, menu_name):
        super(NukeMenuGenerator, self).__init__(menu_name)
        #NukeMenuGenerator.__dict__['__init__'](self, menu_name)


    ___ create_menu(self):
        menu_handle = ?.menu("Nuke").addMenu(self._menu_name)
        node_menu_handle = ?.menu("Nodes").addMenu(self._menu_name)


