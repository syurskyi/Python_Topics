____ models ______ User


c_ TestUserModel:
    ___ setup_method  method
        pass

    @classmethod
    ___ setup_class(cls
        pass

    @classmethod
    ___ teardown_class(cls
        pass

    ___ test_constructor
        user _ User('e@example.com', 't1', 't2')
        assert user.first_name == 't1'
        assert user.last_name == 't2'
        assert user.email == 'e@example.com'

    ___ test_str  user
        pattern _ 'User: <{id}: {name}>'
        assert st.(user) == pattern.f..(id_user.id,
                                           name_user.get_full_name())

    ___ test_full_name  user
        pattern _ '{} {}'
        assert user.get_full_name() == \
               pattern.f..(user.first_name, user.last_name)


c_ TestUserModel2:

    ___ test_str  user, post
        pass

    ___ test_full_name  user, post
        pass
