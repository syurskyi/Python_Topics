______ j___
______ u__.r..
______ t___


___ count_letters(url, frequency):
    response = u__.r...u..(url)
    txt = s..(response.r..
    ___ l __ txt:
        letter = l.l..
        __ letter __ frequency:
            frequency[letter] += 1


___ main
    frequency = {}
    ___ c __ "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = t___.t___()
    ___ i __ r...(1000, 1020):
        count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    end = t___.t___()
    print(j___.d..(frequency, i.._4))
    print("Done, time taken", end - start)


main()
