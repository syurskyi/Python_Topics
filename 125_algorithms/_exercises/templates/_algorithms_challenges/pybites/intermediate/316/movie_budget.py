____ d__ _______ date
____ typing _______ Dict, Sequence, NamedTuple


c_ MovieRented(NamedTuple):
    title: s..
    price: i..
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


___ rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: i.. = STREAMING_COST_PER_MONTH
) __ Dict[s.., s..]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    movie_history    # dict
    ___ movie __ renting_history:
        movie_date = movie.date.s..("%Y-%m")
        __ movie_date n.. __ movie_history:
            movie_history[movie_date] = [movie.price]
        ____:
            movie_history[movie_date].a..(movie.price)

    ___ key, value __ movie_history.i..:
        __ s..(value) <= streaming_cost_per_month:
            movie_history[key] = "rent"
        ____:
            movie_history[key] = "stream"

    r.. movie_history


__ _______ __ _______
    rent_or_stream([MovieRented('Mad Max Fury Road', 4, date(2020, 12, 17)),
     MovieRented('Die Hard', 4, date(2020, 12, 3)),
     MovieRented('Wonder Woman', 4, date(2020, 12, 28))])