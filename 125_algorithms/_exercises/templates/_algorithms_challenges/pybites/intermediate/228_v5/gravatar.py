_______ hashlib

GRAVATAR_URL = ("https://www.gravatar.com/avatar/"
                "{hashed_email}?s={size}&r=g&d=robohash")


___ create_gravatar_url(email: s.., size=200):
    """Use GRAVATAR_URL above to create a gravatar URL.

       You need to create a hash of the email passed in.

       PHP example: https://en.gravatar.com/site/implement/hash/

       For Python check hashlib check out (md5 / hexdigest):
       https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest
    """
    r.. GRAVATAR_URL.f..(hashed_email=hashlib.md5(email.s...l...encode('utf-8')).hexdigest(),
                               size=size)
