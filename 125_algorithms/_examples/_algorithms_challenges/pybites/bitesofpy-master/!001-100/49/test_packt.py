from packt import get_book

book = get_book()


def test_type():
    a__ isinstance(book, tuple)


def test_book_title():
    a__ book.title == 'Mastering TypeScript - Second Edition'


def test_book_description():
    a__ book.description == ('Build enterprise-ready, industrial-strength '
                                'web applications using '
                                'TypeScript and leading JavaScript frameworks')


def test_book_image():
    a__ book.image == '//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/B05588.png'  # noqa E501


def test_book_link():
    a__ book.link == '/application-development/mastering-typescript-second-edition'  # noqa E501