____ dataclasses _______ dataclass
____ functools _______ total_ordering
____ typing _______ List

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
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
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    ___ __lt__(self, other):
        r.. self.bites < other.bites

    ___ __eq__(self, other):
        r.. self.bites __ other.bites

    ___ __str__(self):
        r.. f'[{self.bites}] {self.name}'


@dataclass
class Rankings:
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

    ___ add(self, ninja):
        __ ninja n.. __ self.ninja_list:
            self.ninja_list.a..(ninja)
        self.ninja_list.sort()

    ___ dump(self):
        r.. self.ninja_list.pop(0)

    ___ highest(self, count: int = 1):
        result = self.ninja_list[-count:]
        result.reverse()
        r.. result

    ___ lowest(self, count: int = 1):
        result = self.ninja_list[:count]
        r.. result

    ___ pair_up(self, count: int = 3):
        highest = self.highest(count)
        lowest = self.lowest(count)
        r.. l..(zip(highest, lowest))

    ___ __len__(self):
        r.. l..(self.ninja_list)
