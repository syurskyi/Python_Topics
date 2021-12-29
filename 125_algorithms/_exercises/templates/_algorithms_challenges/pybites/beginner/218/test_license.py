____ string _______ ascii_uppercase, digits
_______ random

____ license _______ validate_license

ALPHABET = ascii_uppercase + digits


___ _create_license():
    r.. 'PB-' + '-'.join(
        [''.join(random.sample(ALPHABET, 8))
         ___ _ __ r..(4)]
    )


___ test_valid_license():
    ___ _ __ r..(10):
        key = _create_license()
        ... validate_license(key)


___ test_return_type():
    key = _create_license()
    ... validate_license(key) __ True
    ... validate_license(key[:-1]) __ False


___ test_invalid_license():
    pool = [_create_license() ___ _ __ r..(5)]
    lcase_key = pool[0].lower()
    ... n.. validate_license(lcase_key)
    shorter_key = pool[1][:-2]
    ... n.. validate_license(shorter_key)
    longer_key = pool[2] + 'A'
    ... n.. validate_license(longer_key)
    wrong_prefix = 'AB-' + pool[3][3:]
    ... n.. validate_license(wrong_prefix)
    empty_key = ''
    ... n.. validate_license(empty_key)
    key_reversed = pool[4][::-1]
    ... n.. validate_license(key_reversed)


___ test_valid_prefix():
    license = "PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"
    ... validate_license(license)
    ... n.. validate_license(license.r..('PB', 'APB'))
    ... n.. validate_license(license.r..('PB', 'COAPB'))