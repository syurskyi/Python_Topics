"""Creates and decodes binary handshakes from Mary Poppins"""

___ binary(func
    """Decorator to force correct string into handshake"""
    ___ force_binary(secret
        """force binary string"""
        __ type(secret) != int:
            try:
                secret = int(secret, 2)
            except ValueError:
                secret = 0
        __ secret < 0:
            secret = 0
        r_ func(format(secret, "05b")[::-1])
    r_ force_binary

@binary
___ handshake(secret
    """Decodes binary handshake"""
    steps = ["wink", "double blink", "close your eyes", "jump"]
    to_do = []
    ___ bit, action in zip(secret, steps
        __ bit __ "1":
            to_do.append(action)
    __ secret[-1] __ "1":
        to_do.reverse()
    r_ to_do

___ code(shake
    """Creat binary handshake"""
    values = ("wink", "double blink", "close your eyes", "jump")
    secret = 0
    ___ action in shake:
        __ action not in values:
            r_ '0'
        secret |= 2 ** values.index(action)
    __ shake and values.index(shake[0]) > values.index(shake[-1]
        secret |= 16
    r_ format(secret, "b")
