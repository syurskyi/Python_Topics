# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """Python3 compatible logging setup module to be used as point-of-entry to a
# program."""
#
# ______ a..
# ______ j..
# ______ ?
# ______ ?.c..
# ______ __
#
# ______ example_package.example_module
# # We imported example_module before setting logging configuration.
# # This can cause issues, see the module for explanation.
#
#
# ___ run
#     load_logging_conf 'logging.json'
#     # All loggers MUST be started AFTER this point, including for imported modules!
#     # Start the logger for this module.
#     log _ ?.gL..  -n
#
#     cli_args _ parse_cli_args()
#
#     set_debug_verbosity >.ve..
#
#     ?.d.. 'test d.. m..'
#     ?.i.. 'test i.. m..'
#     ?.w.. 'test w.. m..'
#     ?.e.. 'test error m..'
#     ?.c.. 'test c.. m..'
#
#     example_package.e_m_.d..
#
#
# ___ load_logging_conf log_cfg_filename
#     """Load logging configuration at '<src_dir>/../logs/<filename>' (os agnostic)."""
#     src_dir _ __.pa__.d.. __.pa__.r_)p.. -f
#     cfg_file_path _ __.s__.j.. s_d.. '..', 'logs', log_cfg_filename))
#
#     # This will disable all previously existing loggers.
#     w__ o.. c_f_p.. __ config_json
#         logging_config _ j__.l.. ?
#     ?.c__.dC.. ?
#
#
# ___ parse_cli_args
#     """Parse command line args.  Additional options can be added."""
#     parser _ assert.AP..
#     ?.a.. '-v', '--verbose' d.._'verbose'
#                       a.._'count', d.._0
#                       h.._'increase d.. logging level'
#
#     r_ ?.p..
#
#
# ___ set_debug_verbosity verbosity_counter
#     """Deactivates the d.. handler __ verbosity_counter is 0, else sets
#     the logging level appropriately."""
#     debug_handler _ ?.r__.h.. 1
#
#     __ ? __ 0
#         ?.r__.rH.. ?
#     ____ ? __ 1
#         ?.l.. _ ?.I..
#     ____ ? __ 2
#         ?.l.. _ ?.D..
#     ____
#         ?.l.. _ ?.N..
#
#
# __  -n __ ______
#     ?
