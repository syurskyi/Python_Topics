___ get_profile(**kwargs):
    for key in kwargs:
        __ key not in ['name', 'profession']:
            raise TypeError
    return f"{kwargs.get('name', 'julian')} is a {kwargs.get('profession', 'programmer')}"