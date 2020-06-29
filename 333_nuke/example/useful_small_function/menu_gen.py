import nuke 
import os



#
## @brief [CLASS] - 
#
# More detailed description can be here
#
class BaseMenu(object):
    def __init__(self, menu_name):
        self._menu_name = menu_name 


    @property
    def menu_name(self):
        return self._menu_name


#
## @brief [CLASS] - 
#
# More detailed description can be here
#
class NukeMenuGenerator(BaseMenu):
    def __init__(self, menu_name):
        super(NukeMenuGenerator, self).__init__(menu_name)
        #NukeMenuGenerator.__dict__['__init__'](self, menu_name)


    def create_menu(self):
        menu_handle = nuke.menu("Nuke").addMenu(self._menu_name)
        node_menu_handle = nuke.menu("Nodes").addMenu(self._menu_name)


