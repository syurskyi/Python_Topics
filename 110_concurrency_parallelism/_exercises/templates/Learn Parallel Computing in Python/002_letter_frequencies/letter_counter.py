______ json
______ urllib.request
______ t___
____ _ ______ T.., Lock

finished_count = 0


___ count_letters(url, frequency, mutex):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    mutex.acquire()
    ___ l __ txt:
        letter = l.lower()
        if letter __ frequency:
            frequency[letter] += 1
    global finished_count
    finished_count += 1
    mutex.release()


___ main
    frequency = {}
    mutex = Lock()
    ___ c __ "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = t___.t___()
    ___ i __ r...(1000, 1020):
        T..(t.._count_letters, a.._(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).s..
    while True:
        mutex.acquire()
        if finished_count == 20:
            break
        mutex.release()
        t___.s..(0.5)
    end = t___.t___()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)


main()
