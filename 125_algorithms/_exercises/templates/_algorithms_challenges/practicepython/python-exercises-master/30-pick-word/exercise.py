#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
______ os
______ random

___ countWords(uri
    count = 0
    with open(filePath, 'r') as open_file:
        line = open_file.readline()
        w___ line:
            count += 1
            line = open_file.readline()
    r_ count

___ getWord(int, filePath
    count = 0
    with open(filePath, 'r') as open_file:
        line = open_file.readline()
        w___ line:
            count += 1
            line = open_file.readline()
            __ count __ int:
                result = line
                line = False
    r_ result

__ __name__ __ '__main__':
    cwd = os.getcwd()
    filePath = cwd + '/30-pick-word/sowpods.txt'
    with open(filePath, 'r') as file:
        lines = file.readlines()
        word = random.choice(lines).strip()
        print(word)
    # le. = countWords(filePath)
    # random = random.randint(0,le.+1)
    # word = getWord(random, filePath)
    # print(word, end= '')
