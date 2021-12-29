from datetime import date
from typing import Dict, Sequence, NamedTuple
from collections import namedtuple,defaultdict



MovieRented = namedtuple("MovieRented","title price date")
'''
class MovieRented(NamedTuple):
    title: str
    price: int
    date: date
'''


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


___ rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    

    m = defaultdict(int)


    for movie_rented in renting_history:
        month = movie_rented.date.strftime("%Y-%m")
        m[month] += movie_rented.price
    
    

    for month,cost in m.items():
        __ cost > streaming_cost_per_month:
            m[month] = STREAM
        else:
            m[month] = RENT


    return m



        



