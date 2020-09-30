# Cesear Cipher
# Question: Build a ROT13 encryption algorithm. So for example all A's translate into N's, B's translate into O's and vice-versa.
# Solutions:

c_ Solution:
    ___ ROT13(message):
        plaintext _ li..(message.lower
        alphabet _ li..('abcdefghijklmnopqrstuvwxyz')
        k _ 13
        cipher _ ''
        ___ c __ plaintext:
            __ c __ alphabet:
                cipher +_ alphabet[(alphabet.index(c)+k)%(le.(alphabet))]
        print ( 'Your encrypted message is: ' + cipher )

Solution.ROT13("Hello There Friends!")