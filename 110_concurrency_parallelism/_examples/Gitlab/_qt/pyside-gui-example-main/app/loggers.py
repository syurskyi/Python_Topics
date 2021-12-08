import os
import sys
import logging
import datetime
import colorama


class ColorizingStreamHandler(logging.StreamHandler):
    color_map = {
        logging.DEBUG: colorama.Style.DIM + colorama.Fore.WHITE,
        logging.INFO: colorama.Style.BRIGHT + colorama.Fore.WHITE,
        logging.WARNING: colorama.Style.BRIGHT + colorama.Fore.YELLOW,
        logging.ERROR: colorama.Style.BRIGHT + colorama.Fore.RED,
        logging.CRITICAL: colorama.Style.BRIGHT + colorama.Back.RED,
    }

    def __init__(self, stream, color_map=None):
        logging.StreamHandler.__init__(self, colorama.AnsiToWin32(stream).stream)
        if color_map is not None:
            self.color_map = color_map

    @property
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty()

    def format(self, record):
        message = logging.StreamHandler.format(self, record)
        if self.is_tty:
            # Don't colorize a traceback
            parts = message.split('\n', 1)
            parts[0] = self.colorize(parts[0], record)
            message = '\n'.join(parts)
        return message

    def colorize(self, message, record):
        try:
            return (self.color_map[record.levelno] + message +
                    colorama.Style.RESET_ALL)
        except KeyError:
            return message


class ConsoleFormatter(logging.Formatter):

    def __init__(self):
        super().__init__('[%(asctime)s%(prefix)s] %(message)s', datefmt='%H:%M:%S')

    def format(self, record):
        """ Ensures that a 'prefix' value is defined before the record is formatted. """
        if hasattr(record, 'prefix'):
            if record.prefix and not record.prefix.startswith('|'):
                record.prefix = '|' + record.prefix
        else:
            if hasattr(record, 'pid'):
                record.prefix = '|%d' % record.pid
            else:
                record.prefix = ''
        return super().format(record)


class ConsoleLogger(logging.Logger):

    def __init__(self, name):
        super().__init__(name)
        self.logFilepath = None

    @classmethod
    def new(cls, name):
        log = cls(name)

        stdoutHandler = ColorizingStreamHandler(sys.stdout)
        stdoutFormatter = ConsoleFormatter()
        stdoutHandler.setFormatter(stdoutFormatter)
        log.addHandler(stdoutHandler)

        logDirpath = os.path.join(os.path.expanduser('~'), '.ThisApplication', 'logs')
        if not os.path.isdir(logDirpath):
            os.makedirs(logDirpath)

        logFilename = 'ThisApplication_%s.txt' % datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')
        logFilepath = os.path.join(logDirpath, logFilename)
        fileHandler = logging.FileHandler(logFilepath)
        fileFormatter = logging.Formatter('[%(asctime)s|%(levelname)-1.1s] %(message)s', datefmt='%H:%M:%S')
        fileHandler.setFormatter(fileFormatter)
        log.addHandler(fileHandler)

        log.setLevel(logging.DEBUG)
        return log
