______ json
______ urllib.request
______ t___


___ count_letters(url, frequency):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    ___ l __ txt:
        letter = l.lower()
        if letter __ frequency:
            frequency[letter] += 1


___ main
    frequency = {}
    ___ c __ "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = t___.t___()
    ___ i __ r...(1000, 1020):
        count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    end = t___.t___()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)


main()
