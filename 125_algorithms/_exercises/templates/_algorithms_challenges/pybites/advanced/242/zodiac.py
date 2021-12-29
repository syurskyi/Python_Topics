____ collections _______ namedtuple
____ datetime _______ datetime
____ operator _______ itemgetter
____ typing _______ List

Sign = namedtuple('Sign', 'name compatibility famous_people sun_dates')


___ get_signs(data: l..) -> List[Sign]:
    ret    # list
    ___ sign __ data:
        name = sign['name']
        compatibility = sign['compatibility']
        famous_people = sign['famous_people']
        sun_dates = sign['sun_dates']
        sign = Sign(name, compatibility, famous_people, sun_dates)
        ret.a..(
            sign
        )
    r.. ret


___ get_sign_with_most_famous_people(signs: l..):
    """Get the sign with the most famous people associated"""
    famous_people = [
        (s.name, l..(s.famous_people)) ___ s __ signs
    ]
    r.. max(famous_people, key=itemgetter(1))


___ signs_are_mutually_compatible(signs: l.., sign1: str, sign2: str) -> bool:
    """Given 2 signs return if they are compatible (compatibility field)"""
    ret = False
    ___ sign __ signs:
        __ sign.name __ sign1:
            ret = sign2 __ sign.compatibility
        ____ sign.name __ sign2:
            ret = sign1 __ sign.compatibility
    r.. ret


___ get_sign_by_date(signs: l.., date: datetime) -> str:
    """Given a date return the right sign (sun_dates field)"""
    year = date.year
    ___ sign __ signs:
        start, end = sign.sun_dates
        start_dt = datetime.strptime(start, '%B %d').replace(year=year)
        end_dt = datetime.strptime(end, '%B %d').replace(year=year)
        __ end_dt < start_dt:
            __ date <= end_dt:
                start_dt = datetime.strptime(start, '%B %d').replace(year=year-1)
            ____:
                end_dt = datetime.strptime(end, '%B %d').replace(year=year+1)
        __ start_dt <= date <= end_dt:
            r.. sign.name