_______ p__

____ validate _______ (get_secret_token, SECRET,
                      UserDoesNotExist, UserAccessExpired, UserNoPermission)


___ test_get_secret_token
    ... issubclass(UserDoesNotExist, E..)
    ... issubclass(UserAccessExpired, E..)
    ... issubclass(UserNoPermission, E..)

    w__ p__.r..(UserDoesNotExist):
        get_secret_token('Tim')
    w__ p__.r..(UserAccessExpired):
        get_secret_token('Bob')
    w__ p__.r..(UserNoPermission):
        get_secret_token('Julian')

    ... get_secret_token('PyBites') __ SECRET
