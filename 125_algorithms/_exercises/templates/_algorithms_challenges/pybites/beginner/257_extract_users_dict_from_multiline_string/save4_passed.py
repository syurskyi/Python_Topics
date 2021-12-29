_______ re

___ get_users(passwd: str) -> d..:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    passwd = passwd.splitlines()
    passwd = [line ___ line __ passwd __ line.strip()]
    keys    # list
    values    # list
    ___ p __ passwd:
        keys.a..(p.split(':')[0])
        __ l..(p.split(':')[4]) __ 0:
            values.a..('unknown')
        ____:
            values.a..(' '.join(
                re.sub(',',' ', p.split(':')[4]).split()))
    r.. d..(zip(keys, values))