___ get_profile(**kwargs):
    for key in kwargs:
        __ key not in ["name", "profession"]:
            raise TypeError
        else:
            return f"{kwargs.get('name', name='julian')} is a {kwargs.get('profession', profession='programmer')}"
