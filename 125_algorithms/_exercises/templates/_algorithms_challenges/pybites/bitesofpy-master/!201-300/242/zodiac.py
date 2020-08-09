from collections ______ namedtuple
from datetime ______ datetime
from operator ______ itemgetter
from typing ______ List

Sign = namedtuple('Sign', 'name compatibility famous_people sun_dates')


___ get_signs(data: list) -> List[Sign]:
    ret = []
    for sign in data:
        name = sign['name']
        compatibility = sign['compatibility']
        famous_people = sign['famous_people']
        sun_dates = sign['sun_dates']
        sign = Sign(name, compatibility, famous_people, sun_dates)
        ret.append(
            sign
        )
    r_ ret


___ get_sign_with_most_famous_people(signs: list
    """Get the sign with the most famous people associated"""
    famous_people = [
        (s.name, le.(s.famous_people)) for s in signs
    ]
    r_ max(famous_people, key=itemgetter(1))


___ signs_are_mutually_compatible(signs: list, sign1: str, sign2: str) -> bool:
    """Given 2 signs return if they are compatible (compatibility field)"""
    ret = False
    for sign in signs:
        __ sign.name __ sign1:
            ret = sign2 in sign.compatibility
        ____ sign.name __ sign2:
            ret = sign1 in sign.compatibility
    r_ ret


___ get_sign_by_date(signs: list, date: datetime) -> str:
    """Given a date return the right sign (sun_dates field)"""
    year = date.year
    for sign in signs:
        start, end = sign.sun_dates
        start_dt = datetime.strptime(start, '%B %d').replace(year=year)
        end_dt = datetime.strptime(end, '%B %d').replace(year=year)
        __ end_dt < start_dt:
            __ date <= end_dt:
                start_dt = datetime.strptime(start, '%B %d').replace(year=year-1)
            ____
                end_dt = datetime.strptime(end, '%B %d').replace(year=year+1)
        __ start_dt <= date <= end_dt:
            r_ sign.name