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
    
    users = [user.name ___ user __ USERS]

    __ username n.. __ users:
        raise UserDoesNotExist

    ___ user __ USERS:
        __ username __ user.name:
            __ user.expired __ T..:
                raise UserAccessExpired
            __ user.role != ADMIN:
                raise UserNoPermission

            r.. SECRET

# if __name__ == "__main__":
#     print(get_secret_token("Bob"))