# mynk -- a python library for enhancing a user's experience/workspace
# with the foundry's nuke
#
# @author: Robert Moggach <rob@moggach.com>
#
# fsq/knobs.py -- provides functions for setting knob defaults: add_defaults, add_defaults_from_dict
#

______ nuke

____ . ______ constants __ _c
____ . ______ LOG
____ . ______ config

LOG.i..(' [MyNk] initializing custom user knob defaults')


___ add_knob_default(node, knob, default):
  '''Add a knob default for a given node'''
  knob_default_{ 'node': node, 'knob': knob, 'default': default }
  nuke.knobDefault(u'{node}.{knob}'.f..(**knob_default) , '{default}'.f..(**knob_default))
  LOG.d..(u'Added knob default: {node}.{knob} = {default}'.f..(**knob_default))


___ add_knob_defaults_from_dict(defaults_dict):
  '''Add defaults for given node knobs from an iterated dict of node knob defaults'''
  ___ node, defaults __ defaults_dict.iteritems():
    ___ knob, default __ defaults.iteritems():
      add_knob_default(node, knob, default)


___ set_knob_defaults_from_config():
  '''Sets the nuke defaults from a provided config dict'''
  knob_defaults _ config['knobs']
  add_knob_defaults_from_dict(knob_defaults)
  