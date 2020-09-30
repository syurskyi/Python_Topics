results =   # list
words = input()
words_list = list(words.split())[:-1]
words_list.sort()

word = ""
___ i __ words_list:
    __(words.index(i) __ words.index(word) and i not __ results
        results.append(i)        
    word = i

print(*results)