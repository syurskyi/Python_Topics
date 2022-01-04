____ password _______ validate_password, used_passwords


___ test_password_len
    ... n.. validate_password('short')
    ... n.. validate_password('waytoolongpassword')


___ test_password_missing_chars
    ... n.. validate_password('UPPERCASE')
    ... n.. validate_password('lowercase')
    ... n.. validate_password('PW_no_digits')
    ... n.. validate_password('Pw9NoPunc')
    ... n.. validate_password('_password_')
    ... n.. validate_password('@#$$)==1')


___ test_password_only_one_letter
    ... n.. validate_password('@#$$)==1a')


___ test_validate_password_good_pws
    ... validate_password('passWord9_')
    ... validate_password('another>4Y')
    ... validate_password('PyBites@1912')
    ... validate_password('We<3Python')


___ test_password_not_used_before
    ... n.. validate_password('PassWord@1')
    ... n.. validate_password('PyBit$s9')


___ test_password_cache_cannot_reuse
    num_passwords_use = l..(used_passwords)
    ... validate_password('go1@PW')
    ... l..(used_passwords) __ num_passwords_use + 1
    ... n.. validate_password('go1@PW')