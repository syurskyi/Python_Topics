# Cesear Cipher
# Question: Build a ROT13 encryption algorithm. So for example all A's translate into N's, B's translate into O's and vice-versa.
# Solutions:

class Solution:
    ___ ROT13(message):
        plaintext = list(message.lower())
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        k = 13
        cipher = ''
        ___ c __ plaintext:
            if c __ alphabet:
                cipher += alphabet[(alphabet.index(c)+k)%(len(alphabet))]
        print ( 'Your encrypted message is: ' + cipher )

Solution.ROT13("Hello There Friends!")