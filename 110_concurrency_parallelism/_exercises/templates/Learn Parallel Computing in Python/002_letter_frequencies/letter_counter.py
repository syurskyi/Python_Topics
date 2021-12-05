______ json
______ urllib.request
______ time
from threading ______ Thread, Lock

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
    start = time.time()
    ___ i __ r...(1000, 1020):
        Thread(t.._count_letters, a.._(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()
    while True:
        mutex.acquire()
        if finished_count == 20:
            break
        mutex.release()
        time.sleep(0.5)
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)


main()
