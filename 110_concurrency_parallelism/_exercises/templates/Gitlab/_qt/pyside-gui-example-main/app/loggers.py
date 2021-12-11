______ __
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

    ___ f.. record):
        message = l__.StreamHandler.f.. record)
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
        _____ KeyError:
            r_ message


c_ ConsoleFormatter(l__.Formatter):

    ___ - 
        s__().- ('[%(asctime)s%(prefix)s]  _ m.. _, datefmt='%H:%M:%S')

    ___ f.. record):
        """ Ensures that a 'prefix' value is defined before the record is formatted. """
        __ hasattr(record, 'prefix'):
            __ record.prefix a.. n.. record.prefix.startswith('|'):
                record.prefix = '|' + record.prefix
        ____
            __ hasattr(record, 'pid'):
                record.prefix = '|%d' @ record.pid
            ____
                record.prefix = ''
        r_ s__().f..(record)


c_ ConsoleLogger(l__.Logger):

    ___ -  name):
        s__().- (name)
        logFilepath = N..

    @classmethod
    ___ new(cls, name):
        log = cls(name)

        stdoutHandler = ColorizingStreamHandler(sys.stdout)
        stdoutFormatter = ConsoleFormatter()
        stdoutHandler.setFormatter(stdoutFormatter)
        log.addHandler(stdoutHandler)

        logDirpath = __.path.join(__.path.expanduser('~'), '.ThisApplication', 'logs')
        __ n.. __.path.isdir(logDirpath):
            __.makedirs(logDirpath)

        logFilename = 'ThisApplication_@.txt' @ d__.d__.now().strftime('%Y-%m-%d-%H%M%S')
        logFilepath = __.path.join(logDirpath, logFilename)
        fileHandler = l__.FileHandler(logFilepath)
        fileFormatter = l__.Formatter('[%(asctime)s|%(levelname)-1.1s]  _ m.. _, datefmt='%H:%M:%S')
        fileHandler.setFormatter(fileFormatter)
        log.addHandler(fileHandler)

        log.setLevel(l__.DEBUG)
        r_ log
