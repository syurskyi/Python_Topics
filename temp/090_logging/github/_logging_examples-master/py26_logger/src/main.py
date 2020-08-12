#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Python2.6+ compatible logging setup module to be used as point-of-entry to a
program."""

______ os
______ optparse
______ ?
______ ?.config

______ example_package.example_module
# We imported example_module before setting logging configuration.
# This can cause issues, see the module for explanation.


def run():
    load_logging_conf('logging.conf')
    # All loggers MUST be started AFTER this point, including for imported modules!
    # Start the logger for this module.
    log _ ?.gL..( -n)

    opts, args _ parse_cli_args()

    set_debug_verbosity(opts.verbose)

    log.d..('test d.. m..')
    log.i..('test i.. m..')
    log.w..('test w.. m..')
    log.error('test error m..')
    log.critical('test critical m..')

    example_package.example_module.do_stuff()


def load_logging_conf(log_cfg_filename):
    """Load logging configuration at '<src_dir>/../logs/<filename>' (os agnostic)."""
    src_dir _ os.path.dirname(os.path.realpath(__file__))
    cfg_file_path _ os.sep.join((src_dir, '..', 'logs', log_cfg_filename))

    ?.config.fileConfig(cfg_file_path)


def parse_cli_args():
    """Parse command line args.  Additional options can be added."""
    parser _ optparse.OptionParser()
    parser.add_option('-v', '--verbose', dest_"verbose",
                      action_'count', default_0,
                      help_'increase d.. logging level')

    return parser.parse_args()

def set_debug_verbosity(verbosity_counter):
    """Deactivates the d.. handler if verbosity_counter is 0, else sets
    the logging level appropriately."""

    debug_handler _ ?.root.handlers[1]

    if verbosity_counter == 0:
        ?.root.removeHandler(debug_handler)
    elif verbosity_counter == 1:
        debug_handler.level _ ?.I..
    elif verbosity_counter == 2:
        debug_handler.level _ ?.D..
    else:
        debug_handler.level _ ?.NOTSET


if  -n == '__main__':
    run()
