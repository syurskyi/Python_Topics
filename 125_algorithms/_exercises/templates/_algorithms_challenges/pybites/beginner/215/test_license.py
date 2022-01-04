____ s__ _______ a.., d..
_______ r__

____ license _______ validate_license

ALPHABET = a.. + d..


___ _create_license
    r.. 'PB-' + '-'.j..(
        [''.j..(r__.sample(ALPHABET, 8))
         ___ _ __ r..(4)]
    )


___ test_valid_license
    ___ _ __ r..(10):
        key = _create_license()
        ... validate_license(key)


___ test_return_type
    key = _create_license()
    ... validate_license(key) __ T..
    ... validate_license(key[:-1]) __ F..


___ test_invalid_license
    pool = [_create_license() ___ _ __ r..(5)]
    lcase_key = pool[0].l..
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


___ test_valid_prefix
    license = "PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"
    ... validate_license(license)
    ... n.. validate_license(license.r..('PB', 'APB'))
    ... n.. validate_license(license.r..('PB', 'COAPB'))