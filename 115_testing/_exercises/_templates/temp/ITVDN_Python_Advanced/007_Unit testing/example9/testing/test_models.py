______ datetime

____ models ______ User


___ setup_method  method):
    raise ValueError


c_ TestUserModel:
    ___ setup_method  method):
        pass

    ___ teardown_method  method):
        pass

    @classmethod
    ___ setup_class(cls):
        pass

    @classmethod
    ___ teardown_class(cls):
        pass

    ___ test_constructor
        user _ User('e@example.com', 't1', 't2')
        assert user.first_name == 't1'
        assert user.last_name == 't2'
        assert user.email == 'e@example.com'

    ___ test_str  user):
        pattern _ 'User: <{id}: {name}>'
        assert str(user) == pattern.f..(id_user.id,
                                           name_user.get_full_name())

    ___ test_full_name  user):
        pattern _ '{} {}'
        assert user.get_full_name() == \
               pattern.f..(user.first_name, user.last_name)


c_ TestUserModel2:

    ___ test_constructor
        user _ User('e@example.com', 't1', 't2')
        assert user.first_name == 't1'
        assert user.last_name == 't2'
        assert user.email == 'e@example.com'

    ___ test_str  user):
        pattern _ 'User: <{id}: {name}>'
        assert str(user) == pattern.f..(id_user.id,
                                           name_user.get_full_name())

    ___ test_full_name  user):
        pattern _ '{} {}'
        assert user.get_full_name() == \
               pattern.f..(user.first_name, user.last_name)

    ___ test_list
        assert [1, 2, 3] == [1, 2, 3]
        # assert [1, 2, 3] == [1, 2, 4]

    ___ test_mocker  mocker):
        mocked_dt _ mocker.patch('datetime.datetime')
        mocked_dt.now.return_value _ 1
        assert datetime.datetime.now() == 1
        assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 20, 3, 4, 5] == \
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
