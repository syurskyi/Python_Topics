from datetime import date
from typing import Dict, Sequence, NamedTuple
from collections import defaultdict

class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def collect_totals(renting_history: RentingHistory) -> Dict[str, int]:
    '''Creates a dictionary containing totals per month, with keys
    YYYY-MM and values (int) of the total cost for that month and year.
    '''
    totals = defaultdict(lambda: 0)
    for movie in renting_history:
        totals[movie.date.strftime('%Y-%m')] += movie.price
    return totals


def rent_or_stream(
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
    return {key: RENT if value <= STREAMING_COST_PER_MONTH else STREAM
            for key, value in collect_totals(renting_history).items()}
