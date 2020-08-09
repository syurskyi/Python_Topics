#/#! /urs/bin/env python

__ __name__ __ '__main__':
    firstWord = str(raw_input('Give me a first word: '))
    firstWord = firstWord.replace(" ","")

    firstWordBackword = firstWord[::-1]

    __ firstWord __ firstWordBackword:
        print("The word %s is a palindrome! (%s)"%(firstWord, firstWordBackword))
    ____
        print("The word %s is not a palindrome! (%s)"%(firstWord, firstWordBackword))