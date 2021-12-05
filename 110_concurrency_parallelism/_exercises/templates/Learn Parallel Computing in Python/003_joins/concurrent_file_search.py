______ os
____ os.path ______ isdir, join
____ _ ______ L..., T..

mutex = L...()
matches = []


___ file_search(root, filename):
    print("Searching in:", root)
    child_threads = []
    ___ file __ os.listdir(root):
        full_path = join(root, file)
        __ filename __ file:
            mutex.a...
            matches.append(full_path)
            mutex.r..
        __ isdir(full_path):
            t = T..(t.._file_search, a.._([full_path, filename]))
            t.s..
            child_threads.append(t)
    ___ t __ child_threads:
        t.join()


___ main
    t = T..(t.._file_search, a.._(["c:/tools", "README.md"]))
    t.s..
    t.join()
    ___ m __ matches:
        print("Matched:", m)


main()
