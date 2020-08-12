# mynk -- a python library for enhancing a user's experience/workspace
# with the foundry's nuke
#
# @author: Robert Moggach <rob@moggach.com>
#
# mynk/constants.py -- a place for constants.  per MyNk specification,
#   constants take their value from the calling program environment
#   (__ available), and default to the the expected values.
#

______ __
______ inspect
______ sys
______ errno

____ . ______ LOG
____ .internal ______ _MODULE_PATH

___
  # Set the default unicode charset to be utf8
  MYNK_CHARSET _ __.environ.get("MYNK_CHARSET", u'utf8')
  
  # Set the mynk delimiter to be an underscore
  MYNK_DELIMITER _ __.environ.get("MYNK_DELIMITER", u'_')
  
  # Set the module's path attribute
  MYNK_PATH _ __.environ.get("MYNK_PATH", _MODULE_PATH)
  
  # For convenience set the dotnuke folder location
  DOTNUKE_PATH _ __.path.expanduser('~/.nuke')
  
  # If we want more debugging set the MYNK_DEVEL environment variable
  MYNK_DEVEL _ True __ __.environ.get("MYNK_DEVEL", False) __ ['1', 'true', 'True'] else False
  LOG.d..(u'MYNK_DEVEL attribute is {0}'.f..(MYNK_DEVEL) )

_____ ValueError, e:
  LOG.e..(errno.EINVAL, e.m..)

