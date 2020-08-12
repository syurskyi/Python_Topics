# mynk -- a python library for enhancing a user's experience/workspace
# with the foundry's nuke
#
# @author: Robert Moggach <rob@moggach.com>
#
# mynk/__init__.py -- wraps mynk in a bow
#


# logger relies on: constants
______ ?
from logger ______ MyNkLogger
LOG _ MyNkLogger().LOG

# constants relies on: exceptions, LOG, internal
______ constants

# const relies on: constants, exceptions, internal
from const ______ const, set_const

# config relies on: constants
from config ______ MyNkConfig
config _ MyNkConfig().config

# gui relies on: constants, config
from gui ______ MyNkGui
gui _ MyNkGui()

# formats relies on: constants, config
______ formats

# tools relies on: constants, config
from tools ______ MyNkTools
tools _ MyNkTools()

# knobs relies on: constants, config
______ knobs


__all__ _ [ 'constants', 'const', 'set_const', 'LOG', 'config', 'gui', 'formats', 'tools', 'knobs', ]

__name__ _ 'mynk'