# Besides debug, info, warning, error, and critical messages, you can log exceptions that will include any
# associated traceback information.
# With logger.exception, you can log traceback information should the code encounter any error. logger.exception will log
# the message provided in its arguments as well as the error message traceback info.
#
# Below is a nice example.

import logging

# Create or get the logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.INFO)

def divide(x, y):
    try:
        out = x / y
    except ZeroDivisionError:
        logger.exception("Division by zero problem")
    else:
        return out

# Logs
logger.error("Divide {x} / {y} = {c}".format(x=10, y=0, c=divide(10,0)))

#> ERROR:__main__:Division by zero problem
#> Traceback (most recent call last):
#>   File "<ipython-input-16-a010a44fdc0a>", line 12, in divide
#>     out = x / y
#> ZeroDivisionError: division by zero
#> ERROR:__main__:None