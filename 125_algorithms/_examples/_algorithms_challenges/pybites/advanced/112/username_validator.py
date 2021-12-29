# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

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
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    platforms = social_platforms.split('\n\n')
    
    platform_to_validator = {}
    
    for platform in platforms:
        result = re.search(r"(.+)\n.*Min: (\d+)\n.*Max: (\d+)\n.+: (.+)",platform,flags=re.M)
        
        values = []
        for i in range(1,5):
            values.append(result.group(i))
        platform_name = values[0]
        range_object = range(int(values[1]),int(values[2]))
        last = ''.join(values[-1].split())
        regex = '^[' + last + ']+$'
        r = re.compile(regex)
        validator = Validator(range_object,r)
        platform_to_validator[platform_name] = validator


    return platform_to_validator


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()

    if platform not in all_validators:
        raise ValueError
    platform_validator = all_validators[platform]

    return len(username) in platform_validator.range and platform_validator.regex.search(username)





parse_social_platforms_string()
