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
   hashed = hashlib.md5(email.l...s...encode("utf8")).hexdigest()
   base_url = "https://www.gravatar.com/avatar/"
   hash_size = f"{hashed}?s={size}&r=g&d=robohash"
   r.. f"{base_url}{hash_size}"


# if __name__ == "__main__":
#    print(create_gravatar_url("test"))