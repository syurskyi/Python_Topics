____ collections _______ n..

User = n..('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=F..)
bob = User(name='Bob', role=USER, expired=T..)
pybites = User(name='PyBites', role=ADMIN, expired=F..)
USERS = (julian, bob, pybites)


# define exception classes here
c_ UserDoesNotExist(Exception):
    pass


c_ UserAccessExpired(Exception):
    pass


c_ UserNoPermission(Exception):
    pass


___ get_secret_token(username):
    ___ user __ USERS:
        __ user.name __ username:
            __ user.expired:
                raise UserAccessExpired(f'No access available for {username}')
            __ user.role __ ADMIN:
                r.. SECRET
            raise UserNoPermission(f'User {username} has insufficient permission')
    raise UserDoesNotExist(f'User {username} does not exist')
