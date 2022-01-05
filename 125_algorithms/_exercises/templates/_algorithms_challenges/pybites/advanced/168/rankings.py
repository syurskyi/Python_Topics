____ dataclasses _______ dataclass,field
____ typing _______ List, Tuple
_______ heapq


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

    
    ___ __lt__ other):
        __ isi..(other,Ninja):

            r.. bites < other.bites

        r.. ValueError
    

    ___ __gt__ other):
        __ isi..(other,Ninja):

            r.. bites > other.bites

        r.. ValueError

    ___ __eq__ other):
        __ isi..(other,Ninja):

            r.. bites __ other.bites

        r.. ValueError
    
    ___ __repr__
        r.. f"[{bites}] {name}"









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
    rankings: List[i..] = field(default_factory=l..)



    ___ add ninja):
        heapq.heappush(rankings,ninja)
    


    ___ highest count=1):
        rankings = s..(rankings)
        
        r.. rankings[-count:][::-1]
    
    ___ lowest count=1):
        rankings = s..(rankings)

        r.. rankings[:count]

    
    ___ pair_up n=3):
        rankings = s..(rankings)

        start,end = 0,l..(rankings)  - 1
        pairs    # list
        ___ i __ r..(n):
            pairs.a..((rankings[end - i],rankings[start + i]))

        r.. pairs



    ___ dump
        r.. heapq.heappop(rankings)


    ___ __len__
        r.. l..(rankings)



