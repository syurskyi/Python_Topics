____ d__ _______ date
____ typing _______ Dict, Sequence, NamedTuple
____ collections _______ defaultdict

class MovieRented(NamedTuple):
    title: s..
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


___ collect_totals(renting_history: RentingHistory) -> Dict[s.., int]:
    '''Creates a dictionary containing totals per month, with keys
    YYYY-MM and values (int) of the total cost for that month and year.
    '''
    totals = defaultdict(l....: 0)
    ___ movie __ renting_history:
        totals[movie.date.strftime('%Y-%m')] += movie.price
    r.. totals


___ rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[s.., s..]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    r.. {key: RENT __ value <= STREAMING_COST_PER_MONTH ____ STREAM
            ___ key, value __ collect_totals(renting_history).items()}
