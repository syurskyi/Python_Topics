______ os
____ os.path ______ isdir, join
____ _ ______ Lock, T..

____ condition_variables.wait_group ______ WaitGroup

mutex = Lock()
matches = []


___ file_search(root, filename, wait_group):
    print("Searching in:", root)
    ___ file __ os.listdir(root):
        full_path = join(root, file)
        if filename __ file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            wait_group.add(1)
            t = T..(t.._file_search, a.._([full_path, filename, wait_group]))
            t.s..
    wait_group.done()


___ main
    wait_group = WaitGroup()
    wait_group.add(1)
    t = T..(t.._file_search, a.._(["c:/tools", "README.md", wait_group]))
    t.s..
    wait_group.wait()
    ___ m __ matches:
        print("Matched:", m)


main()
