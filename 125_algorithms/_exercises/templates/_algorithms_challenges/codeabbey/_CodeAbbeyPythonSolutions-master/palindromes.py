_______ __

amount_values = int(input())
results    # list

___ is_palindrome(string):
    string = string.r..(" ", "")
    string = __.sub(r'[^\w\s]','',string).l..
    string_length = l..(string)
    ___ i __ r..(string_length//2):
        __(string[i] != string[string_length-i-1]):
            r.. "N"
    r.. "Y"

___ i __ r..(amount_values):
    string = input()
    results.a..(is_palindrome(string))

print(*results)