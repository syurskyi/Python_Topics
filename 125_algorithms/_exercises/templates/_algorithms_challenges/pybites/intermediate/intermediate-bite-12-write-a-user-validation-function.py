"""
Create a function that takes a username and checks for a valid user:

The username is in USERS,
the user is not expired, and
the user has the ADMIN role.
If those 3 conditions are met return SECRET.

If one of the conditions is not True raise an exception you define yourself: UserDoesNotExist,
UserAccessExpired and UserNoPermission respectively. Check out the tests for more detail.
"""

____ collections _______ n..

# https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python
User = n..('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=F..)
bob = User(name='Bob', role=USER, expired=T..)
pybites = User(name='PyBites', role=ADMIN, expired=F..)
USERS = (julian, bob, pybites)

# define exception classes here
c_ UserDoesNotExist(Exception):
    p..

c_ UserAccessExpired(Exception):
    p..

c_ UserNoPermission(Exception):
    p..

### My solution

___ get_secret_token(username):
    ___ user __ USERS:
        __ user.name __ username:
            __ user.expired __ F..:
                __ user.role __ ADMIN:
                    r.. SECRET
                ____:
                    raise UserNoPermission
            ____:
                raise UserAccessExpired
    raise UserDoesNotExist

### PyBites original solution

___ pyb_get_user(username):
    # This constructs a dictionary from USERS namedtuples
    users = {user.name: user ___ user __ USERS}
    # Q: Is there any difference in accessing nonexisting key when using d[crap] vs d.get(crap)?
    # A: Yes, there is.
    # https://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey
    # So if user does not exist, None is returned
    # https://stackoverflow.com/questions/9494404/use-of-true-false-and-none-as-return-values-in-python-functions
    # https://stackoverflow.com/questions/21095654/what-is-a-nonetype-object
    # https://stackoverflow.com/questions/23086383/how-to-test-nonetype-in-python
    # https://stackoverflow.com/questions/19473185/what-is-a-none-value
    r.. users.get(username)

___ pyb_get_secret_token(username):
    user = pyb_get_user(username)
    print(t..(user))
    print(user)
    # Big question here how to test for None: if not x vs if x is None
    # https://stackoverflow.com/questions/24270344/is-there-a-difference-between-if-not-x-and-if-x-is-none
    # https://amir.rachum.com/blog/2012/08/25/you-cant-handle-the-truth/
    # https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
    # https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
    __ n.. user:
        raise UserDoesNotExist

    __ user.expired:
        raise UserAccessExpired

    __ user.role != ADMIN:
        raise UserNoPermission

    r.. SECRET




try:
    print(pyb_get_secret_token('Tim'))
except UserAccessExpired __ e:
    print("Caught exception UserAccessExpired")
except UserNoPermission __ e:
    print("Caught exception UserNoPermission")
except UserDoesNotExist __ e:
    print("Caught exception UserDoesNotExist")
