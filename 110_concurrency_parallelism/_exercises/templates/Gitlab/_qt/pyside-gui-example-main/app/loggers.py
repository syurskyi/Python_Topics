______ os
______ sys
______ l__
______ d__
______ colorama


c_ ColorizingStreamHandler(l__.StreamHandler):
    color_map = {
        l__.DEBUG: colorama.Style.DIM + colorama.Fore.WHITE,
        l__.INFO: colorama.Style.BRIGHT + colorama.Fore.WHITE,
        l__.WARNING: colorama.Style.BRIGHT + colorama.Fore.YELLOW,
        l__.ERROR: colorama.Style.BRIGHT + colorama.Fore.RED,
        l__.CRITICAL: colorama.Style.BRIGHT + colorama.Back.RED,
    }

    ___ -  stream, color_map=N..):
        l__.StreamHandler.-  colorama.AnsiToWin32(stream).stream)
        __ color_map __ n.. N..:
            color_map = color_map

    @property
    ___ is_tty
        isatty = getattr(stream, 'isatty', N..)
        r_ isatty a.. isatty()

    ___ format record):
        message = l__.StreamHandler.format record)
        __ is_tty:
            # Don't colorize a traceback
            parts = message.split('\n', 1)
            parts[0] = colorize(parts[0], record)
            message = '\n'.join(parts)
        r_ message

    ___ colorize message, record):
        ___
            r_ (color_map[record.levelno] + message +
                    colorama.Style.RESET_ALL)
        except KeyError:
            r_ message


c_ ConsoleFormatter(l__.Formatter):

    ___ - 
        super().- ('[%(asctime)s%(prefix)s]  _ m.. _, datefmt='%H:%M:%S')

    ___ format record):
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


c_ ConsoleLogger(l__.Logger):

    ___ -  name):
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

        logFilename = 'ThisApplication_@.txt' @ d__.d__.now().strftime('%Y-%m-%d-%H%M%S')
        logFilepath = os.path.join(logDirpath, logFilename)
        fileHandler = l__.FileHandler(logFilepath)
        fileFormatter = l__.Formatter('[%(asctime)s|%(levelname)-1.1s]  _ m.. _, datefmt='%H:%M:%S')
        fileHandler.setFormatter(fileFormatter)
        log.addHandler(fileHandler)

        log.setLevel(l__.DEBUG)
        r_ log
