___ get_profile(name, age, *args, **kwargs
    return_dict    # dict
    __ args:
        return_dict 'sports'  = s..(l..(a..
    __ (isi..(age, i.. a.. l..(args) <= 5:
        return_dict 'name'  = name
        return_dict 'age'  = age
        __ args:
            return_dict 'sports'  = s..(l..(a..
        __ kwargs:
            return_dict 'awards'  = kwargs
        r.. return_dict
    ____:
        r.. V...


#print(get_profile('tim', 36, 'tennis', 'basketball', 'archery', 'soccer', 'badminton', champ='helped out team in crisis', winner='python') )
print(get_profile('tim', 36, 'tennis') )