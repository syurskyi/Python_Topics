Python Logging Samples
==================

Some example setups for Python 2.6- and 3-compatible logging.

You can use these as a point-of-entry to a program by importing your modules at the end of main and then just creating loggers where needed, or you can roll your own using these as examples.  I know for a fact that the JSON-style for logging DictConfigs is not very well documented, so this might help you out even if you're rolling your own.

Call from a command-line interface with `python main.py`.  You can turn on the debug logger at the INFO level with a -v argument, and additional v's increase the logging level of the debug logger.  The stdout logger defaults to the INFO level, and the warning file output defaults to the WARN level.

Enjoy!