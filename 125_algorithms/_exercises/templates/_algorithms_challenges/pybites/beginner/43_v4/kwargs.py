___ get_profile(*args, **kwargs) -> str:
    name = profession = None
    for kw in kwargs:
        __ kw == 'name':
            name = kwargs['name']
        elif kw == 'profession':
            profession = kwargs['profession']
        else:
            raise TypeError
    __ name is None:
        name = 'julian'
    __ profession is None:
        profession = 'programmer'
    __ type(profession) != str or type(name) != str or len(args) > 0:
        raise TypeError
    return f'{name} is a {profession}'
