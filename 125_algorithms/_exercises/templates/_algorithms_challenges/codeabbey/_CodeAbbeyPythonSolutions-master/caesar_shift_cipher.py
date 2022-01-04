amount_values,shifter = map(i..,(input().s..()))
results    # list

___ get_cipher(words, shifter):
    cipher_word = ""
    ___ i __ words:
        cipher_char = ord(i)
        __(cipher_char < 65):
            cipher_word += chr(cipher_char)
            continue
        ____(cipher_char-shifter < 65):
            cipher_char += 26
        cipher_char -= shifter
        cipher_word += chr(cipher_char)
        
    r.. cipher_word


___ i __ r..(amount_values):
    results.a..(get_cipher(input(),shifter))

print(*results)
