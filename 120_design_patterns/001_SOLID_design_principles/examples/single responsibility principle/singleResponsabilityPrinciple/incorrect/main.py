# -*- coding: utf-8 -*-

class Book():
    def getTitle(self):
        return 'Im a title'
    
    def getAuthor(self):
        return 'Im a author'

    def printTextCurrentPage(self):
        print('Current page')

    def printHtmlCurrentPage(self):
        print('<div> Current page </div>')


if __name__ == '__main__':
    book = Book()
    book.printTextCurrentPage()
    book.printHtmlCurrentPage()