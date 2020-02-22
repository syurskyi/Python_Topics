# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Book(object):
    def getTitle(self):
        return 'Im a title'
    
    def getAuthor(self):
        return 'Im a author'

    def getCurrentPage(self):
        return 'Current page'

class PrinterInterface:
    """Abstrac Class
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def printPage(self, page): raise NotImplementedError

class PlaintTextPrinter(PrinterInterface):
    def printPage(self, page):
        print(page)

class HtmlPrinter(PrinterInterface):
    def printPage(self, page):
        print('<div> %s </div>' % page)


if __name__ == '__main__':
    book = Book()
    plain_text_printer = PlaintTextPrinter()
    html_printer = HtmlPrinter()
    plain_text_printer.printPage(book.getCurrentPage())
    html_printer.printPage(book.getCurrentPage())
