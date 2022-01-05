____ c.. _______ n..
____ d__ _______ d__
____ operator _______ itemgetter
____ typing _______ List

Sign = n..('Sign', 'name compatibility famous_people sun_dates')


___ get_signs(data: l..) __ List[Sign]:
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
    r.. m..(famous_people, key=itemgetter(1))


___ signs_are_mutually_compatible(signs: l.., sign1: s.., sign2: s..) __ bool:
    """Given 2 signs return if they are compatible (compatibility field)"""
    ret = F..
    ___ sign __ signs:
        __ sign.name __ sign1:
            ret = sign2 __ sign.compatibility
        ____ sign.name __ sign2:
            ret = sign1 __ sign.compatibility
    r.. ret


___ get_sign_by_date(signs: l.., date: d__) __ s..:
    """Given a date return the right sign (sun_dates field)"""
    year = date.year
    ___ sign __ signs:
        start, end = sign.sun_dates
        start_dt = d__.strptime(start, '%B %d').r.. y.._year)
        end_dt = d__.strptime(end, '%B %d').r.. y.._year)
        __ end_dt < start_dt:
            __ date <= end_dt:
                start_dt = d__.strptime(start, '%B %d').r.. y.._year-1)
            ____:
                end_dt = d__.strptime(end, '%B %d').r.. y.._year+1)
        __ start_dt <= date <= end_dt:
            r.. sign.name