amount_values,shifter m.. i..,(i.. ).s..()))
results    # list

___ get_cipher(words, shifter
    cipher_word ""
    ___ i __ words:
        cipher_char o..(i)
        __(cipher_char < 65
            cipher_word += chr(cipher_char)
            _____
        ____(cipher_char-shifter < 65
            cipher_char += 26
        cipher_char -_ shifter
        cipher_word += chr(cipher_char)
        
    r.. cipher_word


___ i __ r..(amount_values
    results.a..(get_cipher(i.. ),shifter

print(*results)
