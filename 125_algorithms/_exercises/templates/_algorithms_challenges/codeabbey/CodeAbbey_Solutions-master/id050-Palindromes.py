___ cleanWord(data):
    word    # list
    ___ char __ data:
        __ str.isalpha(char) __ True:
            word.a..(char)
        ____:
            word.a..('')
    r.. word

___ isPalindrome(wordCount):
    answer    # list
    ___ x __ r..(wordCount):
        word = cleanWord(raw_input().lower())
        word = ''.join(word)
        __ word __ word[::-1]:
            answer.a..('Y')
        ____:
            answer.a..('N')
    print(' '.join(answer))

isPalindrome(input())
