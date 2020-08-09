TOP = 10
WIDTH = 30
FMT = '{:<20} {:>5}'


___ print_header(
    title = 'Twitter Archive report'
    print('=' * WIDTH)
    print(title.upper())
    print('=' * WIDTH)
    print()


___ print_results(title, counter
    print(title + ':')
    print('-' * WIDTH)
    for key, count in counter.most_common(TOP
        print(FMT.format(key, count))
    print()
