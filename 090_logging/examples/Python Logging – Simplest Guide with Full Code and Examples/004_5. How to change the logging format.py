# The logging module provides shorthands to add various details to the logged messages. The below image from Python
# docs shows that list.
# Lets change the log message format to show the TIME, LEVEL and the MESSAGE. To do that just add the format to
# logging.basiconfig() s format argument.

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
logging.info("Just like that!")
#> 2019-02-17 11:40:38,254 :: INFO :: Just like that!