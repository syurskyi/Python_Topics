import logging

class Some:
    def __init__(self):
        # The same instance as in app.py is returned as long getLogger is
        # Called with the same name
        self.logger = logging.getLogger('app_name')

    def do_it(self):
        self.logger.critical('Something critical happend')
