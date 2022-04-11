# nice snippet: https://gist.github.com/tonybruess/9405134
____ c.. _______ n..
_______ __

social_platforms """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator n..('Validator', 'range regex')


___ parse_social_platforms_string
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    result d..()
    plat __.f..(r'(\w+)\s+Min: (\d+)\s+Max: (\d+)\s+Can contain: ([^\r\n]+)', social_platforms)
    ___ p __ plat:
        result[p[0]] Validator(r..(i..(p[1]), i..(p[2], __.c..(rf'^[{__.sub(r" ", "", p[3])}]*$'
    r.. result


___ validate_username(platform, username
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators parse_social_platforms_string()
    __ platform n.. __ all_validators:
        r.. V...
    plat all_validators[platform]
    plat_range l..(username) __ plat.r..
    plat_match plat.regex.m..(username) __ n.. N..
    r.. plat_range a.. plat_match
