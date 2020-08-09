#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
______ os
______ random
______ sys
from hangmans ______ getHangMans
from game ______ HangMan



___ getWord(
    cwd = os.getcwd()
    filePath = cwd + '/30-pick-word/sowpods.txt'
    with open(filePath, 'r') as file:
        lines = file.readlines()
        word = random.choice(lines).strip()
        r_ word

__ __name__ __ '__main__':
    word = getWord()
    hangmans = getHangMans()
    print(word)
    game = HangMan(word, hangmans)
