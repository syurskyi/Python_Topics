# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# Decorator
def validate_type_hinting(func):
    def inner(*argv):
        if not issubclass(type(argv[1]), Ebook) : print("%s is a type %s, the function need a Ebook type" % (argv[1], type(argv[1]))); exit(0)
        return func(*argv)
    return inner


# Abstract Desing
class EbookReader(object):
    
    @validate_type_hinting
    def __init__(self, ebook):
        self._ebook = ebook

    def read(self):
        return self._ebook.read()

# Interface
class Ebook(object):
    __metaclass__ = ABCMeta

    def read(self): raise NotImplementedError

# Detail Class
class PdfEbook(Ebook):
    def read(self):
        return 'pdf read!!!'

if __name__ == '__main__':
    pdf_ebook = PdfEbook()
    ebook_reader = EbookReader(pdf_ebook)
    print(ebook_reader.read())
