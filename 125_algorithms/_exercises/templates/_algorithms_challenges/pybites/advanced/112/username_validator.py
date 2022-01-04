# nice snippet: https://gist.github.com/tonybruess/9405134
____ collections _______ n..
_______ __

social_platforms = """Twitter
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
Validator = n..('Validator', 'range regex')


___ parse_social_platforms_string
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    platforms = social_platforms.s..('\n\n')
    
    platform_to_validator    # dict
    
    ___ platform __ platforms:
        result = __.s..(r"(.+)\n.*Min: (\d+)\n.*Max: (\d+)\n.+: (.+)",platform,flags=__.M)
        
        values    # list
        ___ i __ r..(1,5):
            values.a..(result.group(i))
        platform_name = values[0]
        range_object = r..(i..(values[1]),i..(values[2]))
        last = ''.j..(values[-1].s..())
        regex = '^[' + last + ']+$'
        r = __.c..(regex)
        validator = Validator(range_object,r)
        platform_to_validator[platform_name] = validator


    r.. platform_to_validator


___ validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()

    __ platform n.. __ all_validators:
        r.. ValueError
    platform_validator = all_validators[platform]

    r.. l..(username) __ platform_validator.r.. a.. platform_validator.regex.s..(username)





parse_social_platforms_string()
