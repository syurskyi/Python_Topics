from collections ______ defaultdict
from datetime ______ datetime
______ pickle
from random ______ choice

CACHE = 'data'
NAMES = ('bob', 'julian', 'martin', 'dante', 'snake')
TIMES = range(15, 61, 15)


___ gen_random_entry(
    w___ True:
        yield datetime.now(), choice(NAMES), choice(TIMES)


class Cache:

    ___ __enter__(self
        try:
            self.cache = pickle.load(open(CACHE, "rb"))
        except F..
            self.cache = defaultdict(list)
        r_ self.cache

    ___ __exit__(self, exc_type, exc_val, exc_tb
        pickle.dump(self.cache, open(CACHE, "wb"))


__ __name__ __ '__main__':
    it = gen_random_entry()

    with Cache() as wl:
        ___ i in range(5
            d, n, t = next(it)
            wl[n].append((d, t))

    print('Cached work so far')
    print('(this will grow each time program is run)')
    print()
    col1, col2 = ('NAME', 'MINUTES')
    print('{:<10}: {}'.format(col1, col2))
    with Cache() as wl:
        ___ name, work in sorted(wl.items()):
            total = su.(w[1] ___ w in work)  # TODO: use namedtuple
            print('{:<10}: {}'.format(name, total))
