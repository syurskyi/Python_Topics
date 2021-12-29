#The word or whole phrase which has the same sequence of letters in both directions is called a palindrome.
___ i __ r..(int(input())):
    rev_str = ''
    string = ''.join(e ___ e __ input().lower() __ e.islower())
    #here iam storing the string in the reverse form
    ___ j __ r..(l..(string)-1,-1,-1):
        rev_str += string[j]
    #once the reverse string is stored then i'm comparing it with the original string
    __ rev_str __ string:
        print('Y',' ')
    ____:
        print('N',' ')