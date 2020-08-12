# mynk -- a python library for enhancing a user's experience/workspace
# with the foundry's nuke
#
# @author: Robert Moggach <rob@moggach.com>
#
# mynk/formats.py -- provides functions for setting image format defaults: add_format, add_formats_from_dict
#

______ nuke

____ . ______ constants __ _c
____ . ______ LOG
____ . ______ config

LOG.i..(' [MyNk] initializing custom user image formats')


___ add_format(W, H, x, y, r, t, pa, format_name):
  '''Add a format based on provided attributes'''
  __ no. W is None and no. H is None and no. format_name is None:
      x _ 0 __ x is None else x
      y _ 0 __ y is None else y
      r _ W __ r is None else r
      t _ H __ t is None else t
      pa _ 1 __ pa is None else pa
      format_str _ u'{0} {1} {2} {3} {4} {5} {6} {7}'.f..(W, H, x, y, r, t, pa, format_name)
      nuke.addFormat(format_str)
      msg _ u'Added format: {0}'.f..(format_str)
      LOG.d..(msg)


___ add_formats_from_dict(defaults_dict):
  '''Add nuke formats from an iterated dict of formats'''
  for format_name, f.. __ defaults_dict.iteritems():
    __ f...get('active', False) __ ['1', 'true', 'True']:
      W _ f...get('W', None)
      H _ f...get('H', None)
      x _ f...get('x', 0)
      y _ f...get('y', 0)
      r _ f...get('r', W)
      t _ f...get('r', H)
      pa _ f...get('pa', 1)
      add_format(W, H, x, y, r, t, pa, format_name)


___ add_formats_from_config():
  '''wrapper for adding formats from config dict'''
  add_formats_from_dict(config['formats'])
