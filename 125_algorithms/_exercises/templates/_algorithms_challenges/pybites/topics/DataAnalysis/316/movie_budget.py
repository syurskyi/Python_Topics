____ d__ _______ date
____ t___ _______ Dict, S.., N..
____ c.. _______ d..



c_ MovieRented(N..
    title: s..
    price: i..
    date: date


RentingHistory S..[MovieRented]
STREAMING_COST_PER_MONTH 12
STREAM, RENT 'stream', 'rent'


___ rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: i.. STREAMING_COST_PER_MONTH
) __ Dict[s.., s..]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    month_rental d..(i..)
    return_dict d..(s..)
    ___ movie __ renting_history:
        month_rental[getattr(movie,'date').s..("%Y-%m")] += getattr(movie,'price')
    ___ total_month __ s..(month_rental
        __ month_rental[total_month] > STREAMING_COST_PER_MONTH:
            return_dict[total_month] STREAM
        ____
            return_dict[total_month] RENT
    r.. return_dict



renting_history [
    MovieRented('Breach', 7, date(2020, 12, 1,
    MovieRented('Sonic', 10, date(2020, 11, 4,
    MovieRented('Die Hard', 3, date(2020, 11, 3,
    MovieRented('Love and Monsters', 5, date(2020, 12, 9 ]

print(rent_or_stream(renting_history
