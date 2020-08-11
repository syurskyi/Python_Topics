import logging
import logging.handlers


class Log:
    def __init__(self):
        pass

    def setup_logging(self):
        formt = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(formt)

        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        ch.setFormatter(formatter)

        fh = logging.handlers.RotatingFileHandler('./my_app.log')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        logger = logging.getLogger('app_name')
        # logger.setLevel must be lower than setLevel for all other handlers,
        # otherwise it will cut off before reaching the other handlers
        logger.setLevel(logging.INFO)
        logger.addHandler(ch)
        logger.addHandler(fh)
