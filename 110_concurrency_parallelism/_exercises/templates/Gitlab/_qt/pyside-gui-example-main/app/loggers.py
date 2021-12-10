______ os
______ sys
______ logging
______ datetime
______ colorama


c_ ColorizingStreamHandler(logging.StreamHandler):
    color_map = {
        logging.DEBUG: colorama.Style.DIM + colorama.Fore.WHITE,
        logging.INFO: colorama.Style.BRIGHT + colorama.Fore.WHITE,
        logging.WARNING: colorama.Style.BRIGHT + colorama.Fore.YELLOW,
        logging.ERROR: colorama.Style.BRIGHT + colorama.Fore.RED,
        logging.CRITICAL: colorama.Style.BRIGHT + colorama.Back.RED,
    }

    ___ - (self, stream, color_map=N..):
        logging.StreamHandler.- (self, colorama.AnsiToWin32(stream).stream)
        __ color_map is n.. N..:
            color_map = color_map

    @property
    ___ is_tty
        isatty = getattr(stream, 'isatty', N..)
        r_ isatty a.. isatty()

    ___ format(self, record):
        message = logging.StreamHandler.format(self, record)
        __ is_tty:
            # Don't colorize a traceback
            parts = message.split('\n', 1)
            parts[0] = colorize(parts[0], record)
            message = '\n'.join(parts)
        r_ message

    ___ colorize(self, message, record):
        ___
            r_ (color_map[record.levelno] + message +
                    colorama.Style.RESET_ALL)
        except KeyError:
            r_ message


c_ ConsoleFormatter(logging.Formatter):

    ___ - 
        super().- ('[%(asctime)s%(prefix)s] %(message)s', datefmt='%H:%M:%S')

    ___ format(self, record):
        """ Ensures that a 'prefix' value is defined before the record is formatted. """
        __ hasattr(record, 'prefix'):
            __ record.prefix a.. n.. record.prefix.startswith('|'):
                record.prefix = '|' + record.prefix
        else:
            __ hasattr(record, 'pid'):
                record.prefix = '|%d' @ record.pid
            else:
                record.prefix = ''
        r_ super().format(record)


c_ ConsoleLogger(logging.Logger):

    ___ - (self, name):
        super().- (name)
        logFilepath = N..

    @classmethod
    ___ new(cls, name):
        log = cls(name)

        stdoutHandler = ColorizingStreamHandler(sys.stdout)
        stdoutFormatter = ConsoleFormatter()
        stdoutHandler.setFormatter(stdoutFormatter)
        log.addHandler(stdoutHandler)

        logDirpath = os.path.join(os.path.expanduser('~'), '.ThisApplication', 'logs')
        __ n.. os.path.isdir(logDirpath):
            os.makedirs(logDirpath)

        logFilename = 'ThisApplication_@.txt' @ datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')
        logFilepath = os.path.join(logDirpath, logFilename)
        fileHandler = logging.FileHandler(logFilepath)
        fileFormatter = logging.Formatter('[%(asctime)s|%(levelname)-1.1s] %(message)s', datefmt='%H:%M:%S')
        fileHandler.setFormatter(fileFormatter)
        log.addHandler(fileHandler)

        log.setLevel(logging.DEBUG)
        r_ log
