from datetime import date
from typing import Dict, Sequence, NamedTuple


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


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
    movie_history = {}
    for movie in renting_history:
        movie_date = movie.date.strftime("%Y-%m")
        __ movie_date not in movie_history:
            movie_history[movie_date] = [movie.price]
        else:
            movie_history[movie_date].append(movie.price)

    for key, value in movie_history.items():
        __ sum(value) <= streaming_cost_per_month:
            movie_history[key] = "rent"
        else:
            movie_history[key] = "stream"

    return movie_history


__ __name__ == "__main__":
    rent_or_stream([MovieRented('Mad Max Fury Road', 4, date(2020, 12, 17)),
     MovieRented('Die Hard', 4, date(2020, 12, 3)),
     MovieRented('Wonder Woman', 4, date(2020, 12, 28))])