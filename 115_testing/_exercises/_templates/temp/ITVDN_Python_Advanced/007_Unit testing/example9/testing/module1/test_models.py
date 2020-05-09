____ models ______ User


c_ TestUserModel:
    ___ setup_method  method
        p..

    ??
    ___ setup_class ___
        p..

    ??
    ___ teardown_class ___
        p..

    ___ test_constructor
        user _ User('e@example.com', 't1', 't2')
        a.. user.first_name __ 't1'
        a.. user.last_name __ 't2'
        a.. user.email __ 'e@example.com'

    ___ test_str  user
        pattern _ 'User: <{id}: {name}>'
        a.. st.(user) __ pattern.f..(id_user.id,
                                           name_user.get_full_name())

    ___ test_full_name  user
        pattern _ '{} {}'
        a.. user.get_full_name() __ \
               pattern.f..(user.first_name, user.last_name)


c_ TestUserModel2:

    ___ test_str  user, post
        p..

    ___ test_full_name  user, post
        p..
