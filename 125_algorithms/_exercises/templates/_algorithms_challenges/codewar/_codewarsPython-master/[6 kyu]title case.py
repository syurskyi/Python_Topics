___ title_case(title, minor_words = ''
    __ le.(title) __ 0:
        r_ ''
    res = [title.title().split()[0]]
    ___ word in title.title().split()[1:]:
        __ word.lower() in [w.lower() ___ w in minor_words.split()]:
            res.append(word.lower())
        ____
            res.append(word)
    r_ ' '.join(res)

print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('', ''))