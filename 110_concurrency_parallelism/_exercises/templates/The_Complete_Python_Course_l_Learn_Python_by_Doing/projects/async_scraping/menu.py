______ l__

____ app ______ books

logger = l__.getLogger('scraping.menu')


USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit

Enter your choice: '''


___ print_best_books
    logger.d..('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:5]
    ___ book __ best_books:
        print(book)


___ print_cheapest_books
    logger.d..('Finding best books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    ___ book __ cheapest_books:
        print(book)


books_generator = (x ___ x __ books)


___ get_next_book
    logger.d..('Getting next book from generator of all books...')
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


___ menu
    user_input = i..(USER_CHOICE)
    w... user_input != 'q':
        logger.d..('User did not choose to exit program.')
        __ user_input __ ('b', 'c', 'n'):
            user_choices[user_input]()
        ____
            print('Please choose a valid command.')
        user_input = i..(USER_CHOICE)
    logger.d..('Terminating program...')


menu()
