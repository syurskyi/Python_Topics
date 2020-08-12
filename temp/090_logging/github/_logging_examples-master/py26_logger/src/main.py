#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Python2.6+ compatible logging setup module to be used as point-of-entry to a
program."""

______ __
______ optparse
______ ?
______ ?.config

______ example_package.example_module
# We imported example_module before setting logging configuration.
# This can cause issues, see the module for explanation.


___ run():
    load_logging_conf('logging.conf')
    # All loggers MUST be started AFTER this point, including for imported modules!
    # Start the logger for this module.
    log _ ?.gL..( -n)

    opts, args _ parse_cli_args()

    set_debug_verbosity(opts.verbose)

    log.d..('test d.. m..')
    log.i..('test i.. m..')
    log.w..('test w.. m..')
    log.e..('test error m..')
    log.c..('test c.. m..')

    example_package.example_module.do_stuff()


___ load_logging_conf(log_cfg_filename):
    """Load logging configuration at '<src_dir>/../logs/<filename>' (os agnostic)."""
    src_dir _ __.path.dirname(__.path.realpath( -f))
    cfg_file_path _ __.sep.j..((src_dir, '..', 'logs', log_cfg_filename))

    ?.config.fC..(cfg_file_path)


___ parse_cli_args():
    """Parse command line args.  Additional options can be added."""
    parser _ optparse.OptionParser()
    parser.add_option('-v', '--verbose', dest_"verbose",
                      action_'count', default_0,
                      help_'increase d.. logging level')

    r_ parser.parse_args()

___ set_debug_verbosity(verbosity_counter):
    """Deactivates the d.. handler __ verbosity_counter is 0, else sets
    the logging level appropriately."""

    debug_handler _ ?.root.handlers[1]

    __ verbosity_counter __ 0:
        ?.root.removeHandler(debug_handler)
    elif verbosity_counter __ 1:
        debug_handler.level _ ?.I..
    elif verbosity_counter __ 2:
        debug_handler.level _ ?.D..
    else:
        debug_handler.level _ ?.NOTSET


__  -n __ '__main__':
    run()
