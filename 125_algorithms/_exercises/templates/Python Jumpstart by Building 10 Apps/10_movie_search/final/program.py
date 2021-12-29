import movie_svc
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('--------------------------------')
    print('        MOVIE SEARCH APP')
    print('--------------------------------')
    print()


def search_event_loop():
    search  'ONCE_THROUGH_LOOP'

    w___ search ! 'x':
        try:
            search  input('Movie search text (x to exit): ')
            __ search ! 'x':
                results  movie_svc.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.year, r.title
                    ))
                print()
        except ValueError:
            print("Error: Search text is required")
        except requests.exceptions.ConnectionError:
            print("Error: Your network is down.")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print('exiting...')


__ __name__ __ '__main__':
    main()
