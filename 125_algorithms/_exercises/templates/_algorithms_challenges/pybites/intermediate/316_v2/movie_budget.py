____ d__ _______ date
____ t___ _______ Dict, S.., N..
____ c.. _______ n..,d..



MovieRented = n..("MovieRented","title price date")
'''
class MovieRented(NamedTuple):
    title: str
    price: int
    date: date
'''


RentingHistory = S..[MovieRented]
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
    

    m = d..(i..)


    ___ movie_rented __ renting_history:
        month = movie_rented.date.s..("%Y-%m")
        m[month] += movie_rented.price
    
    

    ___ month,cost __ m.i..:
        __ cost > streaming_cost_per_month:
            m[month] = STREAM
        ____:
            m[month] = RENT


    r.. m



        



