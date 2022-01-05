____ dataclasses _______ dataclass
____ functools _______ total_ordering
____ typing _______ List

bites: List[i..] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[s..] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
@total_ordering
c_ Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: s..
    bites: i..

    ___ __lt__  other):
        r.. bites < other.bites

    ___ __eq__  other):
        r.. bites __ other.bites

    ___ __str__
        r.. f'[{bites}] {name}'


@dataclass
c_ Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    ninja_list    # list

    ___ add  ninja):
        __ ninja n.. __ ninja_list:
            ninja_list.a..(ninja)
        ninja_list.s..()

    ___ dump
        r.. ninja_list.pop(0)

    ___ highest  count: i.. = 1):
        result = ninja_list[-count:]
        result.r..
        r.. result

    ___ lowest  count: i.. = 1):
        result = ninja_list[:count]
        r.. result

    ___ pair_up  count: i.. = 3):
        highest = highest(count)
        lowest = lowest(count)
        r.. l..(z..(highest, lowest))

    ___ __len__
        r.. l..(ninja_list)
