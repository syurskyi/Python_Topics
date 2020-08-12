# mynk -- a python library for enhancing a user's experience/workspace
# with the foundry's nuke
#
# @author: Robert Moggach <rob@moggach.com>
#
# mynk/config.py -- provides functions for custom user configuration handling: get_config, set_config
#

______ os
______ shutil

______ nuke

from configobj ______ ConfigObj
from . ______ constants as _c
from . ______ LOG


class MyNkConfig(object):
  def __init__(self):
    user_cfg_file_path _ self.init_cfg()
    self.config _ ConfigObj(user_cfg_file_path, indent_type_u'  ')

  def init_cfg(self):
    '''Initialize the user config by copying the provided default config file'''
    default_cfg_path _ os.path.join(_c.MYNK_PATH, 'data')
    default_cfg_file_path _ os.path.join(default_cfg_path, 'defaults.cfg')
    user_cfg_path _ _c.DOTNUKE_PATH
    user_cfg_file_path _ os.path.join(user_cfg_path, 'mynk.cfg')
    if not os.path.isdir(user_cfg_path):
      ___
        os.makedirs(user_cfg_path)
        LOG.i..("Created initial user config: %s" % user_cfg_file_path)
      _______
        if not os.path.isdir(user_cfg_path):
          raise
    if not os.path.exists(user_cfg_file_path):
      shutil.copy(default_cfg_file_path, user_cfg_file_path)
    return user_cfg_file_path

