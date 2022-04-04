_______ p__

____ best_programming_books _______ Book, display_books, load_data


?p__.f..(scope="session")
___ dummy_book
    title = "Python Testing with pytest"
    author = "Okken, Brian"
    year = 2017
    rank = 1
    rating = 5
    r.. Book(title, author, year, rank, rating)


?p__.f..(scope="session")
___ python_books
    data = load_data()
    __ isi..(data, l..
        r.. data
    r.. l..(data)


___ test_book_class_incorrectly
    w__ p__.r.. T..
        Book()


___ test_book_class(dummy_book
    ... dummy_book.title __ "Python Testing with pytest"
    ... dummy_book.author __ "Okken, Brian"
    ... dummy_book.year __ 2017
    ... dummy_book.rank __ 1
    ... dummy_book.rating __ 5


___ test_book_class_str(dummy_book
    a.. = s..(dummy_book)
    e.. = ("[001] Python Testing with pytest (2017)"
                "\n      Okken, Brian 5.0")
    ... a.. __ e..


___ test_load_data(python_books
    ... l..(python_books) __ 36
    ... python_books[0].author __ "Bader, Dan"
    ... python_books[-1].title __ "Python for Tweens and Teens"
    ... python_books[10].rating __ 4.66


?p__.m__.p.(
    "index, expected",
    [
        (0, "[001] Python Tricks (2017)"),
        (1, "      Bader, Dan 4.74"),
        (2, "[002] Mastering Deep Learning Fundamentals with Python (2019)"),
        (3, "      Wilson, Richard 4.7"),
        (4, "[006] Python Programming (2019)"),
        (5, "      Fedden, Antony Mc 4.68"),
        (6, "[007] Python Programming (2019)"),
        (7, "      Mining, Joseph 4.68"),
        (8, "[009] A Smarter Way to Learn Python (2017)"),
        (9, "      Myers, Mark 4.66"),
        (10, "[010] Python Crash Course (2019)"),
        (11, "      Robert, Antonio 4.66"),
        (12, "[011] PYTHON PROGRAMMING (2019)"),
        (13, "      Campbell, Clive 4.66"),
        (14, "[012] Python Programming (2019)"),
        (15, "      Harvard, Chris 4.66"),
        (16, "[013] Python Programming (2019)"),
        (17, "      Samelson, Steven 4.66"),
        (18, "[014] Python Programming (2019)"),
        (19, "      James, Thomas 4.65"),
    ],
)
___ test_display_books(python_books, index, e.., capfd
    display_books(python_books, year=2017)
    output = ?.r .. 0].s..
    ... output[index] __ e..


?p__.m__.p.(
    "limit, expected", [(40, 72), (53, 72), (69, 72), (100, 72), (1000, 72)]
)
___ test_display_books_plus(python_books, limit, e.., capfd
    display_books(python_books, limit=limit)
    output = ?.r .. 0].s..
    ... l.. ?  __ e..