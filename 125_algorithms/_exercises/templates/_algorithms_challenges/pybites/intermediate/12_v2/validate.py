____ collections _______ namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here


class UserDoesNotExist(Exception):
    pass

class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


___ get_secret_token(username):
    

    ___ user __ USERS:
        __ user.name __ username:
            break
    ____:
        raise UserDoesNotExist

    __ user.expired:
        raise UserAccessExpired

    __ user.role != ADMIN:
        raise UserNoPermission

    r.. SECRET








