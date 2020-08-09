___ cleanWord(data
    word = []
    ___ char in data:
        __ str.isalpha(char) __ True:
            word.append(char)
        ____
            word.append('')
    r_ word

___ isPalindrome(wordCount
    answer = []
    ___ x in range(wordCount
        word = cleanWord(raw_input().lower())
        word = ''.join(word)
        __ word __ word[::-1]:
            answer.append('Y')
        ____
            answer.append('N')
    print(' '.join(answer))

isPalindrome(input())
