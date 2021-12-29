from dataclasses import dataclass,field
from typing import List, Tuple
import heapq


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

    
    def __lt__(self,other):
        if isinstance(other,Ninja):

            return self.bites < other.bites

        raise ValueError
    

    def __gt__(self,other):
        if isinstance(other,Ninja):

            return self.bites > other.bites

        raise ValueError

    def __eq__(self,other):
        if isinstance(other,Ninja):

            return self.bites == other.bites

        raise ValueError
    
    def __repr__(self):
        return f"[{self.bites}] {self.name}"









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
    rankings: List[int] = field(default_factory=list)



    def add(self,ninja):
        heapq.heappush(self.rankings,ninja)
    


    def highest(self,count=1):
        rankings = sorted(self.rankings)
        
        return rankings[-count:][::-1]
    
    def lowest(self,count=1):
        rankings = sorted(self.rankings)

        return rankings[:count]

    
    def pair_up(self,n=3):
        rankings = sorted(self.rankings)

        start,end = 0,len(rankings)  - 1
        pairs = []
        for i in range(n):
            pairs.append((rankings[end - i],rankings[start + i]))

        return pairs



    def dump(self):
        return heapq.heappop(self.rankings)


    def __len__(self):
        return len(self.rankings)



