from collections import namedtuple

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
    
    users = [user.name for user in USERS]

    __ username not in users:
        raise UserDoesNotExist

    for user in USERS:
        __ username == user.name:
            __ user.expired == True:
                raise UserAccessExpired
            __ user.role != ADMIN:
                raise UserNoPermission

            return SECRET

# if __name__ == "__main__":
#     print(get_secret_token("Bob"))