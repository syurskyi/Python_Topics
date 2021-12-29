___ get_profile(*args, **kwargs) -> s..:
    name = profession = N..
    ___ kw __ kwargs:
        __ kw __ 'name':
            name = kwargs['name']
        ____ kw __ 'profession':
            profession = kwargs['profession']
        ____:
            raise TypeError
    __ name __ N..
        name = 'julian'
    __ profession __ N..
        profession = 'programmer'
    __ type(profession) != s.. o. type(name) != s.. o. l..(args) > 0:
        raise TypeError
    r.. f'{name} is a {profession}'
