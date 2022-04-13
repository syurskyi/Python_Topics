# ____ ? _______ v.. u..
#
#
# ___ test_password_len
#     ... n.. ? 'short'
#     ... n.. ? 'waytoolongpassword'
#
#
# ___ test_password_missing_chars
#     ... n.. ? 'UPPERCASE'
#     ... n.. ? 'lowercase'
#     ... n.. ? 'PW_no_digits'
#     ... n.. ? 'Pw9NoPunc'
#     ... n.. ? '_password_'
#     ... n.. ? '@#$$)==1'
#
#
# ___ test_password_only_one_letter
#     ... n.. ? '@#$$)==1a'
#
#
# ___ test_validate_password_good_pws
#     ... ? 'passWord9_'
#     ... ? 'another>4Y'
#     ... ? 'PyBites@1912'
#     ... ? 'We<3Python'
#
#
# ___ test_password_not_used_before
#     ... n.. ? 'PassWord@1'
#     ... n.. ? 'PyBit$s9'
#
#
# ___ test_password_cache_cannot_reuse
#     num_passwords_use l.. u..
#     ... ? 'go1@PW'
#     ... l.. u.. __ n.. + 1
#     ... n.. ? 'go1@PW')