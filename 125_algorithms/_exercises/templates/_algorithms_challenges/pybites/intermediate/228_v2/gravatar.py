_______ hashlib

GRAVATAR_URL = ("https://www.gravatar.com/avatar/"
                "{hashed_email}?s={size}&r=g&d=robohash")


___ create_gravatar_url(email, size=200):
    """Use GRAVATAR_URL above to create a gravatar URL.

       You need to create a hash of the email passed in.

       PHP example: https://en.gravatar.com/site/implement/hash/

       For Python check hashlib check out (md5 / hexdigest):
       https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest
    """
    email_hash = hashlib.md5(email.lower().s...encode('utf-8'))
    hash = email_hash.hexdigest()

    r.. GRAVATAR_URL.f..(hashed_email=hash,size=size)


    






