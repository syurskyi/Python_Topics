# Trace Options
# The constructor for Trace takes several optional parameters to control runtime behavior.
#
# count
# Boolean. Turns on line number counting. Defaults to True.
# countfuncs
# Boolean. Turns on list of functions called during the run. Defaults to False.
# countcallers
# Boolean. Turns on tracking for callers and callees. Defaults to False.
# ignoremods
# Sequence. List of modules or packages to ignore when tracking coverage. Defaults to an empty tuple.
# ignoredirs
# Sequence. List of directories containing modules or packages to be ignored. Defaults to an empty tuple.
# infile
# Name of the file containing cached count values. Defaults to None.
# outfile
# Name of the file to use for storing cached count files. Defaults to None, and data is not stored.