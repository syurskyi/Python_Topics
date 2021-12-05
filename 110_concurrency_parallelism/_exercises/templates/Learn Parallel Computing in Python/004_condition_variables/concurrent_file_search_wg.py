______ __
____ __.p.. ______ i.., j..
____ _ ______ L..., T..

____ condition_variables.wait_group ______ WaitGroup

mutex = L...()
matches = []


___ file_search(root, filename, wait_group):
    print("Searching in:", root)
    ___ file __ __.listdir(root):
        full_path = j..(root, file)
        __ filename __ file:
            mutex.a...
            matches.a..(full_path)
            mutex.r..
        __ i..(full_path):
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
