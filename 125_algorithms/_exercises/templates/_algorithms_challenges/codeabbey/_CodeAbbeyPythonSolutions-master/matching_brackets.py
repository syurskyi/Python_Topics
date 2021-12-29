import re

amount_values = int(input())
results = []

___ is_matching(word):
    word = re.sub(r"[^()[\]{}<>]","",word)

    open_brackets = ["[","(","{","<"]
    close_brackets = ["]",")","}",">"]

    open_brackets_in_word =[]
    for i in word:
        __(i in open_brackets):
            open_brackets_in_word.append(i)
        elif(i in close_brackets):
            __(len(open_brackets_in_word) == 0):
                return 0
            __(open_brackets.index(open_brackets_in_word[-1]) != close_brackets.index(i)):
                return 0
            else:
                open_brackets_in_word.pop()
    __(len(open_brackets_in_word) > 0):
        return 0
    return 1

for i in range(amount_values):
    word = input()
    results.append(is_matching(word))

print(*results)

