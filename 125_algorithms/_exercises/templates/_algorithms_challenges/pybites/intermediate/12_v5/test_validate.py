_______ pytest

____ validate _______ (get_secret_token, SECRET,
                      UserDoesNotExist, UserAccessExpired, UserNoPermission)


___ test_get_secret_token():
    ... issubclass(UserDoesNotExist, Exception)
    ... issubclass(UserAccessExpired, Exception)
    ... issubclass(UserNoPermission, Exception)

    with pytest.raises(UserDoesNotExist):
        get_secret_token('Tim')
    with pytest.raises(UserAccessExpired):
        get_secret_token('Bob')
    with pytest.raises(UserNoPermission):
        get_secret_token('Julian')

    ... get_secret_token('PyBites') __ SECRET