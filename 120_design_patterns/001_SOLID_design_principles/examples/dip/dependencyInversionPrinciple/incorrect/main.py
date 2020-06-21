# -*- coding: utf-8 -*-

# Decorator
def validate_type_hinting(func):
    def inner(*argv):
        if not isinstance(argv[1], PdfBook) : print("%s is a type %s, the function need a PdfBook type" % (argv[1], type(argv[1]))); exit(0)
        return func(*argv)
    return inner


class PdfReader(object):

    @validate_type_hinting
    def __init__(self, pdf_book):
        self._book = pdf_book

    def read(self):
        return self._book.read()

class PdfBook(object):
    
    def read(self):
        return 'pdf read!!!'

if __name__ == '__main__':
    pdf_book = PdfBook()
    pdf_reader = PdfReader(pdf_book)
    print(pdf_reader.read())