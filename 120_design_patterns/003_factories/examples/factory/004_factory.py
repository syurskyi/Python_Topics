# coding: utf-8

class Document(object):
    def show(self):
        raise NotImplementedError()


class ODFDocument(Document):
    def show(self):
        print('Open document format')


class MSOfficeDocument(Document):
    def show(self):
        print('MS Office document format')


class Application(object):
    def create_document(self, type_):
        # параметризованный фабричный метод `create_document`
        raise NotImplementedError()


class MyApplication(Application):
    def create_document(self, type_):
        if type_ == 'odf':
            return ODFDocument()
        elif type_ == 'doc':
            return MSOfficeDocument()


app = MyApplication()
app.create_document('odf').show()  # Open document format
app.create_document('doc').show()  # MS Office document format