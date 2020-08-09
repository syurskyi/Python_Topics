______ re

amount_values = int(input())
results = []

___ is_matching(word
    word = re.sub(r"[^()[\]{}<>]","",word)

    open_brackets = ["[","(","{","<"]
    close_brackets = ["]",")","}",">"]

    open_brackets_in_word =[]
    for i in word:
        __(i in open_brackets
            open_brackets_in_word.append(i)
        ____(i in close_brackets
            __(le.(open_brackets_in_word) __ 0
                r_ 0
            __(open_brackets.index(open_brackets_in_word[-1]) != close_brackets.index(i)):
                r_ 0
            ____
                open_brackets_in_word.pop()
    __(le.(open_brackets_in_word) > 0
        r_ 0
    r_ 1

for i in range(amount_values
    word = input()
    results.append(is_matching(word))

print(*results)

