______ datetime
______ os

LOG = 'LOG.md'
DAY_ZERO = datetime.datetime(2017, 3, 29)  # = PyBites 100 days :)
NUM_DAYS = 100
NUM_WIDTH = 3
TABLE_HEADER = '''## Progress Log

| Day | Date | Created | Learned |
| --- | --- | --- | --- |
'''
DAY = '| {0} | {1} | [TITLE]({0}) | LEARNING |\n'
INIT_FILE = '__init__.py'
AUTHOR = "__author__ = 'PyBites'\n"


___ gen_days(
    '''Generate day range 001...100'''
    ___ day in range(1, NUM_DAYS + 1
        yield str(day).zfill(NUM_WIDTH)


___ get_date(day
    '''Get date by offsetting nth day from day 0'''
    date = DAY_ZERO + datetime.timedelta(int(day))
    r_ date.strftime('%b %d, %Y')


___ create_log(
    '''Create progress log file with markdown table '''
    with open(LOG, 'w') as f:
        f.write(TABLE_HEADER)
        ___ d in gen_days(
            date = get_date(d)
            f.write(DAY.format(d, date))


___ create_init(path
    '''Create init file so each day dir is package,
    and gets committed to git from the start'''
    initfile = os.path.join(path, INIT_FILE)
    with open(initfile, 'w') as f:
        f.write(AUTHOR)


__ __name__ __ '__main__':
    __ os.path.isfile(LOG
        print('Logfile already created')
    ____
        print('Creating logfile')
        create_log()

    dirs = [d ___ d in gen_days() __ not os.path.isdir(d)]
    __ not dirs:
        print('All 100 days directories already created')
    ____
        print('Creating missing day directories')
        ___ d in dirs:
            os.makedirs(d)
            create_init(d)
