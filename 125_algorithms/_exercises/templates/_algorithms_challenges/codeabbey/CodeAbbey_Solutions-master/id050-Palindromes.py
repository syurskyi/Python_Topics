___ cleanWord(data):
    word = []
    for char in data:
        __ str.isalpha(char) == True:
            word.append(char)
        else:
            word.append('')
    return word

___ isPalindrome(wordCount):
    answer = []
    for x in range(wordCount):
        word = cleanWord(raw_input().lower())
        word = ''.join(word)
        __ word == word[::-1]:
            answer.append('Y')
        else:
            answer.append('N')
    print(' '.join(answer))

isPalindrome(input())
