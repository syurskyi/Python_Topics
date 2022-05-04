____ c.. _______ n..

____ ___ _______ B.. __ S..
_______ r__

PACKT 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT r__.g.. ? .t..

Book n..('Book', 'title description image link')


___ get_book
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    p..

    soup S.. ? 'html.parser')

    title ?.f.. 'div', c.._'dotd-title').h2.?.s..

    description ?.s.. '.dotd-main-book-summary div' 2 .?.s..


    image ?.f.. 'img', c.._"bookimage imagecache imagecache-dotd_main_image") 'src'

    link ?.s.. ".dotd-main-book-image a" 0 'href'

    r.. Book(title,description,image,link)


#print(main_book.prettify)

print(get_book