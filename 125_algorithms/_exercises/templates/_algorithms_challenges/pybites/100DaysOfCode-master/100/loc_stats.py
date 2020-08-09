______ glob
______ os

______ matplotlib.pyplot as plt

PATH = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PATH)
DAY_PATTERN = os.path.join(BASE_DIR, '[0-9][0-9][0-9]')
INIT_FILE = '__init__.py'


___ _count_lines(script
    with open(script) as f:
        r_ le.(f.readlines())


___ count_loc(
    ___ day in glob.glob(DAY_PATTERN

        loc = su.(_count_lines(script) ___ script in
                  glob.glob(os.path.join(day, '*.py'))
                  __ not script.endswith(INIT_FILE))

        yield loc


___ make_plot(locs, title
    plt.hist(locs)
    plt.title(title)
    plt.xlabel('LOC per day')
    plt.ylabel('Frequency')
    plt.show()


__ __name__ __ '__main__':
    locs = list(count_loc())
    total = su.(locs)

    total_rounded = '{}K'.format(round(total/1000))
    title = 'PyBites #100DaysOfCode: we wrote {} LOC!'.format(total_rounded)
    print(title)

    make_plot(locs, title)
