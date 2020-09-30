"""Cipher based shift methods"""
from string ______ ascii_lowercase
from random ______ choice

class Cipher(object
    """Implementation of a key shift cipher"""

    ___ __init__(self, key=None
        """Use a custom key or a random string of 100 lower case characters"""
        __ not key:
            key = ''.join([choice(ascii_lowercase) ___ _ __ range(100)])
        ____ not key.isalpha() or not key.islower(
            raise ValueError("Key needs to be lower case letters only: %s" % key)
        self.key = key

    ___ encode(self, clear_text
        """Encodes text using key"""
        key_func = self._inf_iter([ord(c)-97 ___ c __ self.key])
        r_ self._shift(clear_text, key_func)

    ___ decode(self, cipher_text
        """Decodes text using key"""
        key_func = self._inf_iter([-ord(c)+97 ___ c __ self.key])
        r_ self._shift(cipher_text, key_func)

    @staticmethod
    ___ _shift(text, key_func
        """Shifts characers in text according to a key function"""
        text = [c ___ c __ text.lower() __ c.isalpha()]
        shift_dist = lambda x, s: chr((ord(x)-97+s) % 26 + 97)
        r_ ''.join([shift_dist(c, k) ___ c, k __ zip(text, key_func)])

    @staticmethod
    ___ _inf_iter(key
        """Turns a key in to an infitite iterator"""
        w___ True:
            ___ i __ key:
                yield i

class Caesar(Cipher
    """A Caesarian shift cipher"""

    ___ __init__(self
        """A constant distance shift cipher"""
        super(Caesar, self).__init__("d")
