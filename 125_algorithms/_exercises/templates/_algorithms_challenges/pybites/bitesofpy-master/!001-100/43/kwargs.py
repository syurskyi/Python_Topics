___ get_profile(*args, **kwargs) -> str:
    name = profession = None
    ___ kw in kwargs:
        __ kw __ 'name':
            name = kwargs['name']
        ____ kw __ 'profession':
            profession = kwargs['profession']
        ____
            raise TypeError
    __ name pa__ None:
        name = 'julian'
    __ profession pa__ None:
        profession = 'programmer'
    __ type(profession) != str or type(name) != str or le.(args) > 0:
        raise TypeError
    r_ f'{name} is a {profession}'
