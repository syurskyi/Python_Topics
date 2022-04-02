_______ __
_______ pdb
___ get_users(passwd: s..) __ d..:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    
    passwords    # dict
    #pdb.set_trace()
    ___ line __ passwd.s..
        __ n.. line:
            _____
        values = line.s..(':')
        username,name = values[0],values[4]
        name = name.strip(',')
        __ name != '':
            name = __.sub(r'\,+',' ',name)
        ____:
            name = 'unknown'



        passwords[username] = name

    r.. passwords


__ _______ __ _______
    
    pw = """
postfix:x:108:112::/var/sppol/postfix
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/bin
"""

    print(get_users(pw))


