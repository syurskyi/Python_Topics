_______ movie_svc
_______ requests.exceptions


___ main
    print_header()
    search_event_loop()


___ print_header
    print('--------------------------------')
    print('        MOVIE SEARCH APP')
    print('--------------------------------')
    print()


___ search_event_loop
    s..  'ONCE_THROUGH_LOOP'

    w___ s.. ! 'x':
        ___
            s..  input('Movie search text (x to exit): ')
            __ s.. ! 'x':
                results  movie_svc.find_movies(s..)
                print("Found {} results.".f..(l..(results)))
                ___ r __ results:
                    print('{} -- {}'.f..(
                        r.year, r.title
                    ))
                print()
        ______ V..
            print("Error: Search text is required")
        ______ requests.exceptions.ConnectionError:
            print("Error: Your network is down.")
        ______ E.. __ x:
            print("Unexpected error. Details: {}".f..(x))

    print('exiting...')


__ _____ __ _____
    main()
