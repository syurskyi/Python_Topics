from password import validate_password, used_passwords


def test_password_len():
    a__ not validate_password('short')
    a__ not validate_password('waytoolongpassword')


def test_password_missing_chars():
    a__ not validate_password('UPPERCASE')
    a__ not validate_password('lowercase')
    a__ not validate_password('PW_no_digits')
    a__ not validate_password('Pw9NoPunc')
    a__ not validate_password('_password_')
    a__ not validate_password('@#$$)==1')


def test_password_only_one_letter():
    a__ not validate_password('@#$$)==1a')


def test_validate_password_good_pws():
    a__ validate_password('passWord9_')
    a__ validate_password('another>4Y')
    a__ validate_password('PyBites@1912')
    a__ validate_password('We<3Python')


def test_password_not_used_before():
    a__ not validate_password('PassWord@1')
    a__ not validate_password('PyBit$s9')


def test_password_cache_cannot_reuse():
    num_passwords_use = len(used_passwords)
    a__ validate_password('go1@PW')
    a__ len(used_passwords) == num_passwords_use + 1
    a__ not validate_password('go1@PW')