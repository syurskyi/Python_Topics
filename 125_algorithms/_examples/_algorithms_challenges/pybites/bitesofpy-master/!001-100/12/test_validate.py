import pytest

from validate import (get_secret_token, SECRET,
                      UserDoesNotExist, UserAccessExpired, UserNoPermission)


def test_get_secret_token():
    a__ issubclass(UserDoesNotExist, Exception)
    a__ issubclass(UserAccessExpired, Exception)
    a__ issubclass(UserNoPermission, Exception)

    with pytest.raises(UserDoesNotExist):
        get_secret_token('Tim')
    with pytest.raises(UserAccessExpired):
        get_secret_token('Bob')
    with pytest.raises(UserNoPermission):
        get_secret_token('Julian')

    a__ get_secret_token('PyBites') == SECRET