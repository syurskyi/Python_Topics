# Python 2.7
_______ string

___ encrypt(msg_count, key):
    alphabet = string.ascii_uppercase
    alphabet_shifted = alphabet[key:] + alphabet[:key]
    caesar_shift = string.maketrans(alphabet, alphabet_shifted)
    answer    # list

    ___ msg __ r..(msg_count):
        unencrypted_msg = raw_input().upper()
        encrypted_msg = unencrypted_msg.translate(caesar_shift)
        answer.a..(encrypted_msg)
    print(' '.join(answer))

___ decrypt(msg_count, key):
    key = 26 - key
    alphabet = string.ascii_uppercase
    alphabet_shifted = alphabet[key:] + alphabet[:key]
    caesar_shift = string.maketrans(alphabet, alphabet_shifted)
    answer    # list

    ___ msg __ r..(msg_count):
        unencrypted_msg = raw_input().upper()
        encrypted_msg = unencrypted_msg.translate(caesar_shift)
        answer.a..(encrypted_msg)
    print(' '.join(answer))

___ caesar_cipher():
    encrypted_msg_count, shift_key = [int(x) ___ x __ raw_input().s.. ]
    decrypt(encrypted_msg_count, shift_key)
    #encrypt(encrypted_msg_count, shift_key)
caesar_cipher()
