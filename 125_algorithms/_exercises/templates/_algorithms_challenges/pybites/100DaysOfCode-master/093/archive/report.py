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
    ___ key, count __ counter.most_common(TOP
        print(FMT.format(key, count))
    print()
