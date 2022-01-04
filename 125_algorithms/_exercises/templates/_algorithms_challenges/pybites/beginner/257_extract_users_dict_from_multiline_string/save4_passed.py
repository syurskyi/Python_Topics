_______ __

___ get_users(passwd: s..) __ d..:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    passwd = passwd.splitlines()
    passwd = [line ___ line __ passwd __ line.s..]
    keys    # list
    values    # list
    ___ p __ passwd:
        keys.a..(p.s..(':')[0])
        __ l..(p.s..(':')[4]) __ 0:
            values.a..('unknown')
        ____:
            values.a..(' '.j..(
                __.sub(',',' ', p.s..(':')[4]).s..()))
    r.. d..(z..(keys, values))