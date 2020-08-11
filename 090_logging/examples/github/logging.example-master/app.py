from log import Log
from some_module import Some
import logging


class App:
    def __init__(self):
        self.logger = logging.getLogger('app_name')

    def do_something(self):
        self.logger.debug('Cut off by logger.setLevel')
        self.logger.warning('Log only to file')
        self.logger.error('log to both file and console')


# Customize how the logger behaves
log = Log()
log.setup_logging()

my_app = App()
my_app.do_something()

my_some = Some()
my_some.do_it()

# Log to Console
# 2018-03-08 21:29:42,846 - app.py - ERROR - log to both file and console
# 2018-03-08 21:29:42,846 - some_module.py - CRITICAL - Something critical happend

# Log to my_app.log
# 2018-03-08 21:29:42,846 - app.py - WARNING - Log only to file
# 2018-03-08 21:29:42,846 - app.py - ERROR - log to both file and console
# 2018-03-08 21:29:42,846 - some_module.py - CRITICAL - Something critical happend
