_______ journal
# from journal import load, save
# from journal import *


___ main():
    print_header()
    run_event_loop()


___ print_header():
    print('------------------------')
    print('    JOURNAL APP')
    print('------------------------')


___ run_event_loop():
    print('What do you want to do with your journal?')
    cmd  'EMPTY'
    journal_name  'default'
    journal_data  journal.load(journal_name)  # []  # list()

    w___ cmd ! 'x' a.. cmd:
        cmd  input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd  cmd.l...s..

        __ cmd __ 'l':
            list_entries(journal_data)
        ____ cmd __ 'a':
            add_entry(journal_data)
        ____ cmd ! 'x' a.. cmd:
            print("Sorry, we don't understand '{}'.".f..(cmd))

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


___ list_entries(data):
    print('Your journal entries: ')
    entries  r..(data)
    ___ idx, entry __ e..(entries):
        print('* [{}] {}'.f..(idx + 1, entry))


___ add_entry(data):
    text  input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)


# print("__file__ " + __file__)
# print("__name__ " + __name__)

__ __name__ __ '__main__':
    main()
