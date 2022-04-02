____ c.. _______ n..

User = n..('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=F..)
bob = User(name='Bob', role=USER, expired=T..)
pybites = User(name='PyBites', role=ADMIN, expired=F..)
USERS = (julian, bob, pybites)


# define exception classes here
c_ UserDoesNotExist(E..
    p..


c_ UserAccessExpired(E..
    p..


c_ UserNoPermission(E..
    p..


___ get_secret_token(username
    ___ user __ USERS:
        __ user.name __ username:
            __ user.expired:
                r.. UserAccessExpired _*No access available for {username}')
            __ user.role __ ADMIN:
                r.. SECRET
            r.. UserNoPermission _*User {username} has insufficient permission')
    r.. UserDoesNotExist _*User {username} does not exist')
